import os
import random
import shutil
import json
from faker import Faker
from datetime import datetime, timedelta

# --- CONFIGURAÇÕES INICIAIS ---
QTD_TOTAL = 1000
SPLIT_TREINO = 0.8  # 80% treino, 20% teste
OUTPUT_DIR = "data_test/dataset"

fake = Faker('pt_BR')


bancos_configs = [
    {
        "nome": "Nubank",
        "endereco": "Nu Pagamentos S.A. - CNPJ: 18.236.120/0001-58\nRua Capote Valente, 39 - Pinheiros, SP",
        "estilo_data": "%d %b", # 05 FEV
        "termos_rodape": ["Pagamento antecipado", "Custo Efetivo Total", "IOF"]
    },
    {
        "nome": "Banco do Brasil",
        "endereco": "Banco do Brasil S.A. - SAUN Quadra 5, Lote B, Torre I, Brasilia - DF",
        "estilo_data": "%d/%m", # 05/02
        "termos_rodape": ["Encargos financeiros", "Ouvidoria BB 0800", "Deficiente Auditivo"]
    },
    {
        "nome": "Itaú",
        "endereco": "Itaú Unibanco S.A. - Praça Alfredo Egydio de Souza Aranha, 100, SP",
        "estilo_data": "%d/%m/%Y", # 05/02/2026
        "termos_rodape": ["CET anual", "Juros do rotativo", "Pague suas contas em dia"]
    }
]

descricoes_transacoes = {
    "servicos": [
        "UBER *TRIP", "99APP *CORRIDA", "IFOOD *OSASCO", "NETFLIX.COM", 
        "SPOTIFY", "APPLE.COM/BILL", "GOOGLE CLOUD", "AWS EMEA", "CLOUDFLARE"
    ],
    "varejo": [
        "MERCADOLIVRE", "AMAZON MKTPLACE", "MAGAZINE LUIZA", "LOJAS RENNER", 
        "DROGARIA SAO PAULO", "MC DONALDS", "BURGER KING", "POSTO IPIRANGA"
    ],
    "caos": [
        "PAG*JoseSilva", "SUMUP*Lanchonete", "DL*GOOGLE", "EBN*SPOTIFY", 
        "MP *MERCADOPAGO", "IOF COMPRA INTERNACIONAL", "TARIFA BANCARIA"
    ]
}

locais_sujos = ["SAO PAULO BR", "SP", "OSASCO", "CURITIBA PR", "RIO DE JANEIR", ""]


def formatar_moeda(valor):
    """Formata float para string R$ 0,00"""
    return f"R$ {valor:.2f}".replace('.', ',')

def gerar_item_transacao():
    """
    Gera os DADOS da transação (sem formatação visual ainda).
    Retorna um dicionário com os dados brutos.
    """
    # 1. Data
    data_obj = fake.date_between(start_date='-30d', end_date='today')
    
    # 2. Valor
    valor = random.uniform(5, 500)
    
    # 3. Descrição Base
    categoria_key = random.choice(list(descricoes_transacoes.keys()))
    desc_base = random.choice(descricoes_transacoes[categoria_key])
    
    # 4. Adiciona "Caos" na Descrição (Isso vai tanto para o JSON quanto para o Texto)
    fator_caos = random.random()
    descricao_final = desc_base
    
    if fator_caos < 0.3:
        descricao_final = f"{desc_base} {random.choice(locais_sujos)}"
    elif fator_caos < 0.5:
        # Simula erro de OCR colando texto (ex: MERCADOLIVRE sem espaço)
        descricao_final = desc_base.replace(" ", "")
    elif fator_caos < 0.6:
        # Adiciona parcela
        descricao_final = f"{desc_base} PARC 0{random.randint(1,5)}/12"
        
    return {
        "date_obj": data_obj,
        "description": descricao_final.strip(),
        "value": valor,
        "category_group": categoria_key # Apenas para saber se é taxa
    }

def renderizar_linha_texto(dados, estilo_data):
    """
    Pega o dado bruto e transforma na linha de texto 'suja' para o PDF/TXT.
    """
    # Formata data conforme o banco
    dt_str = dados['date_obj'].strftime(estilo_data).upper()
    
    # Formata valor (às vezes remove o R$ para dificultar)
    str_valor = formatar_moeda(dados['value'])
    if random.choice([True, False]):
        str_valor = str_valor.replace("R$ ", "") # Deixa só o número

    # Espaçamento irregular
    espacos1 = " " * random.randint(2, 10)
    espacos2 = " " * random.randint(2, 15)
    
    return f"{dt_str}{espacos1}{dados['description']:<30}{espacos2}{str_valor}"

# --- 3. GERADOR DO PAR (TXT + JSON) ---

def gerar_fatura_completa(index):
    banco = random.choice(bancos_configs)
    nome_cliente = fake.name().upper()
    cpf = fake.cpf()
    data_venc = fake.date_this_month().strftime("%d/%m/%Y")
    
    # Listas para o TXT e Lista para o JSON
    linhas_txt = []
    itens_json = []
    total_acumulado = 0.0
    taxas_acumuladas = 0.0
    
    # --- CABEÇALHO DO TXT ---
    estilo_cabecalho = random.randint(1, 3)
    if estilo_cabecalho == 1:
        linhas_txt.append(f"{banco['nome'].upper()} - FATURA DO CARTÃO")
        linhas_txt.append(f"CLIENTE: {nome_cliente}  CPF: {cpf}")
    elif estilo_cabecalho == 2:
        linhas_txt.append(f"Olá, {nome_cliente.split()[0]}")
        linhas_txt.append(f"Sua fatura de {fake.month_name().upper()} chegou")
    else:
        linhas_txt.append(f"DEMONSTRATIVO MENSAL - {banco['nome']}")
        linhas_txt.append(f"{nome_cliente} | {cpf} | VENC: {data_venc}")
    
    linhas_txt.append("-" * 60)
    
    # --- CORPO DAS TRANSAÇÕES ---
    # Nota: O resumo financeiro no topo muitas vezes é calculado DEPOIS, 
    # mas em TXT streamado imprimimos antes. Vamos simular um valor aproximado no topo
    # e o valor exato no JSON.
    linhas_txt.append("DATA           DESCRIÇÃO                        VALOR")
    linhas_txt.append("")
    
    num_transacoes = random.randint(5, 15)
    
    for _ in range(num_transacoes):
        # 1. Gera o Dado Bruto
        dados_item = gerar_item_transacao()
        
        # 2. Adiciona ao JSON (Estruturado e Limpo)
        item_para_json = {
            "date": dados_item['date_obj'].strftime("%d/%m/%Y"),
            "description": dados_item['description'],
            "value": formatar_moeda(dados_item['value'])
        }
        itens_json.append(item_para_json)
        
        # 3. Contabiliza Totais
        total_acumulado += dados_item['value']
        if "IOF" in dados_item['description'] or "TARIFA" in dados_item['description']:
            taxas_acumuladas += dados_item['value']
            
        # 4. Adiciona ao TXT (Com ruído visual)
        # 10% de chance de inserir uma categoria aleatória solta no meio do texto
        if random.random() < 0.1:
            linhas_txt.append(random.choice(["Lazer", "Serviços", "Alimentação", "Saúde"]))
            
        linha_renderizada = renderizar_linha_texto(dados_item, banco['estilo_data'])
        linhas_txt.append(linha_renderizada)
        
    linhas_txt.append("")
    linhas_txt.append("-" * 60)
    
    # --- TOTAIS E RODAPÉ ---
    # No TXT, colocamos o total calculado
    linhas_txt.append(f"TOTAL DA FATURA: {formatar_moeda(total_acumulado)}")
    linhas_txt.append(f"PAGAMENTO MÍNIMO: {formatar_moeda(total_acumulado*0.15)}")
    
    linhas_txt.append("INFORMAÇÕES ADICIONAIS")
    for frase in random.sample(banco['termos_rodape'], k=2):
        linhas_txt.append(f"* {frase}: Consultar taxas vigentes no app.")
    linhas_txt.append(f"Endereço: {banco['endereco']}")
    linhas_txt.append(f"Página 1/1 - Gerado em {datetime.now().strftime('%d/%m/%Y')}")

    # --- MONTAGEM DO JSON FINAL ---
    objeto_json = {
        "Invoice": {
            "total": formatar_moeda(total_acumulado),
            "spents": itens_json,
            "tax": formatar_moeda(taxas_acumuladas)
        }
    }
    
    texto_completo = "\n".join(linhas_txt)
    return texto_completo, objeto_json

# --- 4. ORQUESTRADOR PRINCIPAL ---

def main():
    # 1. Limpa e cria diretórios
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    
    dir_treino = os.path.join(OUTPUT_DIR, "train")
    dir_teste = os.path.join(OUTPUT_DIR, "test")
    
    os.makedirs(dir_treino)
    os.makedirs(dir_teste)
    
    print(f"--- Iniciando Geração de {QTD_TOTAL} Pares (TXT + JSON) ---")
    print(f"Diretório: {OUTPUT_DIR}/")
    
    # 2. Loop de Geração
    for i in range(1, QTD_TOTAL + 1):
        texto, gabarito_json = gerar_fatura_completa(i)
        
        # Decide para onde vai (Split Treino/Teste)
        if i <= QTD_TOTAL * SPLIT_TREINO:
            pasta_destino = dir_treino
        else:
            pasta_destino = dir_teste
            
        # Salva TXT
        caminho_txt = os.path.join(pasta_destino, f"fatura_{i}.txt")
        with open(caminho_txt, "w", encoding="utf-8") as f:
            f.write(texto)
            
        # Salva JSON
        caminho_json = os.path.join(pasta_destino, f"fatura_{i}.json")
        with open(caminho_json, "w", encoding="utf-8") as f:
            json.dump(gabarito_json, f, indent=4, ensure_ascii=False)
            
        if i % 100 == 0:
            print(f"Progresso: {i}/{QTD_TOTAL} faturas geradas...")

    print("\n--- Processo Concluído! ---")
    print(f"Arquivos na pasta 'train': {int(QTD_TOTAL * SPLIT_TREINO)}")
    print(f"Arquivos na pasta 'test': {int(QTD_TOTAL * (1 - SPLIT_TREINO))}")

if __name__ == "__main__":
    main()
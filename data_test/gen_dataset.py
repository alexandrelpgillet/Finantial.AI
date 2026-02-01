import os
import random
import shutil
import json
from faker import Faker
from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP

# --- CONFIGURAÇÕES ---
QTD_TOTAL = 1000
SPLIT_TREINO = 0.8
OUTPUT_DIR = "dataset"

fake = Faker('pt_BR')

# --- DADOS ---
bancos_configs = [
    {"nome": "Nubank", "estilo_data": "%d %b", "rodape": ["IOF", "Multa Atraso"]},
    {"nome": "Banco do Brasil", "estilo_data": "%d/%m", "rodape": ["Ouvidoria", "Deficiente Auditivo"]},
    {"nome": "Itaú", "estilo_data": "%d/%m/%Y", "rodape": ["CET", "Juros Rotativo"]}
]

descricoes_transacoes = [
    "NITROXX GAMES", "GOOGLE CLOUD", "SPOTIFY PREMIUM", "TINDER GOLD",
    "AMAZON AWS", "LOJA DO MECANICO", "EMPORIO DO AC0", "MICROSOFT AZURE",
    "OPENAI API", "NETFLIX", "IFD*RESTAURANTE", "UBER*VIAGEM",
    "POSTO IPIRANGA", "DROGASIL", "RENNER", "C&A MODAS"
]

# --- FUNÇÕES AUXILIARES ---

def criar_decimal(valor_float):
    """
    Converte um float aleatório para Decimal com exatas 2 casas.
    Ex: 10.5678 -> Decimal('10.57')
    """
    # Converte para string primeiro para evitar imprecisão do float na entrada
    d = Decimal(str(valor_float))
    return d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def formatar_moeda(valor_decimal):
    """Recebe um Decimal e retorna string 'R$ 10,00'"""
    # A formatação f"{val:.2f}" funciona bem com Decimal
    return f"R$ {valor_decimal:.2f}".replace('.', ',')

def gerar_item_compra():
    """Gera um item de compra com valor Decimal preciso"""
    desc = random.choice(descricoes_transacoes)
    
    # Adiciona variação
    if random.random() < 0.3:
        desc += f" {random.choice(['SP', 'RJ', 'BR', 'APP'])}"
        
    # Gera valor aleatório
    val_raw = random.uniform(5.00, 300.00)
    val_decimal = criar_decimal(val_raw)

    return {
        "date_obj": fake.date_between(start_date='-30d', end_date='today'),
        "description": desc,
        "value": val_decimal # Objeto Decimal
    }

def renderizar_linha_txt(dados, estilo_data):
    dt = dados['date_obj'].strftime(estilo_data).upper()
    val = formatar_moeda(dados['value'])
    
    # Simula ruído (ex: valor sem R$)
    if random.random() < 0.2:
        val = val.replace("R$ ", "")
        
    espaco = " " * random.randint(2, 15)
    return f"{dt}{espaco}{dados['description']:<25}{espaco}{val}"

# --- GERAÇÃO PRINCIPAL ---

def gerar_documento(index):
    banco = random.choice(bancos_configs)
    
    # 1. GERAÇÃO DOS DADOS (DECIMAL)
    lista_compras = []
    
    # Gera compras
    for _ in range(random.randint(5, 15)):
        lista_compras.append(gerar_item_compra())
    
    # Gera taxa (IOF) com Decimal
    taxa_raw = random.uniform(0.10, 15.00)
    valor_taxa_decimal = criar_decimal(taxa_raw)
    
    # --- CÁLCULO MATEMÁTICO SEGURO ---
    # Sum() com Decimals funciona perfeitamente sem erros de ponto flutuante
    soma_spents = sum(item['value'] for item in lista_compras)
    total_geral = soma_spents + valor_taxa_decimal
    
    # 2. MONTAGEM DO JSON (Usando os Decimals formatados)
    json_output = {
        "Invoice": {
            "total": formatar_moeda(total_geral),
            "spents": [],
            "tax": formatar_moeda(valor_taxa_decimal)
        }
    }
    
    # Ordena por data
    lista_compras.sort(key=lambda x: x['date_obj'])
    
    for item in lista_compras:
        json_output["Invoice"]["spents"].append({
            "date": item['date_obj'].strftime("%d/%m/%Y"),
            "description": item['description'],
            "value": formatar_moeda(item['value'])
        })

    # 3. MONTAGEM DO TXT
    txt_lines = []
    txt_lines.append(f"FATURA {banco['nome'].upper()}")
    txt_lines.append(f"CLIENTE: {fake.name().upper()}")
    txt_lines.append("-" * 60)
    txt_lines.append(f"TOTAL: {formatar_moeda(total_geral)}")
    txt_lines.append("-" * 60)
    txt_lines.append("DATA       HISTÓRICO                        VALOR")
    
    for item in lista_compras:
        txt_lines.append(renderizar_linha_txt(item, banco['estilo_data']))
        
    # Inserção da Taxa no texto (para a IA achar)
    txt_lines.append("")
    espacos = " " * random.randint(2, 8)
    # Data da taxa
    dt_taxa = fake.date_between(start_date='-5d', end_date='today').strftime(banco['estilo_data']).upper()
    txt_lines.append(f"{dt_taxa}{espacos}IOF / TARIFAS BANCARIAS       {formatar_moeda(valor_taxa_decimal)}")
    
    txt_lines.append("-" * 60)
    txt_lines.append(f"Subtotal: {formatar_moeda(soma_spents)}")
    txt_lines.append(f"Encargos: {formatar_moeda(valor_taxa_decimal)}")
    
    return "\n".join(txt_lines), json_output

# --- EXECUTOR ---

def main():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
        
    os.makedirs(f"{OUTPUT_DIR}/train")
    os.makedirs(f"{OUTPUT_DIR}/test")
    
    print(f"Gerando {QTD_TOTAL} arquivos com PRECISÃO DECIMAL em '{OUTPUT_DIR}'...")
    
    for i in range(1, QTD_TOTAL + 1):
        txt, gabarito = gerar_documento(i)
        
        pasta = "train" if i <= QTD_TOTAL * SPLIT_TREINO else "test"
        
        with open(f"{OUTPUT_DIR}/{pasta}/fatura_{i}.txt", "w", encoding="utf-8") as f:
            f.write(txt)
            
        with open(f"{OUTPUT_DIR}/{pasta}/fatura_{i}.json", "w", encoding="utf-8") as f:
            json.dump(gabarito, f, indent=4, ensure_ascii=False)
            
    print("Concluído! Cálculos matemáticos 100% precisos.")

if __name__ == "__main__":
    main()
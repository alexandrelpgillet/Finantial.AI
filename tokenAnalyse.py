from transformers import AutoTokenizer
import spacy
import re

text = '''Alexandre P Gillet
AV MILAO COND TOPAZIO 2295 QD09 LT0 APT504 BL03, RESIDENCIAL ELDORADO, GOIANIA, GO
- 74367635
Olá, Alexandre, esta é sua fatura de
outubro
Valor
R$415,00
Vencimento
10/10/2025
Limite único
R$2.621,00
OUROCARD FACIL VISA
Final 2923
Resumo da fatura
Saldo fatura anterior
R$ 723,26
Pagamentos/Créditos
R$ -723,26
Compras nacionais
R$ 394,23
Compras internacionais
R$ 20,77
Tarifas, encargos e multas
R$ 0,00
Total
R$ 415,00
Saldo parcelado em faturas
futuras
R$ 328,90
Opções de pagamento - Esta fatura está em Débito em Conta
Pague a fatura com Pix e libere o limite na hora
Aponte a câmera do seu celular para o QR Code acima para pagar a fatura
Pagando pelo App BB, App Ourocard, WhatsApp ou www.bb.com.br,
você também tem seu limite liberado na hora.
Pague com boleto e libere o limite em até 3 dias úteis
Você pode pagar selecionando e copiando ou digitando o código a seguir
00190.00009  02803.164017  35947.764664  9  00000000000000
Pagamento mínimo
R$ 62,26
Este  é  o  valor  mínimo  que  você  pode  pagar  para  não  ficar  em
atraso.  Você  também  pode  pagar  qualquer  valor  entre  o  valor
mínimo  e  o  valor  total  da  fatura.
Se você escolher esta opção, o valor restante será cobrado na próxima fatura + juros
de 13,76% ao mês (CET 501,23% ao ano).
Mensalidades de parcelamentos anteriores existentes nesta fatura serão incluídas
no valor do pagamento mínimo.
O saldo não pago desta fatura deverá ser quitado ou parcelado até o próximo
vencimento.
Em caso de pagamento mínimo, o valor de encargos cobrados no próximo
vencimento será de R$49,95 (conforme CET na tabela de Encargos financeiros).
Parcelamento em até 14x (entrada + 13 parcelas)
Número mínimo de parcelas:
Entrada de R$ 152,92
+2x de R$ 152,57
Total R$ 458,06
Os juros para o parcelamento desta fatura: 10,21% a.m. (CET 237,72% a.a.).
Número máximo de parcelas:
Entrada de R$ 52,55
+13x de R$ 52,52
Total R$ 735,31
Os juros para o parcelamento desta fatura: 10,21% a.m. (CET 233,47% a.a.).
Para  fazer  o  parcelamento  da  sua  fatura,  escolha  uma  opção  acima  e  pague  exatamente  o  valor  de  entrada  informado.  As  parcelas  serão  lançadas
mensalmente  nas  próximas  faturas  e  seu  limite  será  liberado  à  medida  que  elas  forem  pagas
Se você preferir parcelar com um valor ou número de parcelas diferentes, basta acessar um de nossos canais de autoatendimento, ligar na Central de
Relacionamento BB ou ir até um caixa eletrônico.
Se for pago um valor que seja menor que o valor mínimo da fatura e superior ao valor da menor entrada indicada acima, alertamos que no 5º dia útil após o
vencimento o saldo devedor será parcelado automaticamente pelo BB no prazo máximo de parcelamento.
Se você possuir parcelamentos anteriores, a mensalidade que seria debitada nesta fatura já está incluída no valor da entrada.
Para mais informações sobre o parcelamento da fatura, acesse: www.bb.com.br/ppf
Página 1/3
Informações complementares
Limite do cartão
Limite único
R$ 2.621,00
Limite único utilizado
R$ 879,00
Limite único disponível
R$ 1.742,00
Limite de saque (incluído no limite único)
R$ 0,00
Limite de saque utilizado
R$ 2.252,12
Limite de saque disponível
R$ 0,00
O limite único é o válido para todos os cartões de crédito que você
possui  no  BB.  Consulte  seu  limite  sempre  que  quiser  pelo  App  BB,
App  Ourocard,  WhatsApp  ou  bb.com.br.  Se  preferir,  você  também
pode personalizá-lo nesses canais, de acordo com a sua necessidade.
IOF nesta fatura
Saques e crédito rotativo
R$ 0,00
Pagamento de contas
R$ 0,00
Parcelamento da fatura
R$ 0,00
Compra parcelada com juros
R$ 0,00
Parcelamento de compras à vista
R$ 0,00
Total
R$0,00
Juros nesta fatura
Crédito rotativo
R$ 0,00
Saque na função crédito
R$ 0,00
Pagamento de contas
R$ 0,00
Parcelamento da fatura
R$ 0,00
Compra parcelada com juros
R$ 0,00
Parcelamento de compras à vista
R$ 0,00
Total
R$0,00
Encargos financeiros próxima fatura
Crédito rotativo*
14,16% (CET 16,53% a.m. / 526,98% a.a.)
Crédito parcelado*
5,54% (CET 6,07% a.m. / 102,91% a.a.)
Juros de mora
1,00% - Multa por atraso: 2,00%
*Considerando o valor base de R$1.000,00 de contratação para o
cálculo do CET.
Encargos financeiros nesta fatura
Crédito rotativo*
13,76% (CET 16,12% a.m. / 501,23% a.a.)
Crédito parcelado*
4,74% (CET 5,26% a.m. / 85,06% a.a.)
Juros de mora
1,00% - Multa por atraso: 2,00%
*Considerando o valor base de R$1.000,00 de contratação para o
cálculo do CET.
Pontos Livelo
No  BB  você  tem  flexibilidade  para  usar  seus
pontos como e quando quiser, direto pelo App
BB.
 Escolha
 entre
 Pontos,
 Cashback
 ou
Investimentos  no  Menu  Cartões  do  App  BB  e
aproveite!
Se  preferir,  verifique  seus  pontos  pelo  site
www.livelo.com.br  ou  App  Livelo.
Datas fatura
Fatura fechada em
30/09/2025
Fechamento da próxima fatura
29/10/2025
Melhor data de compra
30/10/2025
Valor máximo de juros e encargos
(parcelamento)
Valor original
R$ 0,00
Juros e encargos
R$ 0,00
Lançamentos nesta fatura
Confira aqui todas as compras e outros lançamentos realizados nesta fatura, feitas com o seu cartão
principal ou cartões adicionais. Lembre-se: caso ainda tenha faturas em aberto, você pode optar por
parcelar uma compra feita à vista. Saiba mais em www.bb.com.br/pcv.
Alexandre P Gillet  (Cartão 2923)
Data
   Descrição
País
Valor
    SALDO FATURA ANTERIOR
BR
R$ 723,26
    Pagamentos/Créditos
02/09
    PGTO. CASH AG.    5902 000590200  200
BR
R$ -723,26
    Lazer
05/09
    NITROXX GAMES          GOIANIA
BR
R$ 22,50
    Serviços
01/09
    DL *GOOGLE CLOUD 6BPKv Sao Pablo
BR
R$ 30,74
02/09
    EBN*SPOTIFY            CURITIBA
BR
R$ 12,90
06/09
    DM *gotindercomhelp    Sao Paulo
BR
R$ 35,99
08/09
    SPARKS COMMUNICATIONS  PETAH TIQWA
IL
R$ 20,77
    ***   3,70 DOLAR AMERICANO
    Cotação do Dólar de 08/09: R$ 5,6127
Página 2/3
10/09
    IOF - COMPRA NO EXTERIOR
R$ 0,72
29/09
    RESPONDE AI            RIO DE JANEIR
BR
R$ 47,50
    Outros lançamentos
08/09
    DL*GOOGLE 2nd Li       SAO PAULO
BR
R$ 89,99
15/09
    PPRO   *MICROSOFT      SAO PAULO
BR
R$ 25,00
19/09
    DL*GOOGLE ChatGP       SAO PAULO
BR
R$ 95,99
29/09
    PROTECAO OURO OUT/2025
BR
R$ 3,00
    Compras parceladas
01/09
    KIWIFY *Betos PARC 01/12 Natal
BR
R$ 29,90
Subtotal
R$ 415,00
Total da Fatura
R$ 415,00
Fale conosco
Atendimento 24 horas, 7 dias por semana
Central de Atendimento BB
4004 0001 ou 0800 729 0001
(para serviços transacionais, saldos, extratos,
pagamentos, resgates, transferências, demais
transações, informações e dúvidas)
Serviço de Atendimento
ao Consumidor SAC
0800 729 0722
(para atendimento de: reclamações,
cancelamentos, informações e dúvidas
gerais)
Ouvidoria BB
0800 729 5678
(reclamações não solucionadas nos canais
habituais de atendimento - agência, SAC e
demais pontos) ou acesse bb.com.br
Deficiente Auditivo ou de
Fala
0800 729 0088
Tarifas
Tabela de tarifas disponível nas
agências BB ou acesse bb.com.br
Página 3/3'''





nlp = spacy.load("pt_core_news_sm")


doc = nlp(text)

words_fix = [ 
              
              t.text for t in doc
              if t.pos_ in ["PROPN", "NUM", "NOUN", "SYM"] or t.text.lower() == "r$"
              
              ]


text_filtred = " ".join(words_fix)


tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-2b")



tokensBeforeFilter= tokenizer.encode(text)

tokensAfterFilter = tokenizer.encode(text_filtred)

print(f"Total de tokens antes do filtro = ${len(tokensBeforeFilter)}")
print(f"Total de tokens após filtro = {len(tokensAfterFilter)}")


print(f"Ganhos = {len(tokensBeforeFilter)/len(tokensAfterFilter) *100 - 100}")



output = open("textFiltred.txt", "w")

output.write(text_filtred)

output.close()


##print(text_filtred)



'A partir do .txt extraia o valor total da fatura e os faça uma tabela com a descrição de cada gasto no seguinte formato =  Data, Descrição , Valor.'








    
    
    
    
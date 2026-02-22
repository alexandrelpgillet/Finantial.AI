# Financy.AI

[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)

Financy.AI é um software como serviço (SAAS), seu propósito geral é gerenciar as despesas pessoais do usuário.


## Diferencial entre o Financy.AI e outros softwares de gestão financeira


* Integração com WhatsApp;
* Ferramentas essenciais para o usuário gerenciar suas despesas financeiras;
* Uso de IA para escanear todas as despesas financeiras em formato .pdf;

## Funcionalidades do Financy.AI

![Este é um diagrama de funcionalidades do Financy.AI](/imgs/diagramFunctionalites.svg)


## Tecnologias utilizadas no desenvolvimento do Financy.AI

|Nome|Versão|
|----|------|
|Python|3.12.3|
|Pip     |24.0|
|Google Gemini Flash|gemini-2.5-flash-lite|
|PostgreSQL| |
|Docker| |
|API Oficial do WhatsApp| |

## Bibliotecas Python utilizadas no desenvolvimento do Financy.AI

|Nome|Versão|
|----|------|
|FastAPI|0.128.0|
|Pymupdf|1.26.7|
|SpaCy|3.8.11|
|Transformers|5.0.0|
|LangChain|1.2.7|
|LangChain-Google-GenAi|4.2.0|
|Wheel| 0.46.3|
|Setup Tools| 80.10.2| 
|Python-dotenv| 1.2.1|
|Pydantic|2.12.5|
|Faker|40.1.2|
|Pytest|9.0.2|
|Flakek8|7.3.0|
|Black|26.1.0|

## Dataset do SpaCy utilizado para stemização

|Nome|Versão|
|----|------|
|pt_core_news_lg|3.8.0|



## Pré-requisitos do Servidor Virtual Privado (VPS)


* 2 vCPU;
* 8 GB RAM;
* 100 GB Armazenamento;
* Sistema Operacional: Ubuntu 24.04 LTS;


### Iniciar o projeto

```

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

fastapi dev app.py

```

### Formatar o projeto de acordo com a PEP8

``` 

source .venv/bin/activate

black .
    
flake8 .
```

### /upload/invoice


```

{
    "Invoice": {
        "total": "R$ 415,00",
        "spents": [
            {
                "date": "05/09",
                "description": "NITROXX GAMES GOIANIA",
                "value": "R$ 22,50"
            },
            {
                "date": "01/09",
                "description": "DL GOOGLE CLOUD 6BPKv Sao Pablo",
                "value": "R$ 30,74"
            },
            {
                "date": "02/09",
                "description": "CURITIBA",
                "value": "R$ 12,90"
            },
            {
                "date": "06/09",
                "description": "DM gotindercomhelp Sao Paulo",
                "value": "R$ 35,99"
            },
            {
                "date": "08/09",
                "description": "SPARKS COMMUNICATIONS PETAH TIQWA IL",
                "value": "R$ 20,77"
            },
            {
                "date": "29/09",
                "description": "RESPONDE AI RIO DE JANEIR",
                "value": "R$ 47,50"
            },
            {
                "date": "08/09",
                "description": "DL*GOOGLE 2nd Li SAO PAULO",
                "value": "R$ 89,99"
            },
            {
                "date": "15/09",
                "description": "PPRO MICROSOFT SAO PAULO",
                "value": "R$ 25,00"
            },
            {
                "date": "19/09",
                "description": "DL*GOOGLE ChatGP SAO PAULO",
                "value": "R$ 95,99"
            },
            {
                "date": "29/09",
                "description": "PROTECAO OURO",
                "value": "R$ 3,00"
            },
            {
                "date": "01/09",
                "description": "KIWIFY Betos PARC",
                "value": "R$ 29,90"
            }
        ],
        "tax": "R$ 0,72"
    }
}

```

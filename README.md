# Financy.AI

Financy.AI is a software was a service(SAAS), your general porpouse is management the user's personal expenses.


## Diferencial between Financy.AI and other Financial's Management Software 


* Integration with WhatsApp;
* Essential tools for user managent your financial expenses;
* Using AI for scanner all financial expenses in .pdf format;

## Financy.AI functionalities 

![This is a functionality diagram about Financy.AI](/imgs/diagramFunctionalites.svg)


## Technologies using for development Financy.AI

|Name|Version|
|----|-------|
|Python|3.12.3|
|Pip     |24.0|
|Google Gemini Flash|gemini-2.5-flash-lite|
|PostgreSQL| |
|Docker| |
|WhatsApp Official API| |

## Python's libraries using for development Financy.AI

|Name|Version|
|----|-------|
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

## Spacy's data set using for stemming

|Name|Version|
|----|-------|
|pt_core_news_lg|3.8.0|



## Virtual Private Server pre-requisites


* 2 vCPU;
* 8 GB RAM;
* 100 GB Storage;
* System Operational : Ubuntu 24.04 LTS;


### Start project

```

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

fastapi dev app.py

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
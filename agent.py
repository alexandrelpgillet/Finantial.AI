import os
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from typing import List

class Spent(BaseModel):
    
    date:str = Field(description="Data")
    description:str = Field(description="Descrição")    
    value:str = Field(description="Valor gasto com o símbolo da moeda, ex: R$ 10,00")
    category:str = Field(description="Categoria do gasto a partir da descrição do gasto, podendo ser Alimentação ou Supermercado ou Lazer ou Transporte ou Despesas ou Outros")

class Invoice(BaseModel):
    
    total: str = Field(description="Valor total gasto com símbolo de moeda, ex : R$ 99,00")
    spents: List[Spent] = Field(description="Lista de gastos")
    tax: str = Field(description="Valor total de gasto envolvendo impostos e taxas bancárias, como IOF e juros e gastos com descrição IOF e Juros, com símbolo de moeda, ex : R$ 83,00  ")
def getInvoice(content :str):
    
    
    load_dotenv()
    
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    
    parser = PydanticOutputParser(pydantic_object=Invoice)
    
    
    
    prompt = ChatPromptTemplate.from_messages([
        
        ("system"," Você é um assistente financeiro que analisa faturas de cartões de crédio,a  partir do conteúdo da fatura enviado pelo usuário extraia o valor total da fatura  e  faça a descrição de cada gasto.\n{format_instruction}"),
        ("user","Aqui está o conteúdo da fatura:\n\n {content}")
    ])
    
    chain = prompt | model
    
    response = chain.invoke({"content":content,"format_instruction":parser.get_format_instructions()})
    
    
    tokens_entrada = response.usage_metadata.get("input_tokens")
    tokens_saida = response.usage_metadata.get("output_tokens")
    total = response.usage_metadata.get("total_tokens")
    
    
    ##Salvar no banco de dados de histórico com metricas
    print(f"Custo de Entrada: {tokens_entrada} tokens")
    print(f"Custo de Saída: {tokens_saida} tokens")
    print(f"Total: {total} tokens")    
    
    
    try:
        
        objInvoice = parser.parse(response.content)
    
    except Exception as e:
        
        print(f"ERROR Parser objInvoice = {e}")    
    
    return objInvoice
    
    
    
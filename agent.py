import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

def getInvoice(content :str):
    
    
    load_dotenv()
    
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    
    prompt = ChatPromptTemplate.from_messages([
        
        ("system"," Você é um assistente financeiro que analisa faturas de cartões de crédio,a  partir do conteúdo da fatura enviado pelo usuário extraia o valor total da fatura  e  faça uma tabela com a descrição de cada gasto no seguinte formato =  Data, Descrição , Valor."),
        ("user","Aqui está o conteúdo da fatura:\n\n {content}")
    ])
    
    chain = prompt | model
    
    response = chain.invoke({"content":content})
    
    return response
    
    
    
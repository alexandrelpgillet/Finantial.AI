
from fastapi import FastAPI, File, UploadFile
from typing import Union
from api.pdfRead import pdf_Process
from api.nlpFilter import filterText
from api.agent import getInvoice


app = FastAPI()

@app.get("/status")
def read_root():
    return {"Status": "Online"}


@app.post("/upload/invoice")
async def receiveUploadFile(invoice:UploadFile):
    
   
   content = await invoice.read() 
   
   
   text = pdf_Process(content)
   
   text = filterText(text)
   
   response = getInvoice(text)
   

   return {"Invoice":response}
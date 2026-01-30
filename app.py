
from fastapi import FastAPI, File, UploadFile
from typing import Union
from pdfRead import pdf_Process
from nlpFilter import filterText
from agent import getInvoice


app = FastAPI()

@app.get("/status")
def read_root():
    return {"Status": "Online"}


@app.post("/upload/")
async def receiveUploadFile(file:UploadFile):
    
   
   content = await file.read() 
   
   
   text = pdf_Process(content)
   
   text = filterText(text)
   
   response = getInvoice(text)
   

   return {"file_content":response}
import pymupdf



def pdf_Process(pdf_content):
   
    
   doc = pymupdf.open(stream=pdf_content, filetype="pdf")


   full_text_list = []
   

   for page in doc:
    
     text = page.get_text()
    
     full_text_list.append(text)
    
    
   final_string = "\n".join(full_text_list)
   
   return final_string
    
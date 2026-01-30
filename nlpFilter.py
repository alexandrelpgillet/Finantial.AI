import spacy


def filterText(text):

   nlp = spacy.load("pt_core_news_sm")

   doc = nlp(text)

   words_fix = [ 
              
              t.text for t in doc
              if t.pos_ in ["PROPN", "NUM", "NOUN", "SYM"] or t.text.lower() == "r$"
              
              ]

   text_filtred = " ".join(words_fix)
   
   return text_filtred












    
    
    
    
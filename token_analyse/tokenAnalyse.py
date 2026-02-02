from transformers import AutoTokenizer
import spacy

with open("invoice_test/example.txt", "r", encoding="utf-8") as archive:
    text = archive.read()


nlp = spacy.load("pt_core_news_lg")


doc = nlp(text)

words_fix = [
    t.text
    for t in doc
    if t.pos_ in ["PROPN", "NUM", "NOUN", "SYM"] or t.text.lower() == "r$"
]


text_filtred = " ".join(words_fix)

print(text_filtred)


tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-2b")


tokensBeforeFilter = tokenizer.encode(text)

tokensAfterFilter = tokenizer.encode(text_filtred)

print(f"Total de tokens antes do filtro = ${len(tokensBeforeFilter)}")
print(f"Total de tokens após filtro = {len(tokensAfterFilter)}")


print(f"Ganhos = {len(tokensBeforeFilter)/len(tokensAfterFilter) * 100 - 100}")


output = open("textFiltred.txt", "w")

output.write(text_filtred)

output.close()


print(text_filtred)

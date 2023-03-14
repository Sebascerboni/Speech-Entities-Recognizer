import torch
import json
#Librerías para usar el modelo 
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("Davlan/bert-base-multilingual-cased-ner-hrl")
model = AutoModelForTokenClassification.from_pretrained("Davlan/bert-base-multilingual-cased-ner-hrl")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)

def modelo(index):
    ner_results = nlp(index)
    contenido = str(ner_results)
    contenido = contenido.replace("'", '"')
    return contenido
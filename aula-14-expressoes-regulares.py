import re
import requests

string_de_teste = requests.get('https://generator.email/')

padrao = re.findall(r'[\w\.-]+@\w+\.\w+[\w\.-]+',string_de_teste.text) # r = RAW string (tira o poder das string especiais como \n
# . ou \w to completed the words
# + repete o último padrão uma ou mais vezes
# * repete por 0 ou infinitas vezes
if(padrao):
    print(padrao)
else:
    print("Padrão não encontrado")
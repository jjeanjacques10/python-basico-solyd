import requests
import json
import time
import datetime

def view_cotacao(cotacao):
    print("### Cotação - ",datetime.datetime.now()," ###")
    if(cotacao != "erro"):
        print("Moeda: "+ cotacao[0]['code'])
        print("Valor: "+ cotacao[0]['high']+'\n')
    else:
        print("Erro ao tentar fazer a cotação, tentando novamente...")

def cotacao():
    try:
        dolar = requests.get('http://economia.awesomeapi.com.br/USD-BRL/1')
        cotacao_dolar = json.loads(dolar.text)
        return cotacao_dolar
    except:
        print("Erro na requisição")
        return "erro"

while True:
    view_cotacao(cotacao())
    time.sleep(2)
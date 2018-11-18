import requests #Beautiful Soup 4 BS4 pip install bs4
import re

cabecalho = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36', 'Referer' : 'https://google.com'}
texto = None

try:
    requisicao = requests.get('https://putsreq.com/0WCM4v5V4Eadkwd4BvRZ', headers = cabecalho)
    texto = requisicao.text
    if re.search('Why do I have to complete a CAPTC.',texto, re.IGNORECASE):
        texto = "Google não deixou ;-;"
except Exception as e:
    print('Requisição deu erro', e)

print(texto)

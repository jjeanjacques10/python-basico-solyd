import requests
import json

sair = False
cabecalho = {
'Cookie':'__cfduid=db01d17c3350abbd85587427e79928aa51541942144; _ga=GA1.2.1173770263.1541942150; _gid=GA1.2.1806403208.1542313065; cf_clearance=1712f95155f77ccde1f265acf1b5c36a0e06597d-1542315653-1800-250',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
'Referer' : 'https://google.com'}

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=3766fb5c&t='+titulo, headers=cabecalho)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexao')
        return None

def printar_detalhes(filme):
    print('Título:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])

while not sair:
    op = input('Escreva o nome do filme ou SAIR para fechar: ')
    if op == 'SAIR':
        sair = True
    else:
        filme = requisicao(op)
        if filme == None:
            print("não foi dessa vez")
        else:
            printar_detalhes(filme)
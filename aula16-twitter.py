import oauth2
import json
import urllib.parse

consumer_key = '' #inserir a sua consumer key
consumer_secret = '' #inserir a sua consumer secret

token_key = '' #inserir o seu token key
token_secret = '' #inserir o seu token secret

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key,token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Pesquisa: ")
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt') #Inserir o link da API

decodificar = requisicao[1].decode() #transformar byte em string

objeto = json.loads(decodificar)
twittes = objeto['statuses']

for twit in twittes:
    print(twit['user']['screen_name'])
    print(twit['text'])
    print()

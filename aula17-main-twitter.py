from twitter import Twitter

consumer_key = '' #inserir a sua consumer key
consumer_secret = '' #inserir a sua consumer secret

token_key = '' #inserir o seu token key
token_secret = '' #inserir o seu token secret

#cria o objeto para utilizarmos
twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)

print(twitter)

#testando para fazer um tweet
resp = twitter.tweet('Vamos testar nossa lib')

print(resp)

#testando para fazer uma pesquisa
pesquisa = twitter.search('Quero ganhar pessoal, da uma forcinha o/ ','pt')

for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])
    print()
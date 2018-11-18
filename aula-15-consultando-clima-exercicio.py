import requests
import json

def  view_weather(json_weather):
    print('Temperature: ' + json_weather["query"]["results"]["channel"]["item"]["condition"]["temp"] + 'ºF')
    print('Text: ' + json_weather["query"]["results"]["channel"]["item"]["condition"]["text"])
    print('City: '+json_weather["query"]["results"]["channel"]["location"]["city"])
    print('Country: ' + json_weather["query"]["results"]["channel"]["location"]["country"]+'\n')

def my_request(location):
    try:
        weather = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22'+location+'%2C%20ak%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
        json_weather = json.loads(weather.text)
        return json_weather
    except:
        print("Não foi possível fazer a requisição")

op = " "
while(op != "SAIR"):
    op = input('Insira o local que deseja saber o clima ou SAIR: ')
    if(op != "SAIR"):
        view_weather(my_request(op))
    else:
        print("Saindo...")
        exit()
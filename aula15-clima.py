import requests
import json
import  locale

cidade = input("Escreva sua cidade: ")
api = '93c976c71d3d0d1fba3fec9cf77a97ba'

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid='+api)

tempo = json.loads(requisicao.text)

print('Tempo: '+ tempo['weather'][0]['main'])
print('Temperatura: ', locale.format_string("%1.0f",float(tempo['main']['temp']-273.15)))

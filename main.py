# o link da API é chamado de endpoint
# endpoint é o link para os métodos get e post
# ex.: https://api.open-meteo.com/v1/forecast

# sempre que utilizo API em Python, devo chamar a biblioteca de requisições
# pip install requests

# sempre que queremos utilizar gráficos, podemos utilizar a biblioteca matplotlib
# pip install matplotlib

import requests 
import matplotlib.pyplot as plt

# criar uma função chamada de buscar_clima
def buscar_clima(latitude, longitude):
    # deve informar o endpoint
    endpoint = 'https://api.open-meteo.com/v1/forecast'
    # informar os parámetros para o sistema em formato de dicionário 
    # o dicionário trabalha com chave:valor
    parametros = { 
        # "chave":valor,
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "timezone": "America/Sao_Paulo"
    }
    resposta = requests.get(endpoint, params=parametros)
    # sempre que queremos obter a resposta, usamos o comando requests.get para coletar os valores e inserimos os atributos
    # requests.get(variavel_do_endpoint, params=dicionário_com_parametros)
    # para o sistema usar o método post - para mostrar as informações
    dados = resposta.json()
    # o sistema transforma os dados em json para poder manipulá-los
    return dados

latitude = float(input("Informe a latitude:"))
longitude = float(input("Informe a longitude:"))

# Exibindo informações para os usuários
dados = buscar_clima(latitude, longitude)

horas = dados['hourly']['time']
# chamo a base de dados, informo o parâmetro e informo qual a variável o parâmetro vai ler
temperatura = dados['hourly']['temperature_2m']

plt.plot(horas, temperatura)
# plt.plot cria um gráfico, no qual crio um parâmetro onde informo como parâmetro primeiro o eixo x e depois o eixo y
# plt.plot(eixo_x, eixo_y)
plt.title('TEMPERATURA POR HORA')
# para ver o gráfico
plt.show()
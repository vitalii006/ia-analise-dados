import requests

cep = input("digite seu cep: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)
resposta = dados.json()

print(f"voce mora na rua: {resposta["logradouro"]}. no bairro: {resposta["bairro"]}. na cidade de {resposta["localidade"]}")
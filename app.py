import requests
import json

# Faça uma solicitação HTTP para obter o JSON
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}

    for item in dados_json:
        nome_restaurante = item["Company"]
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append({
            "Item": item["Item"],
            "Price": item["price"],
            "Description": item["description"]
        })

    print(dados_restaurante)

    for nome_restaurante, dados in dados_restaurante.items():
        nome_arquivo = f"{nome_restaurante}.json"
        with open(nome_arquivo, 'w') as arquivo_restaurante:
            json.dump(dados, arquivo_restaurante, indent=4)

else:
    print(f"Erro: Código de status {response.status_code}")


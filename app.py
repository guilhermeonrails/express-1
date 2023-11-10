from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/ola')
def diga_ola():
    return {'Olá': 'Mundo'}

@app.get('/api/restaurantes/')
def get_restaurante(restaurante: str = Query(None)):
    # Fazer uma solicitação HTTP para obter o JSON
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()

        if restaurante is None:
            return {'dados': dados_json}

        itens = []
        for item in dados_json:
            if item['Company'] == restaurante:
                itens.append({
                    "Item": item["Item"],
                    "Price": item["price"],
                    "Description": item["description"]
                })

        return {'Restaurante': restaurante, 'itens': itens}

    else:
        return {'error': f"'{response.status_code} - {response.text}"}



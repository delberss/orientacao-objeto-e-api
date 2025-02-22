import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}  # Dicionário vazio para armazenar os restaurantes
    
    for item in dados_json:
        # Removendo espaços extras nas chaves
        nome_do_restaurante = item['Company'].strip()  
        
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'].strip(),  # Removendo espaços extras
            "price": item['price'],
            "description": item['description'].strip()
        })
    
    print(dados_restaurante['McDonald’s'])  # Exibir o dicionário formatado
else:
    print(f'Erro ao acessar API. Código: {response.status_code}')

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
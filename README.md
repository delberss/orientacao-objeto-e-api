# Gerenciamento de Restaurantes com Python e FastAPI

Este projeto demonstra a aplicação de conceitos de Programação Orientada a Objetos (POO) em Python, além da utilização da biblioteca FastAPI para criar uma API REST. O projeto também consome uma API externa para obter dados de cardápios de restaurantes.

## 📌 Funcionalidades
- Criação de um sistema de restaurante utilizando POO.
- Definição de classes para modelar restaurantes, bebidas e pratos.
- Implementação de uma API REST com FastAPI.
- Consumo de uma API externa para obtenção de dados de restaurantes.
- Exportação dos dados para arquivos JSON.

## 🛠 Tecnologias Utilizadas
- **Python 3.x**
- **FastAPI**
- **Requests**
- **JSON**
- **Virtual Environment (venv)**

## 📁 Estrutura do Projeto
```
📂 projeto_restaurante
├── 📂 modelos
│   ├── 📂 cardapio
│   │   ├── bebida.py
│   │   ├── prato.py
|   |   ├── item_cardapio.py
│   ├── restaurante.py
│   ├── avaliacao.py
├── app.py
├── main_fastapi.py
├── main.py
├── requirements.txt
└── README.md
```

## 🚀 Como Executar o Projeto

### 1️⃣ Criar e ativar o ambiente virtual
```sh
python -m venv venv
```
Para ativar o ambiente virtual:
- No **Windows**:
  ```sh
  venv\Scripts\activate
  ```
- No **Linux/macOS**:
  ```sh
  source venv/bin/activate
  ```

### 2️⃣ Instalar as dependências
```sh
pip install -r requirements.txt
```

### 3️⃣ Executar o código principal
Para rodar o script que consome a API externa e gera arquivos JSON:
```sh
python main.py
```

### 4️⃣ Executar a API com FastAPI
Para iniciar o servidor FastAPI, execute:
```sh
uvicorn main_fastapi:app --reload
```
Acesse a API no navegador ou via Postman em:
- **Documentação Interativa:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Endpoint de teste:** [http://127.0.0.1:8000/api/hello](http://127.0.0.1:8000/api/hello)

### 5️⃣ Desativar o ambiente virtual (quando terminar)
```sh
deactivate
```

## 📌 Endpoints Disponíveis

### `GET /api/hello`
Retorna uma mensagem simples de "Hello, World!".

### `GET /api/restaurantes/?restaurante={nome}`
Retorna o cardápio de um restaurante específico com base nos dados da API externa.

## 📝 Aprendizados
Este projeto foi desenvolvido como parte do curso **Python: Avance na Orientação a Objetos e Consuma APIs**. Durante o desenvolvimento, foram aplicados conceitos de:
- **Encapsulamento, herança e polimorfismo** em POO.
- **Manipulação de JSON** para leitura e escrita de dados.
- **Consumo de APIs** usando a biblioteca `requests`.
- **Criação de APIs REST** utilizando `FastAPI`.

---
🚀 Desenvolvido com Python 🐍 e FastAPI ⚡


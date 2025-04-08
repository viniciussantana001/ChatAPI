# Importa a classe FastAPI para criar a API
from fastapi import FastAPI

# Importa a classe JsonDB, responsável por manipular o banco de dados em JSON
from json_db import JsonDB

# Importa a classe Message, que representa a estrutura de uma mensagem
from message import Message

# Importa o middleware de CORS para permitir requisições de origens diferentes
from fastapi.middleware.cors import CORSMiddleware

# Inicializa a aplicação FastAPI
app = FastAPI()

# Configura o middleware de CORS para permitir acessos de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite acesso de qualquer domínio
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

# Instancia um banco de dados JSON para armazenar mensagens, usando o arquivo especificado
messageDB = JsonDB(path='./data/messages.json')

# Rota para obter todas as mensagens salvas
@app.get('/messages')
def get_messages():
    messages = messageDB.read()  # Lê as mensagens do banco de dados JSON
    return {"messages": messages}  # Retorna as mensagens no formato JSON

# Rota para enviar uma nova mensagem
@app.post('/messages')
def send_messages(message: Message):
    messageDB.insert(message)  # Insere a nova mensagem no banco de dados JSON
    return {"status": "inserted"}  # Retorna uma resposta confirmando a inserção
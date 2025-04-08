```md
# ChatAPI  

ChatAPI é uma API simples para troca de mensagens em tempo real, desenvolvida com FastAPI e utilizando JSON como banco de dados. Com suporte a CORS, pode ser integrada a aplicações web e móveis.  

## Requisitos  

- Python 3.8+  
- FastAPI e Uvicorn  (os dois ja estao na mesma instalacao)

Instale as dependências com:  
```sh
pip install "fastapi[standard]"
```

## Como Usar  

### Criar e ativar um ambiente virtual (opcional)  
```sh
python -m venv venv  
venv\Scripts\activate  # Windows  
source venv/bin/activate  # macOS/Linux  
```

### Instalar os requisitos  
```sh
pip install -r requirements.txt
```

### Iniciar o servidor  
``` 
fastapi dev main.py
```

O servidor será iniciado em `http://127.0.0.1:8000`.  

## Rotas  

### Obter todas as mensagens  
**GET** `/messages`  
Retorna todas as mensagens armazenadas.  

### Enviar uma nova mensagem  
**POST** `/messages`  

Corpo da requisição (JSON):  
```json
{
  "name": "Alice",
  "message": "Olá, pessoal!"
}
```

Resposta:  
```json
{
  "status": "inserted"
}
```

## Estrutura do Projeto  

```
ChatAPI/
│── data/
│   ├── messages.json
│── venv/
│── json_db.py
│── main.py
│── message.py
│── requirements.txt
```
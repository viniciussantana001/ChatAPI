from pydantic import BaseModel # importar a base model

class Message(BaseModel): # criar a classe para guardar o nome e a mensagem
    name: str
    message: str
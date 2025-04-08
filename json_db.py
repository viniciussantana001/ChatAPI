import json # importar json
from pydantic import BaseModel

from message import Message # importar a classe Message do message.py

class JsonDB(BaseModel): # criar classe para ler e escrever dados no json(banco de dados improvisado)
    path: str #caminho do json

    def read(self): # funcao para ler o json
        f = open(self.path) # abrir o local do json
        data = json.loads(f.read()) # ler o conteudo do json
        f.close() # fechar caminho
        return data # retornar o que foi escrito no json
    
    def insert(self, message: Message): # funcao para inserir dados
        data = self.read() # le a funcao e retorna para a variavel data
        data['send_messages'].append(message.dict()) #faz com que o dict que tem no messages.json, adicione as duas variaveis da classe Message
        f = open(self.path, 'w') # abri o json e entra no modo escrever
        f.write(json.dumps(data)) # escreve o dict data no json
        f.close() # fecha caminho
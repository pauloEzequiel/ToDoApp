from unicodedata import category
from pydantic import BaseModel,Field
from typing import Optional, List
import datetime
import uuid


class TarefaSchema(BaseModel):
     tarefa_id:str = str(uuid.uuid4())
     descricao:str = "comprar pão"
     concluido:bool = False
     criado_em:str = datetime.datetime.now().strftime("%c") 
     atualizado_em:str = datetime.datetime.now().strftime("%c")

class TarefaBody(BaseModel):
    descricao:str = Field(None,min_lenght=2, description ="Descrição da tarefa")
    concluido:int = Field(0, description ="status de conclusao")


class obterTarefaSchema(BaseModel):
    tarefa_id: str = str(uuid.uuid4())
  

class tarefaViewSchema(BaseModel):
     tarefa_id:str = str(uuid.uuid4())
     descricao:str = "comprar pão"
     concluido:bool = False
     criado_em:str = datetime.datetime.now().strftime("%c") 
     atualizado_em:str = datetime.datetime.now().strftime("%c") 

     

class ListaTarefaViewSchema(BaseModel):
    tarefa: List[TarefaSchema]

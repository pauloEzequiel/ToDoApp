import datetime
from infra.configs.base import Base
from sqlalchemy import Column, String,Boolean, DateTime
import uuid

class Tarefas(Base):
   __tablename__= 'tarefas'

   tarefa_id = Column(String(36), primary_key = True, default = str(uuid.uuid4()))
   descricao = Column(String(300))
   concluido = Column(Boolean)
   criado_em = Column(DateTime,default=datetime.datetime.utcnow)
   atualizado_em = Column(DateTime,default=datetime.datetime.utcnow)


   def __init__(self,tarefa_id,descricao,concluido,criado_em,atualizado_em):
       self.tarefa_id = tarefa_id
       self.descricao = descricao
       self.concluido = concluido
       self.criado_em = criado_em
       self.atualizado_em = atualizado_em
    
   def json(self):
       return{
           'tarefa_id' : self.tarefa_id,  
           'descricao' : self.descricao,
           'concluido' : self.concluido,
           'criado_em' : self.criado_em.strftime("%c"), 
           'atualizado_em' : self.atualizado_em.strftime("%c") 
       }
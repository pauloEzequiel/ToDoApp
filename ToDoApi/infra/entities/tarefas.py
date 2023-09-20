import datetime
from infra.configs.base import Base
from sqlalchemy import Column, String,Boolean, DateTime, Integer,ForeignKey,Table
from sqlalchemy.orm import relationship
import uuid

class Tarefas(Base):
   __tablename__= 'tarefas'

   tarefa_id = Column(String(36), primary_key = True, default = str(uuid.uuid4()))
   descricao = Column(String(300))
   concluido = Column(Boolean)
   criado_em = Column(DateTime,default=datetime.datetime.utcnow)
   atualizado_em = Column(DateTime,default=datetime.datetime.utcnow)
   marcadores = relationship('Marcadores',secondary=lambda:Tarefas_Marcadores.__table__, back_populates="tarefas",lazy="subquery")


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
   

class Marcadores(Base):
    __tablename__= 'marcadores'

    marcador_id =  Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(50))
    tarefas = relationship('Tarefas',secondary=lambda:Tarefas_Marcadores.__table__, back_populates="marcadores",lazy="subquery")

    def __init__(self, descricao) :
        self.descricao = descricao

    def json(self):
        return{
            'marcador_id': self.marcador_id,
            'descricao_id': self.descricao
        }

class Tarefas_Marcadores(Base):
        __table__ = Table(
            'tarefas_marcadores', 
            Base.metadata,
            Column('tarefa_marcador_id',Integer, primary_key=True, autoincrement=True),
            Column('tarefa_id',String(36), ForeignKey('tarefas.tarefa_id', name ='fk_tarefas',onupdate="CASCADE", ondelete= "CASCADE")),
            Column('marcador_id',Integer, ForeignKey ('marcadores.marcador_id', name ='fk_marcadores', onupdate="CASCADE", ondelete= "CASCADE")),
            Column('criado_em',DateTime,default=datetime.datetime.utcnow))

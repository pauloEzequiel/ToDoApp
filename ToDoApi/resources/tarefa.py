from flask_restful import Resource, reqparse
from models.tarefa import TarefaModel
from sqlalchemy.exc import IntegrityError
from resources.logger import logger
from models import Session
import datetime
import uuid


class UpdateTarefa(Resource):

    def put(self,tarefa_id):
         
          tarefa = Tarefa.encontrar_tarefa(tarefa_id)
          if(tarefa == None) :
            return {'message': 'tarefa não localizada'},404
          
          session = Session()
          session.query(TarefaModel).filter(TarefaModel.tarefa_id == tarefa_id).update({TarefaModel.concluido : not tarefa.concluido, TarefaModel.atualizado_em: datetime.datetime.now()})
          session.commit()
          tarefa.concluido = not tarefa.concluido
          tarefa.atualizado_em = datetime.datetime.now()
        
          return tarefa.json(),200

      
class Tarefas(Resource):
    
    def get(self):
        session = Session()
        try:
           return{'Tarefa':[ tarefa.json() for tarefa in session.query(TarefaModel).all()]}
        except Exception as e:
           logger.warning(f"Não foi possivel recuperar dados")
           return {"Tarefa": [] }, 400

    
    def post(self):
        """Adiciona um novo tarefas à base
        """
        session = Session()
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('descricao')
        argumentos.add_argument('concluido')

        dados = argumentos.parse_args()

        try:
           tarefa_model = TarefaModel(str(uuid.uuid4()),dados['descricao'],bool(int(dados['concluido'])),datetime.datetime.now(),datetime.datetime.now())
           session.add(tarefa_model)
           session.commit()
           logger.debug(f"Adicionado tarefa: '{dados['descricao']}'")
           return tarefa_model.json(),201
        except IntegrityError as e:
           error_msg = "Produto de mesmo nome já salvo na base :/"
           logger.warning(f"Erro ao adicionar tarefa '{dados['descricao']}', {error_msg}")
           return {"mesage": error_msg}, 400
        except Exception as e:
           error_msg = "Não foi possível salvar novo item :/"
           logger.warning(f"Erro ao adicionar tarefa '{dados['descricao']}', {error_msg}")
           return {"mesage": error_msg}, 400

         
class Tarefa(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('descricao')
    argumentos.add_argument('concluido') 

    def encontrar_tarefa(tarefa_id):
        session = Session()
        tarefa = session.query(TarefaModel).filter(TarefaModel.tarefa_id == tarefa_id).first()
        if not tarefa :
            return None
            
        return tarefa
     
    def get(self,tarefa_id):
        """Consulta tarefa
        """
        tarefa = Tarefa.encontrar_tarefa(tarefa_id)
        if(tarefa) :
            return tarefa.json()
            
        return {'message': 'tarefa não localizada'},404


    def put(self,tarefa_id):
       """Atualiza tarefa ou caso não exista na base atualiza
        """
       dados = Tarefa.argumentos.parse_args()
       tarefa = Tarefa.encontrar_tarefa(tarefa_id)
       print(tarefa)
       if(tarefa):
           session = Session()
           session.query(TarefaModel).filter(TarefaModel.tarefa_id == tarefa_id).update({ TarefaModel.descricao : dados['descricao'],TarefaModel.concluido : bool(int(dados['concluido'])), TarefaModel.atualizado_em: datetime.datetime.now()})
           session.commit()
           tarefa.descricao = dados['descricao']
           tarefa.concluido = bool(int(dados['concluido']))
           tarefa.atualizado_em = datetime.datetime.now()
           
           return tarefa.json(),200
       
       session = Session() 
       nova_tarefa = TarefaModel(tarefa_id,dados['descricao'],bool(int(dados['concluido'])),datetime.datetime.now(),datetime.datetime.now())
       session.add(nova_tarefa)
       session.commit()

       return nova_tarefa.json(),201
        

    def delete(self,tarefa_id):
        """Excluir tarefa
        """
        session = Session()
        linhas_afetadas = session.query(TarefaModel).filter(TarefaModel.tarefa_id == tarefa_id).delete()
        session.commit()
        if linhas_afetadas:
         return {'message': 'tarefa deletada'}, 200
            
        return {'message': 'tarefa não localizada'},404
    
    
    
    

    

      

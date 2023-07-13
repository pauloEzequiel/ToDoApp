from models.tarefa import TarefaModel
from sqlalchemy.exc import IntegrityError
from resources.logger import logger
from models import Session
import datetime
import uuid



class TarefaManager:
    def adicionarTask(tarefa):
        session = Session()
    
        try:
           tarefa_model = TarefaModel(str(uuid.uuid4()),tarefa.descricao,bool(tarefa.concluido),datetime.datetime.now(),datetime.datetime.now())
           session.add(tarefa_model)
           session.commit()
           logger.debug(f"Adicionado tarefa: '{tarefa.descricao}'")
           return tarefa_model.json(),201
        except IntegrityError as e:
           error_msg = "Produto de mesmo nome já salvo na base :/"
           logger.warning(f"Erro ao adicionar tarefa '{tarefa.descricao}', {error_msg}")
           return {"message": error_msg}, 400
        except Exception as e:
           error_msg = "Não foi possível salvar novo item :/"
           logger.warning(f"Erro ao adicionar tarefa '{tarefa.descricao}', {error_msg}")
           return {"message": error_msg}, 400
        
    def encontrar_tarefa(tarefa_id):
        session = Session()
        tarefa = session.query(TarefaModel).filter(TarefaModel.tarefa_id == tarefa_id).first()
        if not tarefa :
            return None
            
        return tarefa    
        
    def buscarTarefa(tarefa_id):
        tarefa = TarefaManager.encontrar_tarefa(tarefa_id)
        if(tarefa) :
            return tarefa.json()
            
        return {'message': 'tarefa não localizada'},404
    
    def obterTodasTarefas():
        session = Session()
        try:
           return{'Tarefa':[ tarefa.json() for tarefa in session.query(TarefaModel).all()]}
        except Exception as e:
           logger.warning(f"Não foi possivel recuperar dados")
           return {"Tarefa": [] }, 400
        
    def alterarStatusTarefa(tarefa_id):
        tarefa = TarefaManager.encontrar_tarefa(tarefa_id)

        if(tarefa == None) :
            return {'message': 'tarefa não localizada'},404
          
        session = Session()
        session.query(TarefaModel).filter(TarefaModel.tarefa_id == tarefa_id).update({TarefaModel.concluido : not tarefa.concluido, TarefaModel.atualizado_em: datetime.datetime.now()})
        session.commit()
        tarefa.concluido = not tarefa.concluido
        tarefa.atualizado_em = datetime.datetime.now()
        
        return tarefa.json(),200
    
    def atualizarTarefa(tarefa_id,tarefaAtualizada):
       tarefa = TarefaManager.encontrar_tarefa(tarefa_id)
       if(tarefa):
           session = Session()
           session.query(TarefaModel).filter(TarefaModel.tarefa_id == tarefa_id).update({ TarefaModel.descricao : tarefaAtualizada.descricao,TarefaModel.concluido : bool(int(tarefaAtualizada.concluido)), TarefaModel.atualizado_em: datetime.datetime.now()})
           session.commit()
           tarefa.descricao = tarefaAtualizada.descricao
           tarefa.concluido = bool(int(tarefaAtualizada.concluido))
           tarefa.atualizado_em = datetime.datetime.now()
           
           return tarefa.json(),200
       
       session = Session() 
       nova_tarefa = TarefaModel(tarefa_id,tarefaAtualizada.descricao,bool(int(tarefaAtualizada.concluido)),datetime.datetime.now(),datetime.datetime.now())
       session.add(nova_tarefa)
       session.commit()

       return nova_tarefa.json(),201
  
    def apagarTarefa(tarefa_id):
        session = Session()
        linhas_afetadas = session.query(TarefaModel).filter(TarefaModel.tarefa_id == tarefa_id).delete()
        session.commit()
        if linhas_afetadas:
         return {'message': 'tarefa deletada'}, 200
            
        return {'message': 'tarefa não localizada'},404
    


         

    
    
    
    

    

      

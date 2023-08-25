from sqlalchemy.exc import IntegrityError
from resources.logger import logger
from infra.repository.tarefas_repository import TarefaRepository
from infra.entities.tarefas import Tarefas
import datetime
import uuid

class TarefaManager:
    def adicionarTask(tarefa):
        
        try:
           repo = TarefaRepository()

           tarefa_model = Tarefas(str(uuid.uuid4()),tarefa.descricao,bool(tarefa.concluido),datetime.datetime.now(),datetime.datetime.now())
           repo.inserirTarefa(tarefa_model.tarefa_id,tarefa_model.descricao,tarefa_model.concluido,tarefa_model.criado_em,tarefa_model.criado_em)
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
        tarefa = TarefaRepository().obterTarefa(tarefa_id)
        if not tarefa :
            return None
            
        return tarefa    
        
    def buscarTarefa(tarefa_id):
        tarefa = TarefaManager.encontrar_tarefa(tarefa_id)
        if(tarefa) :
            return tarefa.json()
            
        return {'message': 'tarefa não localizada'},404
    
    def obterTodasTarefas():
        try:
           repo = TarefaRepository()
           return {'Tarefa':[ tarefa.json() for tarefa in repo.ObterTodas()]},200
          
        except Exception as e:
           logger.warning(f"Não foi possivel recuperar dados")
           return {"Tarefa": [] }, 400
        
    def alterarStatusTarefa(tarefa_id):
        tarefa = TarefaManager.encontrar_tarefa(tarefa_id)

        if(tarefa == None) :
            return {'message': 'tarefa não localizada'},404
          
        TarefaRepository().atualizarTarefa(tarefa_id, tarefa.descricao, not tarefa.concluido, datetime.datetime.now())
        tarefa.concluido = not tarefa.concluido
        tarefa.atualizado_em = datetime.datetime.now()
        
        return tarefa.json(),200
    
    def atualizarTarefa(tarefa_id,tarefaAtualizada):
       tarefa = TarefaManager.encontrar_tarefa(tarefa_id)
       repo = TarefaRepository()
       if(tarefa):
           repo.atualizarTarefa(tarefa_id, tarefaAtualizada.descricao, bool(int(tarefaAtualizada.concluido)),datetime.datetime.now())
           tarefa.descricao = tarefaAtualizada.descricao
           tarefa.concluido = bool(int(tarefaAtualizada.concluido))
           tarefa.atualizado_em = datetime.datetime.now()
           
           return tarefa.json(),200
       
       nova_tarefa = Tarefas(tarefa_id,tarefaAtualizada.descricao,bool(int(tarefaAtualizada.concluido)),datetime.datetime.now(),datetime.datetime.now())
       repo.inserirTarefa(nova_tarefa.tarefa_id, nova_tarefa.descricao, nova_tarefa.concluido, nova_tarefa.criado_em, nova_tarefa.criado_em)

       return nova_tarefa.json(),201
  
    def apagarTarefa(tarefa_id):
        linhas_afetadas = TarefaRepository().apagarTarefa(tarefa_id)
        if linhas_afetadas:
          return {'message': 'tarefa deletada'}, 200
            
        return {'message': 'tarefa não localizada'},404
    


         

    
    
    
    

    

      

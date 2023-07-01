from flask_restful import Resource, reqparse
from models.tarefa import TarefaModel
import datetime
import uuid

lista_tarefas = [
     {
        'tarefa_id':'11d4dc2e-375a-4b89-9ad4-aa30105385aa',
        'descricao':'Codificar versão inicial da api python',
        'concluido': True,
        'criado_em': datetime.datetime.now().strftime("%c"),
        'atualizado_em': datetime.datetime.now().strftime("%c"),
     },
     {
        'tarefa_id':'78d4dc2e-789a-4b89-9ad4-aa30105385bb',
        'descricao':'Commit da versão inicial da api',
        'concluido': False,
        'criado_em': datetime.datetime.now().strftime("%c"),
        'atualizado_em': datetime.datetime.now().strftime("%c"),
     },
     {
        'tarefa_id':'56d4dc2e-741a-4b1389-9ad4-aa30105385cc',
        'descricao':'Entregar projeto no dia 22/06/2023',
        'concluido': False,
        'criado_em': datetime.datetime.now().strftime("%c"),
        'atualizado_em': datetime.datetime.now().strftime("%c"),
     }
]

class UpdateTarefa(Resource):

    def put(self,tarefa_id):
         
          tarefa = Tarefa.encontrar_tarefa(tarefa_id)
          if(tarefa == None) :
            return {'message': 'tarefa não localizada'},404
        
          tarefa_model = TarefaModel(tarefa_id, tarefa['descricao'], not bool(int(tarefa['concluido'])),tarefa['criado_em'],datetime.datetime.now().strftime("%c"))
          tarefa_atualizada = tarefa_model.json()
          tarefa.update(tarefa_atualizada)
          return tarefa_atualizada,200


      
class Tarefas(Resource):
    
    def get(self):
        return{'Tarefa': lista_tarefas}
    
    def post(self):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('descricao')
        argumentos.add_argument('concluido')

        dados = argumentos.parse_args()
        tarefa_model = TarefaModel(str(uuid.uuid4()),dados['descricao'],bool(int(dados['concluido'])),datetime.datetime.now().strftime("%c"),datetime.datetime.now().strftime("%c"))
        nova_tarefa = tarefa_model.json()
        lista_tarefas.append(nova_tarefa)
        return nova_tarefa,201
    

class Tarefa(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('descricao')
    argumentos.add_argument('concluido') 

    def encontrar_tarefa(tarefa_id):
        for tarefa in lista_tarefas:
            if tarefa['tarefa_id'] == tarefa_id:
                return tarefa
            
        return None
     
    def get(self,tarefa_id):
        tarefa = Tarefa.encontrar_tarefa(tarefa_id)
        if(tarefa) :
            return tarefa
            
        return {'message': 'tarefa não localizada'},404

    

    def put(self,tarefa_id):
       dados = Tarefa.argumentos.parse_args()
       tarefa = Tarefa.encontrar_tarefa(tarefa_id)
       if(tarefa) :
           tarefa_model = TarefaModel(tarefa_id, dados['descricao'],bool(int(dados['concluido'])),tarefa['criado_em'],datetime.datetime.now().strftime("%c"))
           tarefa_atualizada = tarefa_model.json()
           tarefa.update(tarefa_atualizada)
           return tarefa_atualizada,200
       tarefa_model = TarefaModel(tarefa_id,dados['descricao'],bool(int(dados['concluido'])),datetime.datetime.now().strftime("%c"),datetime.datetime.now().strftime("%c"))
       nova_tarefa = tarefa_model.json()
       lista_tarefas.append(nova_tarefa)
       return nova_tarefa,201
        

    def delete(self,tarefa_id):
       global lista_tarefas
       tarefa = Tarefa.encontrar_tarefa(tarefa_id)
       if(tarefa) :
            lista_tarefas = [tarefa for tarefa in lista_tarefas if tarefa['tarefa_id'] != tarefa_id]
            return {'message': 'tarefa deletada'}, 200
            
       return {'message': 'tarefa não localizada'},404
    
    
    
    

    

      

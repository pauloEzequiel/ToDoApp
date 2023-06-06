from flask_restful import Resource
import datetime

lista_tarefas =[
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

class Tarefas(Resource):
    def get(self):
        return{'Tarefa': lista_tarefas}
    

class Tarefa(Resource):
    def get(self,tarefa_id):
        for tarefa in lista_tarefas:
            if tarefa['tarefa_id'] == tarefa_id:
                return tarefa
            
        return {'message': 'tarefa não localizada'},404


    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
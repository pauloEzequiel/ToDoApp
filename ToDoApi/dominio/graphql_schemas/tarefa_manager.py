import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from infra.entities.tarefas import Tarefas as tarefaModel
from infra.repository.tarefas_repository import TarefaRepository
import datetime
import uuid


class Tarefa(SQLAlchemyObjectType):
    class Meta:
        model = tarefaModel

class Query(graphene.ObjectType):
    tarefa = graphene.Field(Tarefa, id=graphene.ID(required=True))
    tarefas = graphene.List(Tarefa)

    def resolve_tarefa(self, info, **kwargs):
        return TarefaRepository().obterTarefa(kwargs.get('id'))

    def resolve_tarefas(self, info):
         repo = TarefaRepository()
         return repo.ObterTodas()
    

class CriarTarefa(graphene.Mutation):
    class Arguments:
        descricao = graphene.String()
        status = graphene.Boolean()


    tarefa = graphene.Field(lambda: Tarefa)

    def mutate(root, info, **kwargs):
        repo = TarefaRepository()
        tarefa_model = tarefaModel(str(uuid.uuid4()),kwargs.get('descricao'),kwargs.get('status'),datetime.datetime.now(),datetime.datetime.now())
        repo.inserirTarefa(tarefa_model.tarefa_id,tarefa_model.descricao,tarefa_model.concluido,tarefa_model.criado_em,tarefa_model.criado_em)
       
        return CriarTarefa(tarefa=tarefa_model)

class ApagarTarefa(graphene.Mutation):
    class Arguments:
        tarefa_id = graphene.String()

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root,info,**kwargs):
         linhas_afetadas = TarefaRepository().apagarTarefa(kwargs.get('tarefa_id'))
         if linhas_afetadas:
            return ApagarTarefa(success = True, message = 'Tarefa Apagada')
            
         return ApagarTarefa(success = False, message = 'Tarefa não localizada')
    
class Mutation(graphene.ObjectType):
    criar_tarefa = CriarTarefa.Field()
    apagar_tarefa = ApagarTarefa.Field()

    
    
schema = graphene.Schema(query=Query, mutation=Mutation, types=[Tarefa])
   

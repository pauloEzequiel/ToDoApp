from infra.configs.connection import DBConnectionHandler
from infra.entities.tarefas import Tarefas
from sqlalchemy.orm.exc import NoResultFound


class TarefaRepository:
    def ObterTodas(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Tarefas).all()
                print(data)
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def obterTarefa(self,tarefa_id):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Tarefas).filter(Tarefas.tarefa_id == tarefa_id).first()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def inserirTarefa(self,tarefa_id,descricao,concluido,criado_em,atualizado_em):
        with DBConnectionHandler() as db:
             try:
                data_insert = Tarefas(tarefa_id=tarefa_id, descricao=descricao, concluido=concluido, criado_em=criado_em,atualizado_em=atualizado_em)
                db.session.add(data_insert)
                db.session.commit()
             except Exception as exception:
                db.session.rollback()
                raise exception
             
    def atualizarTarefa(self,tarefa_id,descricao,concluido,atualizado_em):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Tarefas)\
                    .filter(Tarefas.tarefa_id == tarefa_id)\
                    .update({ Tarefas.descricao : descricao,Tarefas.concluido : concluido , Tarefas.atualizado_em: atualizado_em})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def apagarTarefa(self, tarefa_id):
        with DBConnectionHandler() as db:
            try:
                linhas_afetadas = db.session.query(Tarefas).filter(Tarefas.tarefa_id == tarefa_id).delete()
                db.session.commit()
                return linhas_afetadas
            except Exception as exception:
                db.session.rollback()
                raise exception

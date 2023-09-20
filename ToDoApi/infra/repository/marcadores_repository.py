from infra.configs.connection import DBConnectionHandler
from infra.entities.tarefas import Tarefas, Marcadores, Tarefas_Marcadores
from sqlalchemy.orm.exc import NoResultFound

class MarcadoresRepository:
    def ObterTodosMarcadores(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Marcadores).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def ObterTodosTarefasMarcadores(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Tarefas_Marcadores).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def obterMarcadores(self,tarefa_id):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Tarefas_Marcadores).filter(Tarefas_Marcadores.tarefa_id == tarefa_id).all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def inserirMarcador(self,descricao):
        with DBConnectionHandler() as db:
             try:
                data_insert = Marcadores(descricao=descricao )
                db.session.add(data_insert)
                db.session.commit()
             except Exception as exception:
                db.session.rollback()
                raise exception
             
    def associarTarefaAoMarcador(self,tarefa_id,marcador_id,criado_em):
        with DBConnectionHandler() as db:
             try:
                data_insert = Tarefas_Marcadores(tarefa_id=tarefa_id,marcador_id=marcador_id,criado_em=criado_em,)
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

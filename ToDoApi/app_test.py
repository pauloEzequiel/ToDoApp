from infra.repository.tarefas_repository import TarefaRepository
from infra.repository.marcadores_repository import MarcadoresRepository
import datetime

repo = TarefaRepository()
tarefa = repo.obterTarefa('93105b68-24e4-4483-a894-9703c0751320')
print(tarefa.descricao)

marcRepo = MarcadoresRepository()
#marcRepo.inserirMarcador(descricao="Marcador Teste")
marcRepo.associarTarefaAoMarcador(tarefa_id= '93105b68-24e4-4483-a894-9703c0751320', marcador_id='1',criado_em=datetime.datetime.now())
print(marcRepo.ObterTodosMarcadores())





from infra.repository.tarefas_repository import TarefaRepository

repo = TarefaRepository()
tarefa = repo.obterTarefa('42f0f050-452b-4d39-87a6-73ef86e1ae07')
print(tarefa.descricao)


#a = repo.ObterTodas()
b = {'Tarefa':[ tarefa.json() for tarefa in repo.ObterTodas()]}
print(b)
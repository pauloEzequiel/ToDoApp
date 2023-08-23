from flask_restful import Api
from resources.tarefa import TarefaManager
from flask_cors import CORS
from flask import redirect
from flask_openapi3 import Info,Tag
from flask_openapi3 import OpenAPI
from schemas.tarefa import TarefaBody, TarefaSchema,obterTarefaSchema,ListaTarefaViewSchema
from schemas.error import ErrorSchema



info = Info(title="TO DO API", version="1.0.0")
tarefa_tag = Tag(name="Gerenciador de Tarefas", description="Adição, visualização e remoção de tarefas na base")

app = OpenAPI(__name__, info=info)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_RESOURCES'] = {r"/tarefas/*": {"origins": "*"}}

@app.get('/',doc_ui=False)
def home():
    return redirect('/openapi')

@app.post('/tarefa',tags = [tarefa_tag],responses={"201":TarefaSchema,"400":ErrorSchema,"404":ErrorSchema})
def addTarefa(body:TarefaBody):
    """
       Endpoint destinado a cadastro de uma nova tarefa.
    """
    return TarefaManager.adicionarTask(body)

@app.get('/tarefa/<string:tarefa_id>',tags = [tarefa_tag],responses={"200":TarefaSchema,"400":ErrorSchema,"404":ErrorSchema})
def obterTarefa(path: obterTarefaSchema):
    """
       Endpoint destinado a obter uma tarefa por ID.
    """

    return TarefaManager.buscarTarefa(path.tarefa_id)

@app.get('/tarefas', tags = [tarefa_tag], responses={"200": ListaTarefaViewSchema,"400":ErrorSchema})
def obterTodasTarefa():
    """
       Retorna todas as tarefas cadastradas.
    """
    return TarefaManager.obterTodasTarefas()

@app.put('/concluirTarefa/<string:tarefa_id>', tags = [tarefa_tag], responses={"200":TarefaSchema,"404":ErrorSchema})
def alterarSituacaoTarefa(path: obterTarefaSchema):
    """
       Endpoint destinado a alterar a situação da tarefa de concluido para não concluido ou vice-versa. 
    """
    return TarefaManager.alterarStatusTarefa(path.tarefa_id)

@app.put('/tarefa/<string:tarefa_id>', tags = [tarefa_tag], responses={"200":TarefaSchema,"201":TarefaSchema})
def atualizarTarefa(path: obterTarefaSchema , body:TarefaBody ):
    """
       Endpoint destinado a atualizar as informações pertinentes a tarefa, caso a tarefa não exista, a tarefa será criada.
    """
    return TarefaManager.atualizarTarefa(path.tarefa_id,body)

@app.delete('/tarefa/<string:tarefa_id>', tags = [tarefa_tag], responses={"200":ErrorSchema,"404":ErrorSchema})
def apagarTarefa(path: obterTarefaSchema):
    """
       Endpoint destinado a apagar uma tarefa.
    """
    return TarefaManager.apagarTarefa(path.tarefa_id)


if __name__ == '__main__':
    app.run(debug=True)
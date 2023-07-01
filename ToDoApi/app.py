from flask import Flask
from flask_restful import Api
from resources.tarefa import Tarefa,Tarefas,UpdateTarefa
from flask_cors import CORS, cross_origin


app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_RESOURCES'] = {r"/tarefas/*": {"origins": "*"}}

api.add_resource(Tarefas,'/tarefas') 
api.add_resource(Tarefa,'/tarefas/<string:tarefa_id>')
api.add_resource(UpdateTarefa,'/concluirTarefa/<string:tarefa_id>')



if __name__ == '__main__':
    app.run(debug=True)
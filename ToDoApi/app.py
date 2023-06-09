from flask import Flask
from flask_restful import Api
from resources.tarefa import Tarefa,Tarefas


app = Flask(__name__)
api = Api(app)


api.add_resource(Tarefas,'/tarefas') 
api.add_resource(Tarefa,'/tarefas/<string:tarefa_id>') 


if __name__ == '__main__':
    app.run(debug=True)
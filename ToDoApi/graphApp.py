from flask import Flask
from dominio.graphql_schemas.tarefa_manager import schema

from flask_graphql import GraphQLView

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)


if __name__ == "__main__":
    app.run()
# ToDO API

MVP desenvolvido com o intuito de alicerçar o conteúdo observado na Sprint.


---
## Componentes de aplicação

<img src="diagrama _todo_app.jpg" alt="Componentes da aplicação"
---
## Como instalar e executar com Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Docker-compose.yml no terminal.
Execute **como administrador** o seguinte comando para construir todos os contêiner da aplicação:

```
$ docker-compose up 
```
---
### Acesso no browser

 - Abra o o [http://localhost:8080/](http://localhost:8080) no navegador para verificar execução do front que interage com os demais componentes docker.

 - Abra o [http://localhost:5000/openapi/](http://localhost:5000/openapi/) no navegador para verificar o status da API Rest em execução.

 - Abra o [http://localhost:5001/graphql](http://localhost:5001/graphql) no navegador para verificar o status da API Graph em execução.

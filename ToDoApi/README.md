# ToDO API

MVP desenvolvido com o intuito de alicerçar o conteúdo observado na Sprint.



---
## Como instalar e executar localmente

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(ambvir)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API REST executar:

```
(ambvir)$ flask run --host 0.0.0.0 --port 5000
```

E para executar a API com Graphql executar:

```
(ambvir)$ flask --app graphApp run --host 0.0.0.0 --port 5001
```
---
### Acesso no browser

 - Abra o [http://localhost:5000/openapi/](http://localhost:5000/openapi/) no navegador para verificar o status da API Rest em execução.

 - Abra o [http://localhost:5001/graphql](http://localhost:5001/graphql) no navegador para verificar o status da API Graph em execução.
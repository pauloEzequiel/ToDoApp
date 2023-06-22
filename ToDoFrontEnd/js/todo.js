
const taskInput = document.querySelector(".todo-list-input");
const addTaskBtn = document.querySelector(".todo-list-add-btn"),
taskbox = document.querySelector(".todo-list")

ObterTodasAsTarefas()

function salvar(){
  let texto = document.querySelector(".todo-list-input").value 
  axios.post(`http://127.0.0.1:5000/tarefas`,{
    descricao: texto,
    concluido: 0
  })
  .then((response) => {
    let tarefa = response.data;
    document.querySelector(".todo-list").innerHTML += `<li><div class='form-check'><label class='form-check-label'><input class='checkbox' type='checkbox'/>${tarefa.descricao }<i class='input-helper'></i></label></div><div class='setting-menu settings'><i class='uil uil-pen'></i><i onclick='DeleteTarefa(this,"${tarefa.tarefa_id}")' class='uil uil-trash'></i></div></li>`;
    })
  .catch((error) => {
    alert("Erro ao realizar operação")
    console.error(error)
  });    
}

function ObterTodasAsTarefas() {
  
axios.get(`http://127.0.0.1:5000/tarefas`)
    .then((response) => {
      const tarefas = response.data;
      var lista = document.querySelector(".todo-list");
      tarefas.Tarefa.forEach(tarefa => {
        let completed = tarefa.concluido == true ? "completed" : "";
        let checked = tarefa.concluido == true ? "checked" : "";
        lista.innerHTML +=`<li class="${completed}"><div class='form-check'><label class='form-check-label'><input class='checkbox' type='checkbox' ${checked}/>${tarefa.descricao }<i class='input-helper'></i></label></div><div class='setting-menu settings'><i class='uil uil-pen'></i><i onclick='DeleteTarefa(this,"${tarefa.tarefa_id}")' class='uil uil-trash'></i></div></li>`
      });
    })
    .catch((error) => {
      console.error(error)
      document.querySelector(".todo-list").innerHTML = `<span>Você não possui tarefas</span>`;
    });
}


function DeleteTarefa(tarefaSelecionada,tarefaId){
  
  axios.delete(`http://127.0.0.1:5000/tarefas/${tarefaId}`)
  .then((response) => {
    let menuDiv = tarefaSelecionada.closest('li');
    menuDiv.remove();
    })
  .catch((error) => {
    alert("Erro ao realizar operação")
    console.error(error)
  });  
}

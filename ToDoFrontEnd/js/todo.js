const addTaskBtn = document.querySelector(".todo-list-add-btn")
const taskbox = document.querySelector(".todo-list")
let isEditTask = false;
let task_id = "";

ObterTodasAsTarefas()

function salvar(){

  let texto = document.querySelector(".todo-list-input").value;

  if(isEditTask){
    console.log(task_id)
    isEditTask = false;
    document.querySelector(".todo-list-input").value ="";
    return;
  }

  axios.post(`http://127.0.0.1:5000/tarefas`,{
    descricao: texto,
    concluido: 0
  })
  .then((response) => {
    let tarefa = response.data;
    document.querySelector(".todo-list").innerHTML += `<li id=${tarefa.tarefa_id}><div class='form-check'><label class='form-check-label'><input class='checkbox' type='checkbox'/>${tarefa.descricao }<i class='input-helper'></i></label></div><div class='setting-menu settings'><i onClick='EditarTarefa("${tarefa.tarefa_id}", "${tarefa.descricao}")' class='uil uil-pen'></i><i onclick='DeleteTarefa(this,"${tarefa.tarefa_id}")' class='uil uil-trash'></i></div></li>`;
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
        lista.innerHTML +=`<li id=${tarefa.tarefa_id} class="${completed}"><div class='form-check'><label class='form-check-label'><input class='checkbox' type='checkbox' ${checked}/>${tarefa.descricao }<i class='input-helper'></i></label></div><div class='setting-menu settings'><i  onClick='EditarTarefa("${tarefa.tarefa_id}", "${tarefa.descricao}")' class='uil uil-pen'></i><i onclick='DeleteTarefa(this,"${tarefa.tarefa_id}")' class='uil uil-trash'></i></div></li>`
      });
    })
    .catch((error) => {
      console.error(error)
      document.querySelector(".todo-list").innerHTML = `<span>Você não possui tarefas</span>`;
    });
}

function EditarTarefa(taskId, textName) {
  isEditTask = true;
  task_id = taskId;
  document.getElementById(task_id).remove();
  document.querySelector(".todo-list-input").value = textName;
  document.querySelector(".todo-list-input").focus();
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

(function($) {
  'use strict';
  $(function() {
    var todoListItem = $('.todo-list');
    todoListItem.on('change', '.checkbox', function() {
      if ($(this).attr('checked')) {
        $(this).removeAttr('checked');
      } else {
        $(this).attr('checked', 'checked');
      }

      $(this).closest("li").toggleClass('completed');

    });
  });
})(jQuery);

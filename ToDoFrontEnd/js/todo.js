
const taskInput = document.querySelector(".todo-list-input");
const addTaskBtn = document.querySelector(".todo-list-add-btn"),
taskbox = document.querySelector(".todo-list")

ObterTodasAsTarefas()

function salvar(){
  console.log(JSON.stringify(document.querySelector(".todo-list-input").value))
  document.querySelector(".todo-list").innerHTML += "<li><div class='form-check'><label class='form-check-label'><input class='checkbox' type='checkbox'/>" + document.querySelector(".todo-list-input").value + "<i class='input-helper'></i></label></div><div class='setting-menu settings'><i class='uil uil-pen'></i><i class='uil uil-trash'></i></div></li>"
}

function ObterTodasAsTarefas() {
  
axios.get(`http://127.0.0.1:5000/tarefas`)
    .then((response) => {
      const tarefas = response.data;
      var lista = document.querySelector(".todo-list");

      tarefas.Tarefa.forEach(tarefa => {
        let completed = tarefa.concluido == true ? "completed" : "";
        let checked = tarefa.concluido == true ? "checked" : "";
        lista.innerHTML +=`<li class="${completed}"><div class='form-check'><label class='form-check-label'><input class='checkbox' type='checkbox' ${checked}/>${tarefa.descricao } ´<i class='input-helper'></i></label></div><div class='setting-menu settings'><i class='uil uil-pen'></i><i class='uil uil-trash'></i></div></li>`
      });
    })
    .catch((error) => {
      console.error(error)
      document.querySelector(".todo-list").innerHTML = `<span>Você não possui tarefas</span>`;
    });

 
}

(function($) {
    'use strict';
    $(function() {
      var todoListItem = $('.todo-list');
      var todoListInput = $('.todo-list-input');
      $('.todo-list-add-btn').on("click", function(event) {
        event.preventDefault();
  
        var item = $(this).prevAll('.todo-list-input').val();
  
        if (item) {
          todoListItem.append("<li><div class='form-check'><label class='form-check-label'><input class='checkbox' type='checkbox'/>" + item + "<i class='input-helper'></i></label></div><i class='remove mdi mdi-close-circle-outline'></i></li>");
          todoListInput.val("");
        }
  
      });
  
      todoListItem.on('change', '.checkbox', function() {
        if ($(this).attr('checked')) {
          $(this).removeAttr('checked');
        } else {
          $(this).attr('checked', 'checked');
        }
  
        $(this).closest("li").toggleClass('completed');
  
      });
  
      todoListItem.on('click', '.remove', function() {
        $(this).parent().remove();
      });
  
    });
  })(jQuery);
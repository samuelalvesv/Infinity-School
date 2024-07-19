let tarefa_responsavel = []

function isNullOrWhiteSpace(input) {
  return !input || input.trim().length === 0;
}

document.addEventListener('DOMContentLoaded', (event) => {
  if (localStorage.getItem('tarefas')) {
    tarefa_responsavel = JSON.parse(localStorage.getItem('tarefas'))
    renderizarTarefas()
  }
});

function Adicionar() {
  try {
    let tarefa = document.getElementById('txt_tarefa').value
    let responsavel = document.getElementById('responsavel').value

    if (isNullOrWhiteSpace(tarefa)) {
      throw new Error("Tarefa inválida.");
    }

    tarefa_responsavel.push(`${tarefa} - Responsavel: ${responsavel}`)
    localStorage.setItem('tarefas', JSON.stringify(tarefa_responsavel))

    document.getElementById('txt_tarefa').value = '';
    renderizarTarefas()
  } catch (error) {
    alert(error.message)
  }
}

function Editar() {
  try {
    let id = parseInt(document.getElementById('txt_id').value)

    if (isNaN(id) || id <= 0 || id > tarefa_responsavel.length) {
      throw new Error("Id inválido.");
    }

    let tarefa_edit = document.getElementById('txt_tarefa_edit').value
    let responsavel_edit = document.getElementById('responsavel_edit').value

    if (isNullOrWhiteSpace(tarefa_edit)) {
      throw new Error("Tarefa inválida.");
    }

    tarefa_responsavel[id - 1] = `${tarefa_edit} - Responsavel: ${responsavel_edit}`
    localStorage.setItem('tarefas', JSON.stringify(tarefa_responsavel))

    document.getElementById('txt_id').value = '';
    document.getElementById('txt_tarefa_edit').value = '';
    renderizarTarefas()
  } catch (error) {
    alert(error.message)
  }
}

function Excluir() {
  try {
    let id = parseInt(document.getElementById('txt_id').value)

    if (isNaN(id) || id <= 0 || id > tarefa_responsavel.length) {
      throw new Error("Id inválido.");
    }

    tarefa_responsavel.splice(id - 1, 1)
    localStorage.setItem('tarefas', JSON.stringify(tarefa_responsavel))

    document.getElementById('txt_id').value = '';
    renderizarTarefas()
  } catch (error) {
    alert(error.message)
  }
}

function renderizarTarefas() {
  let lista_tarefas = document.getElementById('lista_tarefas')
  lista_tarefas.innerHTML = ''

  tarefa_responsavel.forEach((tarefa, id) => {
    let li = document.createElement('li')
    li.innerHTML = `Id: ${id + 1}. ${tarefa}`
    lista_tarefas.appendChild(li)
  });
}

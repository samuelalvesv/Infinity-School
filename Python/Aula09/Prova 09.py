# [PYIA-A09] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário adicionar itens a uma lista de tarefas. 
# A interface da aplicação deve incluir um campo de entrada de texto para o usuário digitar o nome da tarefa e um botão para adicionar a tarefa à lista. 
# Quando o usuário clicar no botão, o item deve ser adicionado a uma lista exibida na tela, mostrando todas as tarefas que foram incluídas até o momento. 
# A lista de tarefas deve ser atualizada dinamicamente sempre que um novo item for adicionado.

import flet as ft

def main(janela: ft.Page):
    janela.title = "Lista de tarefas"
    
    def incluir_tarefa(e):
        nova_tarefa = txt_nova_tarefa.value
        
        txt_nova_tarefa.value = ""
        
        lbl_lista.value += f'\n- {nova_tarefa}'

        janela.update()

    lbl_inicial = ft.Text(
        value="Lista de tarefas",
        size=23,
        color=ft.colors.WHITE
    )
    
    txt_nova_tarefa = ft.TextField(
        label="Adicionar tarefa", 
        hint_text="Digite sua nova tarefa.",
    )

    btn_adicionar = ft.ElevatedButton(
        text="Adicionar",
        width=150,
        height=35,
        bgcolor=ft.colors.GREY_50,
        on_click=incluir_tarefa
    )

    lbl_lista = ft.Text(
        value="",
        size=16,
        color=ft.colors.WHITE
    )

    janela.add(lbl_inicial, txt_nova_tarefa, btn_adicionar, lbl_lista)
    janela.update()

ft.app(target=main)
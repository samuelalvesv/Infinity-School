# [PYIA-A10] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário preencher um formulário de contato. 
# O formulário deve incluir três campos: um campo de texto para o nome, um campo de texto para o email e um campo de texto para a mensagem. 
# Após o usuário preencher esses campos, deve haver um botão de envio. Quando o usuário clicar no botão de envio, 
# os dados devem ser processados e uma mensagem de confirmação deve ser exibida na tela, indicando que o formulário foi enviado com sucesso.

import flet as ft

def main(janela: ft.Page):
    janela.title = "Formulário de contato"

    def is_null_or_empty_or_whitespace(text):
        return text is None or text.strip() == ""
    
    def enviar_mensagem(e):
        if is_null_or_empty_or_whitespace(txt_nome.value):
            resultado.value = "Adicione o nome para continuar com o envio da mensagem."
        elif is_null_or_empty_or_whitespace(txt_mensagem.value):
            resultado.value = "Adicione a mensagem para continuar com o envio da mensagem."
        elif is_null_or_empty_or_whitespace(txt_email.value):
            resultado.value = "Adicione o e-mail para continuar com o envio da mensagem."
        else:
            txt_nome.value = ""
            txt_mensagem.value = ""
            txt_email.value = ""

            resultado.value = "Mensagem enviada com sucesso!"

        janela.update()

    lbl_inicial = ft.Text(
        value="Formulário de contato",
        size=23,
        color=ft.colors.WHITE
    )
    
    txt_nome = ft.TextField(
        label="Nome", 
        hint_text="Digite o nome do contato.",
    )
    
    txt_mensagem = ft.TextField(
        label="Mensagem", 
        hint_text="Digite a mensagem que deseja enviar.",
        multiline=True,
    )
    
    txt_email = ft.TextField(
        label="E-mail", 
        hint_text="Digite o e-mail do seu contato.",
    )

    btn_enviar = ft.ElevatedButton(
        text="Enviar",
        width=150,
        height=35,
        bgcolor=ft.colors.GREY_50,
        on_click=enviar_mensagem
    )

    resultado = ft.Text(
        value="",
        size=16,
        color=ft.colors.WHITE
    )

    janela.add(lbl_inicial, txt_nome, txt_mensagem, txt_email, btn_enviar, resultado)
    janela.update()

ft.app(target=main)

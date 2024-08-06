import flet as ft

# Função para processar o envio do formulário
def enviar_formulario(e):
    nome = campo_nome.value.strip()
    email = campo_email.value.strip()
    mensagem = campo_mensagem.value.strip()

    if nome and email and mensagem:
        # Processa os dados (aqui você pode adicionar código para enviar por e-mail, salvar em um banco de dados, etc.)
        mensagem_confirmacao.value = f"Obrigado, {nome}! Seu formulário foi enviado com sucesso."
        mensagem_confirmacao.update()
        
        # Limpa os campos do formulário
        campo_nome.value = ""
        campo_email.value = ""
        campo_mensagem.value = ""
        campo_nome.update()
        campo_email.update()
        campo_mensagem.update()
    else:
        mensagem_confirmacao.value = "Por favor, preencha todos os campos."
        mensagem_confirmacao.update()

# Cria a interface da aplicação
def principal(pagina: ft.Page):
    global campo_nome, campo_email, campo_mensagem, mensagem_confirmacao

    # Define o layout da página
    pagina.title = "Formulário de Contato"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Cria os campos de entrada
    campo_nome = ft.TextField(label="Nome", autofocus=True)
    campo_email = ft.TextField(label="E-mail")
    campo_mensagem = ft.TextField(label="Mensagem", multiline=True, min_lines=4, max_lines=6)

    # Cria o botão de envio
    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_formulario)

    # Cria a mensagem de confirmação
    mensagem_confirmacao = ft.Text(size=18, color="green")

    # Adiciona os componentes à página
    pagina.add(
        ft.Column(
            controls=[
                campo_nome,
                campo_email,
                campo_mensagem,
                botao_enviar,
                mensagem_confirmacao
            ],
            spacing=10
        )
    )

# Inicializa e executa a aplicação
if __name__ == "__main__":
    ft.app(target=principal)

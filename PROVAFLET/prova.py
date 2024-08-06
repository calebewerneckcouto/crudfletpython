import flet as ft

# Função para adicionar uma nova tarefa à lista
def adicionar_tarefa(e):
    nome_tarefa = campo_tarefa.value.strip()
    if nome_tarefa:
        tarefas.append(nome_tarefa)
        campo_tarefa.value = ""  # Limpa o campo de entrada
        campo_tarefa.update()  # Atualiza o campo de entrada
        atualizar_lista_tarefas()  # Atualiza a lista exibida

# Função para atualizar a lista de tarefas exibida
def atualizar_lista_tarefas():
    lista_tarefas.controls.clear()  # Limpa os itens existentes na lista
    for tarefa in tarefas:
        lista_tarefas.controls.append(ft.Text(tarefa, size=18))
    lista_tarefas.update()  # Atualiza a interface com as novas tarefas

# Lista para armazenar as tarefas
tarefas = []

# Cria a interface da aplicação
def principal(pagina: ft.Page):
    global campo_tarefa, lista_tarefas

    # Define o layout da página
    pagina.title = "Lista de Tarefas"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Cria o campo de entrada e o botão
    campo_tarefa = ft.TextField(label="Digite uma tarefa", autofocus=True)
    botao_adicionar = ft.ElevatedButton(text="Adicionar", on_click=adicionar_tarefa)  # Botão atualizado

    # Cria a lista de tarefas
    lista_tarefas = ft.Column()

    # Adiciona os componentes à página
    pagina.add(
        ft.Column(
            controls=[
                campo_tarefa,
                botao_adicionar,
                lista_tarefas
            ]
        )
    )

# Inicializa e executa a aplicação
if __name__ == "__main__":
    ft.app(target=principal)  # Corrigido para usar a função 'principal'

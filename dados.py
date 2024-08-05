import flet as ft
import sqlite3

def create_user(name, email, cpf, login, password, phone=None, birthdate=None):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO users (name, email, cpf, login, password, phone, birthdate)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, email, cpf, login, password, phone, birthdate))
    conn.commit()
    conn.close()

def read_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()
    return users

def update_user(user_id, name, email, cpf, login, password, phone=None, birthdate=None):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        UPDATE users
        SET name = ?, email = ?, cpf = ?, login = ?, password = ?, phone = ?, birthdate = ?
        WHERE id = ?
    ''', (name, email, cpf, login, password, phone, birthdate, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

def main(page: ft.Page):
    page.title = "Formulario de Cadastro"

    # Criar campos de entrada
    login = ft.TextField(hint_text="Digite seu login")
    senha = ft.TextField(hint_text="Digite sua senha")
    nome = ft.TextField(hint_text="Digite seu nome")
    email = ft.TextField(hint_text="Digite seu Email")
    cpf = ft.TextField(hint_text="Digite seu CPF")
    phone = ft.TextField(hint_text="Digite seu telefone", visible=False)  # Novo campo opcional
    birthdate = ft.TextField(hint_text="Digite sua data de nascimento", visible=False)  # Novo campo opcional

    # Botão de cadastro
    def on_submit(e):
        create_user(nome.value, email.value, cpf.value, login.value, senha.value, phone.value, birthdate.value)
        update_user_list()
        page.controls = page.controls[:-7]  # Remove inputs after submission

    submit_button = ft.ElevatedButton(text="Cadastrar", on_click=on_submit)

    # Listar usuários
    user_list = ft.Column()

    def update_user_list():
        user_list.controls = []
        for user in read_users():
            user_list.controls.append(
                ft.Row([
                    ft.Text(f"Nome: {user[1]}, Email: {user[2]}, CPF: {user[3]}, Login: {user[4]}, Phone: {user[6] if user[6] else 'N/A'}, Birthdate: {user[7] if user[7] else 'N/A'}"),
                    ft.IconButton(ft.icons.EDIT, on_click=lambda e, uid=user[0]: edit_user(uid)),
                    ft.IconButton(ft.icons.DELETE, on_click=lambda e, uid=user[0]: delete_user(uid))
                ])
            )
        page.update()

    def edit_user(user_id):
        user = next(u for u in read_users() if u[0] == user_id)
        nome.value = user[1]
        email.value = user[2]
        cpf.value = user[3]
        login.value = user[4]
        senha.value = user[5]
        phone.value = user[6] if user[6] else ""
        birthdate.value = user[7] if user[7] else ""
        submit_button.text = "Atualizar"
        submit_button.on_click = lambda e: update_user(user_id, nome.value, email.value, cpf.value, login.value, senha.value, phone.value, birthdate.value)

    update_user_list()

    # Adicionar controles à página
    page.add(nome, email, cpf, login, senha, phone, birthdate, submit_button, user_list)

ft.app(target=main)

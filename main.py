import sqlite3
from tkinter import messagebox

class Sistema_de_Registro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            tel TEXT NOT NULL,
                            sexo TEXT NOT NULL,
                            data_nascimento TEXT NOT NULL,
                            endereco TEXT NOT NULL,
                            curso TEXT NOT NULL,
                            picture TEXT NOT NULL)''')
        

    def register_student(self, estudantes):
        self.c.execute("INSERT INTO estudantes(nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES (?,?,?,?,?,?,?,?)",
                        (estudantes))
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Registro com sucesso!')
    
    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()

        return dados
    
    def search_student(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.c.fetchone()
        
        return dados


    def update_student(self, novos_valores):
        query = "UPDATE estudantes SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, curso=?, picture=? WHERE id=? "
        self.c.execute(query, novos_valores)
        self.conn.commit()

        messagebox.showinfo('Sucesso', f'Estudante com id: {novos_valores[8]} foi atualizado!')

    def delete_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()

        messagebox.showinfo('Sucesso', f'Estudante com id: {id} foi excluido!')

# Criando uma instancia do sistema de registro
sistema_de_registro = Sistema_de_Registro()

# ---------- informações ----------
# estudante = ('Elena', "elena@gmail.com", '3331', 'F', '01/05/2007', 'Rio de janeiro, SP', 'Veterinaria', 'imagem2.png')

# sistema_de_registro.register_student(estudante)

# ------- ver estudantes -----------
# todos_alunos = sistema_de_registro.view_all_students()

# ------- procurar aluno ---------
# aluno = sistema_de_registro.search_student(3)

# ---------- atualizar aluno ----------
# estudante = ('Elena', "elena@gmail.com", '444', 'F', '01/05/2007', 'Rio de janeiro, SP', 'Veterinaria', 'imagem2.png', 2)
# aluno = sistema_de_registro.update_student(estudante)

# sistema_de_registro.delete_student(1)
# todos_alunos = sistema_de_registro.view_all_students()






    
    

    
     
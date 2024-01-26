import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('students.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS student (
                       id       INTEGER PRIMARY KEY AUTOINCREMENT,
                       name     TEXT NOT NULL,
                       email    TEXT NOT NULL,
                       phone    TEXT NOT NULL,
                       gender   TEXT NOT NULL,
                       address  TEXT NOT NULL,
                       bday     TEXT NOT NULL,
                       course   TEXT NOT NULL,
                       picture  TEXT NOT NULL
                       )''')
        
    def register_student(self, students):
        self.c.execute('INSERT INTO student (name, email, phone, gender,address, bday, course,picture) VALUES (?,?,?,?,?,?,?,?)', 
                       (students))
        self.conn.commit()
        messagebox.showinfo('Sucesso', 'Aluno Cadastrado com Sucesso')

    def view_students(self):
        self.c.execute('SELECT * FROM student')
        dados = self.c.fetchall()

        for i in dados:
            print(f'ID: {i[0]}\n Nome: {i[1]}\n Email: {i[2]}\n Telefone: {i [3]}\n Sexo: {i[4]}\n Endereço: {i[5]}\n Data de Nascimento: {i[6]}\n Curso: {i[7]}\n Imagem: {i[8]}')
        
    def search_students(self, id):
        self.c.execute('SELECT * FROM student WHERE id=?', (id,))
        dados = self.c.fetchone()
        
        print(f'ID: {dados[0]}\n Nome: {dados[1]}\n Email: {dados[2]}\n Telefone: {dados [3]}\n Sexo: {dados[4]}\n Endereço: {dados[5]}\n Data de Nascimento: {dados[6]}\n Curso: {dados[7]}\n Imagem: {dados[8]}')

    def update_students(self, new_values):
        query = 'UPDATE student SET name=?, email=?, phone=?, gender=?, address=?, bday=?, course=?, picture=? WHERE id=?'
        self.c.execute(query, new_values)
        self.conn.commit()
        
        messagebox.showinfo('Sucesso', 'Informações Atualizadas com Sucesso!')
    
    def delete_students(self, id):
        self.c.execute('DELETE FROM student WHERE id=?', (id,))
        self.conn.commit()
        messagebox.showinfo('Sucesso', 'Estudante Deletado com Sucesso!')

sistema_de_registro = SistemaDeRegistro()

#infos
# student = ('eric', 'eric@gmail.com', '1234', 'M', 'São Paulo, Guarulhos', '01/02/2008', 'Desenvolvimento de Sistemas (DS)', 'image.png' )
# sistema_de_registro.register_student(student)

#ver estudantes
# todos_alunos = sistema_de_registro.view_students()

#procurar aluno
# aluno = sistema_de_registro.search_students()

#atualizar alunos
# student = ('eric', 'eric@gmail.com', '4444', 'M', 'São Paulo, Guarulhos', '01/02/2008', 'Desenvolvimento de Sistemas (DS)', 'image.png', 2)
# atualizar = sistema_de_registro.update_students(student)

#deletar aluno
# sistema_de_registro.delete_students()
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
        messagebox.showinfo('Sucesso', 'Estudante Cadastrado com Sucesso')

    def view_students(self):
        self.c.execute('SELECT * FROM student')
        data = self.c.fetchall()
        return data
        
    def search_students(self, id):
        self.c.execute('SELECT * FROM student WHERE id=?', (id,))
        data = self.c.fetchone()
        return data

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

#TESTS

#Cadaster Students
# student = ('Eric Luis', 'ericluis@gmail.com', '11983085555', 'M', 'Rua tal,200', '01-02-08', 'DS', 'images/eric.png')
# sistema_de_registro.register_student(student)

#Show Students
#all_students = sistema_de_registro.view_students()

#Find Student
#student = sistema_de_registro.search_students(id)

#Update Students
# student = ('?', '?', '?', '?', '?', '?', '?', '?', ?)
# update = sistema_de_registro.update_students()

#Delete
# delete = sistema_de_registro.delete_students(2)

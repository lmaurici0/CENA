from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
from datetime import date
from main import *

co0 = "#2e2d2b" 
co1 = "#feffff"  
co2 = "#e5e5e5"  
co3 = "#00a095"  
co4 = "#403d3d"   
co6 = "#003452"  
co7 = "#ef5350"   
co6 = "#146C94"   
co8 = "#263238"   
co9 = "#e9edf5"   

janela = Tk()
janela.title('Sistema de Cadastro de Alunos')
janela.geometry('810x535')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use('clam')

cursos = ['Engenharia','Medicina','Direito']

frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_table = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_table.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

global imagem, image_string, l_image

app_lg = Image.open('images/logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text='   Sistema de Registro de Alunos', width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place(x=5, y=0)
imagem_string = ""

def escolher_imagem():
    global imagem, imagem_string, l_imagem
    imagem = fd.askopenfilename()
    imagem_string=imagem
    
    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=430, y=10)

    botao_carregar['text'] = 'Trocar de foto'

botao_carregar = Button(frame_details, command=escolher_imagem, text='Carregar Foto', width=20, compound=CENTER, anchor=CENTER, overrelief=GROOVE, font=('Verdana 7 bold'), bg=co1, fg=co0)
botao_carregar.place(x=430, y=160)

def mostrar_alunos():

    list_header = ['id','Nome','Email','Telefone','Sexo','Endereço','Aniversário','Curso']
    df_list = sistema_de_registro.view_students()
    
    tree_aluno = ttk.Treeview(frame_table, selectmode='extended',columns=list_header, show='headings')
    vsb = ttk.Scrollbar(frame_table, orient='vertical', command=tree_aluno.yview)
    hsb = ttk.Scrollbar(frame_table, orient='horizontal', command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0,row=1,sticky='nsew')
    vsb.grid(column=1,row=1,sticky='ns')
    hsb.grid(column=0,row=2,sticky='ew')
    frame_table.grid_rowconfigure(0, weight=12)

    hd=['nw','nw','nw','center','center','center','center','center','center']
    h=[40,150,150,70,70,70,120,100,100]
    n=0

    for col in list_header:
        tree_aluno.heading(col,text=col.title(), anchor=NW)
        tree_aluno.column(col, width=h[n], anchor=hd[n])
        n+=1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)

def adicionar():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sex = c_sex.get()
    bday = e_bday.get()
    end = e_end.get()
    curso = c_curso.get()
    img = imagem_string

    lista = [nome, email, tel, sex, bday, end, curso, img]

    for i in lista:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos!')
            return

    sistema_de_registro.register_student(lista)

    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sex.delete(0, END)
    e_bday.delete(0, END)
    e_end.delete(0, END)
    c_curso.delete(0, END)

    mostrar_alunos()

def atualizar():
    global imagem, imagem_string, l_imagem

    id_aluno = int(e_procurar.get())

    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sex = c_sex.get()
    bday = e_bday.get()
    end = e_end.get()
    curso = c_curso.get()
    img = imagem_string

    lista = [nome, email, tel, sex, bday, end, curso, img, id_aluno]

    for i in lista:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos!')
            return

    sistema_de_registro.update_students(lista)

    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sex.set(0, END)
    e_bday.delete(0, END)
    e_end.delete(0, END)
    c_curso.set(0, END)

    logo_ini = Image.open('images/logo.png')
    logo_ini = logo_ini.resize((50,50))
    logo_ini = ImageTk.PhotoImage(logo_ini)
    logo_ini.place(x=430, y=160)

    mostrar_alunos()

def deletar():
    global imagem, imagem_string, l_imagem

    id_aluno = int(e_procurar.get())

    sistema_de_registro.delete_students(id_aluno)

    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sex.set(0, END)
    e_bday.delete(0, END)
    e_end.delete(0, END)
    c_curso.set(0, END)

    e_procurar.delete(0, END)

    imagem = Image.open('images/logo.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=430, y=10)

    mostrar_alunos()

def procurar_aluno():
    global imagem, imagem_string, l_imagem
    #obtendo o id
    id_aluno = int(e_procurar.get())

    dados = sistema_de_registro.search_students(id_aluno)

    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sex.delete(0, END)
    e_bday.delete(0, END)
    e_end.delete(0, END)
    c_curso.delete(0, END)

    e_nome.insert(END, dados[1])
    e_email.insert(END, dados[2])
    e_tel.insert(END, dados[3])
    c_sex.insert(END, dados[4])
    e_bday.insert(END, dados[5])
    e_end.insert(END, dados[6])
    c_curso.insert(END, dados[7])

    imagem = dados[8]
    imagem_string= imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=430, y=10)

l_nome = Label(frame_details, text='Nome *', anchor=NW, font=('Verdana 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_details, width=30, justify='left', relief='solid')
e_nome.place(x=7,y=40)

l_email = Label(frame_details, text='Email Institucional *', anchor=NW, font=('Verdana 10'), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_details, width=30, justify='left', relief='solid')
e_email.place(x=7,y=100)

l_tel = Label(frame_details, text='Telefone *', anchor=NW, font=('Verdana 10'), bg=co1, fg=co4)
l_tel.place(x=4, y=130)
e_tel = Entry(frame_details, width=15, justify='left', relief='solid')
e_tel.place(x=7,y=160)

l_sex = Label(frame_details, text='Sexo *', anchor=NW, font=('Verdana 10'), bg=co1, fg=co4)
l_sex.place(x=127, y=130)
c_sex = ttk.Combobox(frame_details, width=10, font=('Verdana 8 bold'), justify='center')
c_sex['values'] = ('Masculino', 'Feminino')
c_sex.place(x=130, y=160)

l_bday = Label(frame_details, text='Data de Nascimento *', anchor=NW, font=('Verdana 10'), bg=co1, fg=co4)
l_bday.place(x=255, y=10)
e_bday = DateEntry(frame_details, witdth=18, justify='center', background='darkblue',foreground='white',borderwidth=2,year=2023)
e_bday.place(x=255, y=40)

l_end = Label(frame_details, text='Endereço *', anchor=NW, font=('Verdana 10'), bg=co1, fg=co4)
l_end.place(x=255, y=70)
e_end = Entry(frame_details, width=22, justify='left', relief='solid')
e_end.place(x=255,y=100)

l_curso = Label(frame_details, text='Curso *', anchor=NW, font=('Verdana 10'), bg=co1, fg=co4)
l_curso.place(x=255, y=130)
c_curso = ttk.Combobox(frame_details, width=15, font=('Verdana 8 bold'), justify='center')
c_curso['values'] = (cursos)
c_curso.place(x=255, y=160)

frame_procurar = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text=' Procurar aluno: ', anchor=NW, font=('Verdana 10'), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)

e_procurar = Entry(frame_procurar, width=5, justify='center', relief='solid', font=('Verdana 10'))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procurar, command=procurar_aluno, text=' Procurar', width=9, anchor=CENTER, overrelief=GROOVE, font=('Verdana 7 bold'), bg=co1, fg=co0)
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

add = Image.open('images/add.png')
add = add.resize((25,25))
add = ImageTk.PhotoImage(add)
botao_add = Button(frame_botoes, command=adicionar, image=add, relief=GROOVE, text=' Adicionar', width=100, compound=LEFT, overrelief=RIDGE, font=('Verdana 11'), bg=co1, fg=co0)
botao_add.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

up = Image.open('images/update.png')
up = up.resize((25,25))
up = ImageTk.PhotoImage(up)
botao_up = Button(frame_botoes, command=atualizar, image=up, relief=GROOVE, text=' Atualizar', width=100, compound=LEFT, overrelief=RIDGE, font=('Verdana 11'), bg=co1, fg=co0)
botao_up.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

delete = Image.open('images/delete.png')
delete = delete.resize((25,25))
delete = ImageTk.PhotoImage(delete)
botao_delete = Button(frame_botoes, command=deletar, image=delete, relief=GROOVE, text=' Remover', width=100, compound=LEFT, overrelief=RIDGE, font=('Verdana 11'), bg=co1, fg=co0)
botao_delete.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

l_linha = Label(frame_botoes, relief=GROOVE, width=1, height=123, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
l_linha.place(x=200,y=15)

mostrar_alunos()

janela.mainloop()

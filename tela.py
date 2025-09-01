from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

#  ----- importando main -------
from main import *

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde


#--- criando janela -----
janela = Tk()
janela.title("")
janela.geometry("810x535")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# ---- Criandos frames -----
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

# -------- Trabalhando no frame logo -------
global imagem, imagem_string, l_imagem

app_lg = Image.open("images/logo.png")
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="  Sistema de Registro de Alunos", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place(x=5, y=0)

# -------- abrindo a imagem --------

imagem = Image.open('images/logo.png')
imagem = imagem.resize((130,130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
l_imagem.place(x=390, y=10)



# ------- Criando funcoes para CRUD --------
# funcao adicionar
def adicionar():
    global imagem, imagem_stringm, l_imagem

    #obtendo os valores
    nome = entrada_nome.get()
    email = entrada_email.get()
    tel = entrada_telefone.get()
    sexo = c_sexo.get()
    data = data_nascimento.get()
    endereco = entrada_endereco.get()
    curso = c_curso.get()
    img = imagem_string

    lista = [nome, email, tel, sexo, data, endereco, curso, img]

    # verificando se a lista contem valores vazios
    for i in lista:
        if i =='':
            messagebox.showerror("Erro", 'Preencha todos os campos ')
            return 
        
    # registrando os valores 
    sistema_de_registro.register_student(lista)

    # limpando os campos de entrada
    entrada_nome.delete(0, END)
    entrada_email.delete(0, END)
    entrada_telefone.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    entrada_endereco.delete(0, END)
    c_curso.delete(0, END)

    #mostrando os valores na tabela
    mostrar_alunos()

#funcao procurar aluno
def procurar():
    global imagem, imagem_stringm, l_imagem

    # obtendo o id
    id_aluno = int(entrada_procurar.get())

    # procurando o aluno a partir do id
    dados = sistema_de_registro.search_student(id_aluno)

    # limpando os campos de entrada
    entrada_nome.delete(0, END)
    entrada_email.delete(0, END)
    entrada_telefone.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    entrada_endereco.delete(0, END)
    c_curso.delete(0, END)

    # inserir os valores nos campos de entrada
    entrada_nome.insert(END, dados[1])
    entrada_email.insert(END, dados[2])
    entrada_telefone.insert(END, dados[3])
    c_sexo.insert(END, dados[4])
    data_nascimento.insert(END, dados[5])
    entrada_endereco.insert(END, dados[6])
    c_curso.insert(END, dados[7])

    imagem = dados[8]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

# funcao de atualizar
def atualizar():
    global imagem, imagem_stringm, l_imagem

    # obtendo o id
    id_aluno = int(entrada_procurar.get())


    #obtendo os valores
    nome = entrada_nome.get()
    email = entrada_email.get()
    tel = entrada_telefone.get()
    sexo = c_sexo.get()
    data = data_nascimento.get()
    endereco = entrada_endereco.get()
    curso = c_curso.get()
    img = imagem_string

    lista = [nome, email, tel, sexo, data, endereco, curso, img, id_aluno]

    # verificando se a lista contem valores vazios
    for i in lista:
        if i =='':
            messagebox.showerror("Erro", 'Preencha todos os campos ')
            return 
        
    # registrando os valores 
    sistema_de_registro.update_student (lista)

    # limpando os campos de entrada
    entrada_nome.delete(0, END)
    entrada_email.delete(0, END)
    entrada_telefone.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    entrada_endereco.delete(0, END)
    c_curso.delete(0, END)

    # -------- abrindo a imagem --------
    imagem = Image.open('logo.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    #mostrando os valores na tabela
    mostrar_alunos()

#funcao deletar
def deletar():
    global imagem, imagem_stringm, l_imagem

    # obtendo o id
    id_aluno = int(entrada_procurar.get())

    # deletando o aluno a partir do id
    sistema_de_registro.delete_student(id_aluno)

    # limpando os campos de entrada
    entrada_nome.delete(0, END)
    entrada_email.delete(0, END)
    entrada_telefone.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    entrada_endereco.delete(0, END)
    c_curso.delete(0, END)

    entrada_procurar.delete(0, END)

    # -------- abrindo a imagem --------
    imagem = Image.open('images/logo.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    #mostrando os valores na tabela
    mostrar_alunos()
# ---- Criando os campos de entrada -----
l_nome = Label(frame_details, text="Nome: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
entrada_nome = Entry(frame_details, width=30, justify='left', relief='solid')
entrada_nome.place(x=7, y=40)

l_email = Label(frame_details, text="Email: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=4, y=70)
entrada_email = Entry(frame_details, width=30, justify='left', relief='solid')
entrada_email.place(x=7, y=100)

l_telefone = Label(frame_details, text="Telefone: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_telefone.place(x=4, y=130)
entrada_telefone = Entry(frame_details, width=15, justify='left', relief='solid')
entrada_telefone.place(x=7, y=160)

l_sexo = Label(frame_details, text="Sexo: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sexo.place(x=127, y=130)
c_sexo = ttk.Combobox(frame_details, width=7, font=('Ivy 8 bold'), justify='center')
c_sexo['values'] = ('M', 'F', 'Outro')
c_sexo.place(x=130, y=160)

l_data_nascimento = Label(frame_details, text="Data de nascimento: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_data_nascimento.place(x=220, y=10)
data_nascimento = DateEntry(frame_details, width=18, justify='center', background='darkblue', foreground='white', borderwidht=2, year=2025)
data_nascimento.place(x=224, y=40)

l_endereco = Label(frame_details, text="Endereco: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_endereco.place(x=220, y=70)
entrada_endereco = Entry(frame_details, width=20, justify='left', relief='solid')
entrada_endereco.place(x=224, y=100)

cursos = ["Engenharia", "Medicina", "Sociais"]

l_curso = Label(frame_details, text="Cursos: ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_curso.place(x=220, y=130)
c_curso = ttk.Combobox(frame_details, width=20, font=('Ivy 8 bold'), justify='center')
c_curso['values'] = (cursos)
c_curso.place(x=224, y=160)

# ------ funcao para escolher imagem ------

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    botao_carregar['text'] = 'Trocar de foto'

botao_carregar = Button(frame_details, command=escolher_imagem, text='Carregar Foto'.upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_carregar.place(x=390, y=160)



# ----- tabelas aluno ----- 
def mostrar_alunos():
    # Limpa a tabela antiga antes de desenhar uma nova para evitar sobreposição
    for widget in frame_tabela.winfo_children():
        widget.destroy()

    list_header = ['Id', 'Nome', 'Email', 'Telefone', 'Sexo', 'Data Nasc', 'Endereco', 'Curso']
    df_list = sistema_de_registro.view_all_students()

    # Criando a Treeview (tabela)
    tree_aluno = ttk.Treeview(frame_tabela, columns=list_header, show="headings")
    
    # Criando as barras de rolagem
    vsb = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree_aluno.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient='horizontal', command=tree_aluno.xview) #  BARRA HORIZONTAL ADICIONADA

    # Configurando o comando de rolagem da Treeview para as barras
    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Posicionando os widgets na tela com grid
    tree_aluno.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew', columnspan=2) #  POSICIONANDO A BARRA HORIZONTAL

    # Configurando o frame da tabela para expandir corretamente
    frame_tabela.grid_rowconfigure(0, weight=1)
    frame_tabela.grid_columnconfigure(0, weight=1)

    # Definindo a LARGURA FIXA de cada coluna
    # Ajuste esses valores conforme sua preferência
    larguras = [40, 120, 120, 100, 38, 70, 150, 140] 

    # Configurando os cabeçalhos e a largura das colunas
    for i, col in enumerate(list_header):
        tree_aluno.heading(col, text=col, anchor=NW)
        tree_aluno.column(col, width=larguras[i], anchor=NW, stretch=NO) # Usamos stretch=NO para que a coluna não se encolha

    # Inserindo os dados na tabela
    for item in df_list:
        tree_aluno.insert('', 'end', values=item)

# ----- procurar aluno ---------
frame_procurar_id = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar_id.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar_id, text="Procurar aluno [Insira o ID]", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
entrada_procurar = Entry(frame_procurar_id, width=5, justify='center', relief='solid', font=('Ivy 10'))
entrada_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procurar_id,command=procurar, text='Procurar', width=9,  anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)


# --------- Botoes ------------
app_img_adicionar = Image.open("images/adicionar.png")
app_img_adicionar = app_img_adicionar.resize((25,25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_botoes, command=adicionar,  image=app_img_adicionar, relief=GROOVE,  text=' Adicionar', width=100,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)


app_img_atualizar = Image.open("images/update.png")
app_img_atualizar = app_img_atualizar.resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes, command=atualizar, image=app_img_atualizar, relief=GROOVE,  text=' Atualizar', width=100,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)


app_img_deletar = Image.open("images/delete_icon.png")
app_img_deletar = app_img_deletar.resize((25,25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
app_deletar = Button(frame_botoes, command=deletar, image=app_img_deletar, relief=GROOVE,  text=' Deletar', width=100,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# ------ linha separatoria -------
l_linha = Label(frame_botoes, relief=GROOVE,  text='h', width=1 , height=123, anchor=NW, font=('Ivy 1'), bg=co1, fg=co2)
l_linha.place(x=240, y=15)





# ----- chamar a tabela ------
mostrar_alunos()

janela.mainloop()

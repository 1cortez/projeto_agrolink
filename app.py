from tkinter import *
from tkinter import messagebox
from pathlib import Path
from PIL import Image, ImageTk


from Aplicacao.Logar import Logar

root = Tk()
LOGO_PATH = Path(__file__).resolve().parent / 'logo.png'

class TelaLogin:
    def __init__(self):
        self.root = root
        self.tela_main()
        self.frames()
        self.botoes()
        self.autenticador = Logar()
        
    def tela_main(self):
        self.root.title('Tela de Login')
        self.root.configure(bg='#022326')
        self.root.geometry('1920x1080') 
        
        
    def frames(self):
        self.frame_1 = Frame(self.root, bg='#014040', width=500, height=450, highlightbackground='#BFBFBF', highlightthickness=3)
        self.frame_1.place(relx=0.5, rely=0.5, anchor=CENTER) # y = altura, x = comprimento
        # importando a logo do app
        imagem = Image.open(LOGO_PATH)
        imagem = imagem.resize((160, 160), Image.Resampling.LANCZOS)  # largura x altura
        self.imagem_tk = ImageTk.PhotoImage(imagem) 
       
    def botoes(self):
        self.bt_logar = Button(self.frame_1, text='LOGIN', background='#022326', font=('Arial', 9, 'bold'), command=self.tentativa_login, fg='white')
        self.bt_logar.place(relx=0.2, rely=0.65, relwidth=0.6, relheight=0.06)

        self.bt_cadastrar = Button(self.frame_1, text='Cadastre-se', font=('Arial', 10, 'bold'), command=self.abrir_cadastro, bg='#022326', fg='white')
        self.bt_cadastrar.place(relx=0.54, rely=0.8, relheight=0.05, relwidth=0.2)

        # label da imgimagem = 
        self.lb_imagem = Label(self.frame_1, image=self.imagem_tk, bg='#014040')
        self.lb_imagem.image = self.imagem_tk
        self.lb_imagem.place(relx=0.5, rely=0.19, anchor=CENTER)
        

        # criação da label e entrada do código
        #self.lb_text = Label(self.frame_1, text='AgroLINK', font=('Arial', 19, 'bold'), bg='#014040', fg='white')
        #self.lb_text.place(relx=0.5, rely=0.05, anchor=N)

        self.lb_cadastro = Label(self.frame_1, text='Ainda não tem conta?', font=('Arial', 9, 'bold'), bg='#014040', fg='white' )
        self.lb_cadastro.place(relx=0.4, rely=0.85, anchor=S)

        self.lb_user = Label(self.frame_1)

        # metodo input do tkinter
        self.input_entry = Entry(self.frame_1, highlightbackground='#02735E', highlightthickness=1)
        self.input_entry.place(relx=0.2, rely=0.4, relheight=0.06, relwidth=0.6)
        
        self.input_senha = Entry(self.frame_1, highlightbackground='#02735E', highlightthickness=1, show='*')
        self.input_senha.place(relx=0.2, rely=0.55, relheight=0.06, relwidth=0.6)

        self.lb_user = Label(self.frame_1, text='Usuário', font=('Arial', 12, 'bold'), background='#014040', fg='white')
        self.lb_user.place(relx=0.21, rely=0.33)

        self.lb_senha = Label(self.frame_1, text='Senha', font=('Arial', 12, 'bold'), background='#014040', fg='white')
        self.lb_senha.place(relx=0.21, rely=0.48)

    def abrir_cadastro(self):
        self.frame_1.destroy()  # Remove a tela de login
        Cadastro(self.root)     # Abre a tela de cadastro
    

    def tentativa_login(self):
        email = self.input_entry.get()
        senha = self.input_senha.get()
        resultado,mensagem = self.autenticador.executar(email, senha)
        messagebox.showinfo("Resultado", mensagem) 
        self.frame_1.destroy()  # remove a tela de login
        Contrato(self.root)  


class Cadastro:
    
    def __init__(self, root):
        self.root = root
        self.tela_cadastro()
        self.frames()
        self.botoes()

    def tela_cadastro(self):
        self.root.title('Tela de cadastro')
        self.root.configure(bg='#022326')
        self.root.geometry('1920x1080')
    
    def frames(self):
        self.frame_2 = Frame(self.root, bg='#014040', width=500, height=450, highlightbackground='#BFBFBF', highlightthickness=3)
        self.frame_2.place(relx=0.5, rely=0.5, anchor=CENTER) # y = altura, x = comprimento
    
    def botoes(self):
        self.bt_inscrever = Button(self.frame_2, text='INSCREVER-SE', background='#022326', font=('Arial', 10, 'bold'), fg='white', command=self.abrir_login)
        self.bt_inscrever.place(relx=0.5, rely=0.75, relwidth=0.3, relheight=0.06, anchor=CENTER)

        self.bt_voltar = Button(self.frame_2, text='VOLTAR', background='#022326', font=('Arial', 10, 'bold'), fg='white', command=self.voltar_login)
        self.bt_voltar.place(relx=0.5, rely=0.82, relwidth=0.3, relheight=0.06, anchor=CENTER)

        self.lb_cadastro = Label(self.frame_2, text='Cadastro', font=('Arial', 19, 'bold'), bg='#014040', fg='white')
        self.lb_cadastro.place(relx=0.5, rely=0.05, anchor=N)
        

        # cadastro do user

        self.input_entry = Entry(self.frame_2, highlightbackground='#02735E', highlightthickness=1)
        self.input_entry.place(relx=0.2, rely=0.29, relheight=0.06, relwidth=0.6)
        
        self.input_email = Entry(self.frame_2, highlightbackground='#02735E', highlightthickness=1)
        self.input_email.place(relx=0.2, rely=0.43, relheight=0.06, relwidth=0.6)
        
        self.input_senha = Entry(self.frame_2, highlightbackground='#02735E', highlightthickness=1, show='*')
        self.input_senha.place(relx=0.2, rely=0.58, relheight=0.06, relwidth=0.6)

        self.lb_user = Label(self.frame_2, text='Usuário', font=('Arial', 12, 'bold'), background='#014040', fg='white')
        self.lb_user.place(relx=0.21, rely=0.22)

        self.lb_email = Label(self.frame_2, text='E-mail', font=('Arial', 12, 'bold'), background='#014040', fg='white')
        self.lb_email.place(relx=0.21, rely=0.36)

        self.lb_senha = Label(self.frame_2, text='Senha', font=('Arial', 12, 'bold'), background='#014040', fg='white')
        self.lb_senha.place(relx=0.21, rely=0.51)
    
    def abrir_login(self):
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")  # <- mensagem
        self.frame_2.destroy()  # Remove a tela de cadastro
        TelaLogin()     # Abre a tela de login
    
    def voltar_login(self):
        self.frame_2.destroy()
        TelaLogin()
    
class Contrato:
    def __init__(self, root):
        self.root = root
        self.tela_contrato()
        self.frames()
        self.botoes()

    def tela_contrato(self):
        self.root.title('Tela de empréstimo')
        self.root.configure(bg='#022326')
        self.root.geometry('1920x1080')    

    def frames(self):
        self.frame_3 = Frame(self.root, bg='#014040', width=700, height=450, highlightbackground='#BFBFBF', highlightthickness=3)
        self.frame_3.place(relx=0.5, rely=0.5, anchor=CENTER) # y = altura, x = comprimento

        self.frame_4 = Frame(self.root, bd=10, bg='#014040', highlightbackground='#BFBFBF', highlightthickness=3, width=700, height=100)
        self.frame_4.place(relx=0.5, rely=0.8, anchor=CENTER) #0.25
    
    def botoes(self):
        
        # labels

        self.lb_emprestimo = Label(self.frame_3, text='Solicitação de empréstimo', font=('Arial', 19, 'bold'), bg='#014040', fg='white')
        self.lb_emprestimo.place(relx=0.5, rely=0.05, anchor=N)
        
        self.lb_nome = Label(self.frame_3, text='Nome', font=('Arial', 12, 'bold'), bg='#014040', fg='white')
        self.lb_nome.place(relx=0.17, rely=0.3, anchor=N)
        
        self.lb_renda = Label(self.frame_3, text='Renda anual (R$)', font=('Arial', 12, 'bold'), bg='#014040', fg='white')
        self.lb_renda.place(relx=0.5, rely=0.3, anchor=N)

        self.lb_endereco = Label(self.frame_3, text='Endereço', font=('Arial', 12, 'bold'), bg='#014040', fg='white')
        self.lb_endereco.place(relx=0.83, rely=0.3, anchor=N)

        self.lb_valor = Label(self.frame_3, text='Valor do empréstimo', font=('Arial', 12, 'bold'), bg='#014040', fg='white')
        self.lb_valor.place(relx=0.7, rely=0.52, anchor=CENTER)

        self.lb_produtor = Label(self.frame_3, text='Classificação do Produtor', font=('Arial', 12, 'bold'), bg='#014040', fg='white')
        self.lb_produtor.place(relx=0.3, rely=0.52, anchor=CENTER)

        # entrys 

        self.input_nome = Entry(self.frame_3, highlightbackground='#02735E', highlightthickness=1)
        self.input_nome.place(relx=0.17, rely=0.4, relheight=0.06, relwidth=0.3, anchor=CENTER)

        self.input_renda = Entry(self.frame_3, highlightbackground='#02735E', highlightthickness=1)
        self.input_renda.place(relx=0.5, rely=0.4, relheight=0.06, relwidth=0.3, anchor=CENTER)

        self.input_endereco = Entry(self.frame_3, highlightbackground='#02735E', highlightthickness=1)
        self.input_endereco.place(relx=0.83, rely=0.4, relheight=0.06, relwidth=0.3, anchor=CENTER)

        # drop button
        self.tipvar = StringVar(self.frame_3)
        self.tipv = ('R$ 50.000', 'R$ 150.000', 'R$ 300.000')
        self.tipvar.set('Opções')
        self.popup = OptionMenu(self.frame_3, self.tipvar, *self.tipv)
        self.popup.place(relx=0.7, rely=0.6, relheight=0.06, relwidth=0.3, anchor=CENTER)

        self.tipvar_2 = StringVar(self.frame_3)
        self.tipv_2 = ('Pequeno Produtor', 'Médio Produtor', 'Grande Produtor')
        self.tipvar_2.set('Opções')
        self.popup_2 = OptionMenu(self.frame_3, self.tipvar_2, *self.tipv_2)
        self.popup_2.place(relx=0.3, rely=0.6, relheight=0.06, relwidth=0.3, anchor=CENTER)

        # botoes
        self.bt_solicitar = Button(self.frame_3, text='SOLICITAR', background='#022326', font=('Arial', 9, 'bold'), fg='white')
        self.bt_solicitar.place(relx=0.5, rely=0.8, relwidth=0.3, relheight=0.06, anchor=CENTER)

        self.bt_voltar = Button(self.frame_3, text='VOLTAR', background='#022326', font=('Arial', 9, 'bold'), fg='white', command=self.voltar_login)
        self.bt_voltar.place(relx=0.5, rely=0.88, relwidth=0.3, relheight=0.06, anchor=CENTER)
    
        self.bt_historico = Button(self.frame_4, text='HISTÓRICO', background='#022326', font=('Arial', 9, 'bold'), fg='white', command=self.abrir_historico)
        self.bt_historico.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.3, anchor=CENTER)

        self.bt_novo = Button(self.frame_4, text='NOVO EMPRÉSTIMO', background='#022326', font=('Arial', 9, 'bold'), fg='white')
        self.bt_novo.place(relx=0.17, rely=0.5, relwidth=0.3, relheight=0.3, anchor=CENTER)

        self.bt_encerrar = Button(self.frame_4, text='SAIR', background='#022326', font=('Arial', 9, 'bold'), fg='white', command=self.encerrar)
        self.bt_encerrar.place(relx=0.83, rely=0.5, relwidth=0.3, relheight=0.3, anchor=CENTER)
    
    def voltar_login(self):
        self.frame_3.destroy()
        self.frame_4.destroy()
        TelaLogin()
    
    def abrir_historico(self):
        self.frame_3.destroy()
        self.frame_4.destroy()
        Historico(self.root)
    
    def encerrar(self):
        self.root.destroy()

class Historico:

    def __init__(self, root):
        self.root = root
        self.tela_historico()
        self.frames()
        self.botoes()

    def tela_historico(self):
        self.root.title('Tela de empréstimo')
        self.root.configure(bg='#022326')
        self.root.geometry('1920x1080')    

    def frames(self):
        self.frame_5 = Frame(self.root, bg='#014040', width=700, height=450, highlightbackground='#BFBFBF', highlightthickness=3)
        self.frame_5.place(relx=0.5, rely=0.5, anchor=CENTER) # y = altura, x = comprimento
    
    def botoes(self):

        # labels
        self.lb_historico = Label(self.frame_5, text='Histórico de empréstimos', font=('Arial', 19, 'bold'), bg='#014040', fg='white')
        self.lb_historico.place(relx=0.5, rely=0.05, anchor=N)

        # botoes

        self.bt_voltar = Button(self.frame_5, text='VOLTAR', background='#022326', font=('Arial', 9, 'bold'), fg='white', command=self.voltar_login)
        self.bt_voltar.place(relx=0.5, rely=0.88, relwidth=0.3, relheight=0.06, anchor=CENTER)

    def voltar_login(self):
        self.frame_5.destroy()
        Contrato(self.root)


TelaLogin()
root.mainloop()


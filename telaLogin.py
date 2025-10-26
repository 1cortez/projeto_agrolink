from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

class TelaLogin:
    def __init__(self):
        self.root = root
        self.tela_main()
        self.frames()
        self.botoes()
        
    def tela_main(self):
        self.root.title('Tela de Login')
        self.root.configure(bg='lightgray')
        self.root.geometry('600x600') 
        
    def frames(self):
        self.frame_1 = Frame(self.root, bg='#E3E1E1', width=500, height=450, highlightbackground='#DEA41D', highlightthickness=3)
        self.frame_1.place(relx=0.5, rely=0.5, anchor=CENTER) # y = altura, x = comprimento
    
    def botoes(self):
        self.bt_logar = Button(self.frame_1, text='LOGIN', background='#DEA41D', font=('Arial', 9, 'bold'))
        self.bt_logar.place(relx=0.2, rely=0.65, relwidth=0.6, relheight=0.06)

        self.bt_cadastrar = Button(self.frame_1, text='Cadastre-se', font=('Arial', 10, 'bold'), command=self.abrir_cadastro)
        self.bt_cadastrar.place(relx=0.54, rely=0.8, relheight=0.05, relwidth=0.2)

        # criação da label e entrada do código
        self.lb_text = Label(self.frame_1, text='AgroLINK', font=('Arial', 19, 'bold'), bg='#E3E1E1')
        self.lb_text.place(relx=0.5, rely=0.05, anchor=N)

        self.lb_cadastro = Label(self.frame_1, text='Ainda não tem conta?', font=('Arial', 9, 'bold'), bg='#E3E1E1' )
        self.lb_cadastro.place(relx=0.4, rely=0.85, anchor=S)

        self.lb_user = Label(self.frame_1)

        # metodo input do tkinter
        self.input_entry = Entry(self.frame_1, highlightbackground='#DEA41D', highlightthickness=1)
        self.input_entry.place(relx=0.2, rely=0.4, relheight=0.06, relwidth=0.6)
        
        self.input_senha = Entry(self.frame_1, highlightbackground='#DEA41D', highlightthickness=1, show='*')
        self.input_senha.place(relx=0.2, rely=0.55, relheight=0.06, relwidth=0.6)

        self.lb_user = Label(self.frame_1, text='Usuário', font=('Arial', 12, 'bold'), background='#E3E1E1')
        self.lb_user.place(relx=0.21, rely=0.33)

        self.lb_senha = Label(self.frame_1, text='Senha', font=('Arial', 12, 'bold'), background='#E3E1E1')
        self.lb_senha.place(relx=0.21, rely=0.48)
    
    def abrir_cadastro(self):
        self.frame_1.destroy()  # Remove a tela de login
        Cadastro(self.root)     # Abre a tela de cadastro

class Cadastro:
    
    def __init__(self, root):
        self.root = root
        self.tela_cadastro()
        self.frames()
        self.botoes()

    def tela_cadastro(self):
        self.root.title('Tela de cadastro')
        self.root.configure(bg='lightgray')
        self.root.geometry('600x600')
    
    def frames(self):
        self.frame_2 = Frame(self.root, bg='#E3E1E1', width=500, height=450, highlightbackground='#DEA41D', highlightthickness=3)
        self.frame_2.place(relx=0.5, rely=0.5, anchor=CENTER) # y = altura, x = comprimento
    
    def botoes(self):
        self.bt_inscrever = Button(self.frame_2, text='INSCREVER-SE', command=self.abrir_login, background='#DEA41D', font=('Arial', 10, 'bold'))
        self.bt_inscrever.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.06, anchor=CENTER)

        self.lb_cadastro = Label(self.frame_2, text='Cadastro', font=('Arial', 19, 'bold'), bg='#E3E1E1')
        self.lb_cadastro.place(relx=0.5, rely=0.05, anchor=N)

        # cadastro do user

        self.input_entry = Entry(self.frame_2, highlightbackground='#DEA41D', highlightthickness=1)
        self.input_entry.place(relx=0.2, rely=0.4, relheight=0.06, relwidth=0.6)
        
        self.input_email = Entry(self.frame_2, highlightbackground='#DEA41D', highlightthickness=1)
        self.input_email.place(relx=0.2, rely=0.55, relheight=0.06, relwidth=0.6)
        
        self.input_senha = Entry(self.frame_2, highlightbackground='#DEA41D', highlightthickness=1, show='*')
        self.input_senha.place(relx=0.2, rely=0.7, relheight=0.06, relwidth=0.6)

        self.lb_user = Label(self.frame_2, text='Usuário', font=('Arial', 12, 'bold'), background='#E3E1E1')
        self.lb_user.place(relx=0.21, rely=0.33)

        self.lb_email = Label(self.frame_2, text='E-mail', font=('Arial', 12, 'bold'), background='#E3E1E1')
        self.lb_email.place(relx=0.21, rely=0.48)

        self.lb_senha = Label(self.frame_2, text='Senha', font=('Arial', 12, 'bold'), background='#E3E1E1')
        self.lb_senha.place(relx=0.21, rely=0.63)

        

    def abrir_login(self):

        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")  # <- mensagem
        self.frame_2.destroy()  # Remove a tela de cadastro
        TelaLogin()     # Abre a tela de login
    


TelaLogin()
root.mainloop()


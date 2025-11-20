from tkinter import *
from tkinter import messagebox
from pathlib import Path
from typing import Optional
from PIL import Image, ImageTk


from Aplicacao.Logar import Logar
from Aplicacao.SolicitarNovoEmprestimo import SolicitarNovoEmprestimo

root = Tk()
LOGO_PATH = Path(__file__).resolve().parent / 'logo.png'


class SessaoAplicacao:
    def __init__(self):
        self.cliente_id: Optional[int] = None
        self.token: Optional[str] = None

    def iniciar(self, cliente_id: int, token: str):
        self.cliente_id = cliente_id
        self.token = token

    def ativa(self) -> bool:
        return self.cliente_id is not None and self.token is not None

    def limpar(self):
        self.cliente_id = None
        self.token = None


sessao = SessaoAplicacao()


class TelaLogin:
    def __init__(self, sessao_ativa: Optional[SessaoAplicacao] = None):
        self.root = root
        self.sessao = sessao_ativa or sessao
        self.autenticador = Logar()
        self.sessao.limpar()
        self.tela_main()
        self.frames()
        self.botoes()
        
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
        sucesso, mensagem, cliente_id, token = self.autenticador.executar(email, senha)
        if not sucesso:
            messagebox.showerror("Erro", mensagem)
            return

        if cliente_id is None or token is None:
            messagebox.showerror("Erro", "Não foi possível iniciar a sessão.")
            return

        self.sessao.iniciar(cliente_id, token)
        messagebox.showinfo("Resultado", mensagem)
        self.frame_1.destroy()  # remove a tela de login
        Contrato(self.root, self.sessao)  


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
    def __init__(self, root, sessao_ativa: SessaoAplicacao):
        self.root = root
        self.sessao = sessao_ativa
        self.autenticador = Logar()
        self.solicitador = SolicitarNovoEmprestimo()
        self.frame_3 = None
        self.frame_4 = None

        if not self._sessao_valida():
            return

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
        self.bt_solicitar = Button(
            self.frame_3,
            text='SOLICITAR',
            background='#022326',
            font=('Arial', 9, 'bold'),
            fg='white',
            command=self.solicitar_emprestimo
        )
        self.bt_solicitar.place(relx=0.5, rely=0.8, relwidth=0.3, relheight=0.06, anchor=CENTER)

        self.bt_voltar = Button(self.frame_3, text='VOLTAR', background='#022326', font=('Arial', 9, 'bold'), fg='white', command=self.voltar_login)
        self.bt_voltar.place(relx=0.5, rely=0.88, relwidth=0.3, relheight=0.06, anchor=CENTER)
    
        self.bt_historico = Button(self.frame_4, text='HISTÓRICO', background='#022326', font=('Arial', 9, 'bold'), fg='white', command=self.abrir_historico)
        self.bt_historico.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.3, anchor=CENTER)

        self.bt_novo = Button(self.frame_4, text='NOVO EMPRÉSTIMO', background='#022326', font=('Arial', 9, 'bold'), fg='white')
        self.bt_novo.place(relx=0.17, rely=0.5, relwidth=0.3, relheight=0.3, anchor=CENTER)

        self.bt_encerrar = Button(self.frame_4, text='SAIR', background='#022326', font=('Arial', 9, 'bold'), fg='white', command=self.encerrar)
        self.bt_encerrar.place(relx=0.83, rely=0.5, relwidth=0.3, relheight=0.3, anchor=CENTER)

    def solicitar_emprestimo(self):
        if not self._sessao_valida():
            return

        nome = self.input_nome.get().strip()
        endereco = self.input_endereco.get().strip()
        renda = self.input_renda.get()
        valor_opcao = self.tipvar.get()
        classificacao_opcao = self.tipvar_2.get()

        if not nome:
            messagebox.showerror('Erro', 'Informe o nome do solicitante.')
            return
        if not endereco:
            messagebox.showerror('Erro', 'Informe o endereço do cliente.')
            return
        if valor_opcao == 'Opções':
            messagebox.showerror('Erro', 'Selecione o valor do empréstimo.')
            return
        if classificacao_opcao == 'Opções':
            messagebox.showerror('Erro', 'Selecione a classificação do produtor.')
            return

        try:
            renda_normalizada = self._extrair_inteiro(renda, 'Renda anual')
            valor_normalizado = self._extrair_inteiro(valor_opcao, 'Valor do empréstimo')
            classificacao_normalizada = self._normalizar_classificacao(classificacao_opcao)
        except ValueError as erro:
            messagebox.showerror('Erro', str(erro))
            return

        sucesso, mensagem = self.solicitador.executar(
            nome,
            endereco,
            renda_normalizada,
            valor_normalizado,
            self.sessao.token,
            classificacao_normalizada
        )

        if sucesso:
            messagebox.showinfo('Empréstimo solicitado', mensagem)
            self._limpar_formulario()
        else:
            messagebox.showerror('Erro', mensagem)

    def _extrair_inteiro(self, valor_textual: str, nome_do_campo: str) -> int:
        texto = valor_textual or ''
        apenas_digitos = ''.join(ch for ch in texto if ch.isdigit())
        if not apenas_digitos:
            raise ValueError(f'{nome_do_campo} é obrigatório.')
        return int(apenas_digitos)

    def _normalizar_classificacao(self, opcao: str) -> str:
        normalizado = opcao.strip().lower()
        if normalizado.startswith('pequeno'):
            return 'pequeno'
        if normalizado.startswith('médio') or normalizado.startswith('medio'):
            return 'medio'
        if normalizado.startswith('grande'):
            return 'grande'
        raise ValueError('Classificação do produtor inválida.')

    def _limpar_formulario(self):
        self.input_nome.delete(0, END)
        self.input_renda.delete(0, END)
        self.input_endereco.delete(0, END)
        self.tipvar.set('Opções')
        self.tipvar_2.set('Opções')

    def voltar_login(self):
        self._destruir_frames()
        self.autenticador.encerrar_sessao(self.sessao.token)
        self.sessao.limpar()
        TelaLogin(self.sessao)
    
    def abrir_historico(self):
        if not self._sessao_valida():
            return
        self._destruir_frames()
        Historico(self.root, self.sessao)
    
    def encerrar(self):
        self.autenticador.encerrar_sessao(self.sessao.token)
        self.sessao.limpar()
        self.root.destroy()

    def _destruir_frames(self):
        if self.frame_3 is not None:
            self.frame_3.destroy()
            self.frame_3 = None
        if self.frame_4 is not None:
            self.frame_4.destroy()
            self.frame_4 = None

    def _sessao_valida(self) -> bool:
        if not self.sessao.ativa():
            messagebox.showwarning('Sessão encerrada', 'Faça login novamente para continuar.')
            self._destruir_frames()
            TelaLogin(self.sessao)
            return False

        registro = self.autenticador.buscar_cliente_por_token(self.sessao.token)
        if registro is None:
            messagebox.showwarning('Sessão encerrada', 'Faça login novamente para continuar.')
            self.sessao.limpar()
            self._destruir_frames()
            TelaLogin(self.sessao)
            return False

        return True

class Historico:

    def __init__(self, root, sessao_ativa: SessaoAplicacao):
        self.root = root
        self.sessao = sessao_ativa
        self.autenticador = Logar()
        self.frame_5 = None

        if not self._sessao_valida():
            return

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
        if self.frame_5 is not None:
            self.frame_5.destroy()
            self.frame_5 = None
        Contrato(self.root, self.sessao)

    def _sessao_valida(self) -> bool:
        if not self.sessao.ativa():
            messagebox.showwarning('Sessão encerrada', 'Faça login novamente para continuar.')
            if self.frame_5 is not None:
                self.frame_5.destroy()
                self.frame_5 = None
            TelaLogin(self.sessao)
            return False

        registro = self.autenticador.buscar_cliente_por_token(self.sessao.token)
        if registro is None:
            messagebox.showwarning('Sessão encerrada', 'Faça login novamente para continuar.')
            self.sessao.limpar()
            if self.frame_5 is not None:
                self.frame_5.destroy()
                self.frame_5 = None
            TelaLogin(self.sessao)
            return False

        return True


TelaLogin()
root.mainloop()


#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importa o modulo do pyodbc para conxçao com o banco de dados 
import pyodbc

#importa o modulo tkinter para construçao da interfaces graficas 
from tkinter import *
#importa a classe ttk do modulo tkinter 
from tkinter import ttk

# Fuçao verifica as credencias estao corretas 
def verifica_credenciais():

    #Database - nome do banco de dados 
    conexao = pyodbc.connect ("DRIVER={SQLite3 ODBC Driver};Server=localhost;Database=Projetos_Compras.db")
    

    #cursor -  ferramenta para executar os comando em SQL
    cursor =conexao.cursor()

    #executando uma query que seleciona  os  usuarios  que possuem  o nome e senha no banco de dados
    cursor.execute("SELECT * FROM Usuarios WHERE NOME = ? AND SENHA =?", (nome_usuario_entry.get(), senha_usuario_entry.get ()))
    #recebendo o dados do query 
    usuario =  cursor.fetchone()

    if usuario:

        janela_principal.destroy()
        
        dadosconexao = ("DRIVER={SQLite3 ODBC Driver};Server=localhost;Database=Projetos_Compras.db")


        #UID - LOGIN 
        #PWD - SENHA 

        #Criando a conexao
        conexao = pyodbc.connect(dadosconexao)

        cursor= conexao.cursor()

        conexao.execute("Select * From Produtos")

        print('Conectado com sucesso !')


        #limpa os valores  da treeview
        def listar_dados():
            for i in treeview.get_children():
                treeview.delete(i)

            cursor.execute("Select * From Produtos")

            #amazena os valores retornados pelo comando sql em uma variavel 
            valores =  cursor.fetchall()
            #adicionar os valores na Treeview
            for valor in  valores :

                #popula linha por linha 
                treeview.insert("","end", values=(valor[0],valor[1], valor[2],valor[3], valor [4]))      

        #criando uma janela tkinter com titulos "Cadrasto de Produtos "

        janela = Tk()
        janela.title(" Cadrasto de Produtos ")

        #Definindo a cor de fundo para janela 
        janela.configure(bg="#F5F5F5")

        #deixando a janela em tela cheia 
        janela.attributes("-fullscreen", True)

        Label(janela, text="Nome do Produto: ", font="Arial 16", bg="#F5F5F5").grid(row=0, column=2, padx=10, pady=10)
        nome_produto = Entry(janela,font="Arial 16")
        nome_produto.grid(row=0, column=3, padx=10, pady=10)

        Label(janela, text="Descrição do Produto : ", font="Arial 16", bg="#F5F5F5").grid(row=0, column=5, padx=10, pady=10)
        descriçao_produto = Entry(janela,font="Arial 16")
        descriçao_produto.grid(row=0, column=6, padx=10, pady=10)

        Label(janela, text="Produtos: ", font="Arial 16",fg="blue", bg="#F5F5F5").grid(row=2, column=0, columnspan= 10,padx=10, pady=10)

        Label(janela, text="Quantidade: ", font="Arial 16",fg="blue", bg="#F5F5F5").grid(row=3, column=0, columnspan= 11,padx=10, pady=10)


        #Função para cadastra produtos
        def cadastrar():

            #Cria a janela para cadrastar o produto
            janela_cadastrar =Toplevel(janela)
            janela_cadastrar.title("Cadastrar Produto")

            janela_cadastrar.configure(bg="#FFFFFF")

            # Define a altura e lagura da janela 
            largura_janela = 500
            altura_janela = 230

            #Obtem  lagura  e  altura  da tela  do computador 
            largura_tela = janela_cadastrar.winfo_screenwidth()
            altura_tela = janela_cadastrar.winfo_screenheight()

            #Calculando  a posiçao  da janela  para centraliza-la na tela 
            pos_x = (largura_tela // 2) - (largura_janela // 2)
            pos_y = (altura_tela // 2) - (altura_janela // 2)

            janela_cadastrar.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela, pos_x,pos_y))

            
            for i in  range(5):
                janela_cadastrar.grid_rowconfigure(i, weight=1)

            for i in range(2):
                janela_cadastrar.grid_columnconfigure(i, weight=1)



            #adiciona bordas para cada campo de entratada 
            estilo_borda = {"borderwidth":2, "relief" : "groove"} 

            Label(janela_cadastrar, text="Nome Do Produto", font=("Arial", 12), bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, stick="W")
            nome_produto_cadrastar = Entry(janela_cadastrar,font=("Arial", 12),**estilo_borda )
            nome_produto_cadrastar.grid(row=0, column=1, padx=5, pady=5)

            Label(janela_cadastrar, text="Descrição Do Produto ", font=("Arial", 12), bg="#FFFFFF").grid(row=1, column=0, padx=10, pady=10, stick="W")
            descriçao_produto_cadrastar = Entry(janela_cadastrar,font=("Arial", 12),**estilo_borda )
            descriçao_produto_cadrastar.grid(row=1, column=1, padx=5, pady=5)

            Label(janela_cadastrar, text="Preço Do Produto ", font=("Arial", 12), bg="#FFFFFF").grid(row=2, column=0, padx=10, pady=10, stick="W")
            preço_produto_cadrastar = Entry(janela_cadastrar,font=("Arial", 12),**estilo_borda )
            preço_produto_cadrastar.grid(row=2, column=1, padx=5, pady=5)

            Label(janela_cadastrar, text=" Quantidade", font=("Arial", 12), bg="#FFFFFF").grid(row=3, column=0, padx=10, pady=10, stick="W")
            quantidade_produto_cadrastar = Entry(janela_cadastrar,font=("Arial", 12),**estilo_borda )
            quantidade_produto_cadrastar.grid(row=3, column=1, padx=5, pady=5)

            #Cria uma função para salvar os dados no banco de dados
            def salvar_dados():
                
                #Cria uma tupla com os valores dos campos de texto
                novo_produto_cadastrar = (nome_produto_cadrastar.get(), descriçao_produto_cadrastar.get(), preço_produto_cadrastar.get(), quantidade_produto_cadrastar.get())
                
                #Executa um comando SQL para inserir os dados na tabela Produtos no banco de dados
                cursor.execute("INSERT INTO Produtos (NomeProduto, Descriçao, Preço, Quantidade ) Values (?, ?, ?, ?)", novo_produto_cadastrar)
                conexao.commit() #Gravando no BD


                print("Dados cadastrados com sucesso!")

            
                        
                #Fecha a janela de cadastro
                janela_cadastrar.destroy()

                #chama funçao para listar os valores 
                listar_dados()


                
                
                
            #columnspan - quantas colunas vai ocupar no grid   
            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
            botao_salvar_dados = Button(janela_cadastrar, text="Salvar", font=("Arial", 12), command=salvar_dados)
            botao_salvar_dados.grid(row=4, column=0, columnspan=3, padx=5, pady=5, stick="NSEW")
            
            #columnspan - quantas colunas vai ocupar no grid   
            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)

            botao_cancelar = Button(janela_cadastrar, text="Cancelar", font=("Arial", 12), command=janela_cadastrar.destroy)
            botao_cancelar.grid(row=5, column=0, columnspan=3, padx=5, pady=5, stick="NSEW")

        # criando o botão para grava  os dados na tela de produto  do banco de dados 
        botao_gravar = Button(janela, text= "Novo", command=cadastrar, font="Arial 26")
        botao_gravar.grid(row=4, column=0, columnspan=4 ,stick="NSEW",padx=20,pady=5)
            

        #define o estilo da Treeview
        style = ttk.Style(janela)

        #criando a treeview
        treeview = ttk.Treeview(janela,style="mystyle.Treeview")

        style.theme_use("default")

        style.configure("mystyle.Treeview",font=("Arial" , 14))

        treeview = ttk.Treeview(janela,style="mystyle.Treeview", columns=("ID","NomeProdutos", "Descriçao", "Preço","Quantidade"),show="headings",height=20)

        treeview.heading("ID", text="ID")
        treeview.heading("NomeProdutos", text="Nome do Produtos")
        treeview.heading("Descriçao", text="Descriçao do Porduto")
        treeview.heading("Preço", text="Preço do Produto ")
        treeview.heading("Quantidade", text="Quantidade de Produto")
        treeview.column("#0", width=0, stretch=NO)
        treeview.column("ID", width=100)
        treeview.column("NomeProdutos", width=300)
        treeview.column("Descriçao", width=500)
        treeview.column("Preço", width=200)

        treeview.grid(row=3, column=0, columnspan=10, stick="NSEW")

        #chama funçao para listar os valores 
        listar_dados()

        def editar_dados(event):

            #obtem o intem selecionado na treeview
            item_selecionado = treeview.selection()[0]

            #Obtem os valores do intem selecionado 
            valores_selecionados = treeview.item(item_selecionado)['values']


            #Cria a janela para cadrastar o produto
            janela_ediçao =Toplevel(janela)
            janela_ediçao.title("Editar  Produto")

            janela_ediçao.configure(bg="#FFFFFF")

            # Define a altura e lagura da janela 
            largura_janela = 500
            altura_janela = 300

            #Obtem  lagura  e  altura  da tela  do computador 
            largura_tela = janela_ediçao.winfo_screenwidth()
            altura_tela = janela_ediçao.winfo_screenheight()

            #Calculando  a posiçao  da janela  para centraliza-la na tela 
            pos_x = (largura_tela // 2) - (largura_janela // 2)
            pos_y = (altura_tela // 2) - (altura_janela // 2)

            janela_ediçao.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela, pos_x,pos_y))

            
            for i in  range(5):
                janela_ediçao.grid_rowconfigure(i, weight=1)

            for i in range(2):
                janela_ediçao.grid_columnconfigure(i, weight=1)



            #adiciona bordas para cada campo de entratada 
            estilo_borda = {"borderwidth":2, "relief" : "groove"} 

            Label(janela_ediçao, text="Nome Do Produto", font=("Arial", 16), bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, stick="W")
            nome_produto_ediçao = Entry(janela_ediçao, font=("Arial", 16), bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[1]), **estilo_borda)
            nome_produto_ediçao.grid(row=0, column=1, padx=10, pady=10)

            Label(janela_ediçao, text="Descrição Do Produto ", font=("Arial", 16), bg="#FFFFFF").grid(row=1, column=0, padx=10, pady=10, stick="W")
            descriçao_produto_ediçao = Entry(janela_ediçao, font=("Arial", 16), bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[2]), **estilo_borda)
            descriçao_produto_ediçao.grid(row=1, column=1, padx=10, pady=10)

            Label(janela_ediçao, text="Preço Do Produto ", font=("Arial", 16), bg="#FFFFFF").grid(row=2, column=0, padx=10, pady=10, stick="W")
            preço_produto_ediçao = Entry(janela_ediçao, font=("Arial", 16), bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[3]), **estilo_borda)
            preço_produto_ediçao.grid(row=2, column=1, padx=10, pady=10)

            Label(janela_ediçao, text="Quantidade de produto  ", font=("Arial", 16), bg="#FFFFFF").grid(row=3, column=0, padx=10, pady=10, stick="W")
            quantidade_edicao = Entry(janela_ediçao,font=("Arial", 16),**estilo_borda )
            quantidade_edicao.grid(row=3, column=1, padx=10, pady=10)

            #Cria uma função para salvar os dados no banco de dados
            def salvar_ediçao():
                
                #Obetem os novos valores  do item delecionado na treeview  
                nome_produto = nome_produto_ediçao.get()
                nova_descriçao = descriçao_produto_ediçao.get()
                novo_proço = preço_produto_ediçao.get()
                novo_quantidade = quantidade_edicao.get()

                #atualizando os valores  dos item delecioando
                treeview.item(item_selecionado, values=(valores_selecionados[0],nome_produto,nova_descriçao , novo_proço, novo_quantidade ))
                
                #Executa um comando SQL para inserir os dados na tabela Produtos no banco de dados
                cursor.execute("UPDATE Produtos SET NomeProduto = ?, Descriçao = ?, Preço= ? , Quantidade =?, WHERE ID = ?",
                            (nome_produto, nova_descriçao, novo_proço, novo_quantidade ,valores_selecionados[0]))
                
                conexao.commit() #Gravando no BD


                print("Dados cadastrados com sucesso!")

            
                        
                #Fecha a janela de cadastro
                janela_ediçao.destroy()

                #chama funçao para listar os valores 
                #listar_dados()


                
                
                
            #columnspan - quantas colunas vai ocupar no grid   
            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
            botao_salvar_ediçao = Button(janela_ediçao, text="Altera", font=("Arial", 16), bg="#008000", fg="#FFFFFF", command=salvar_ediçao)
            botao_salvar_ediçao.grid(row=5, column=0, padx=30, pady=30)
            
            #columnspan - quantas colunas vai ocupar no grid   
            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)

            def deletar_registro():

                #recuperando o id do registro secionado na treeview
                selected_item = treeview.selection()[0]
                id = treeview.item(selected_item)["values"][0]

                #deleta  o registro do banco de dados 
                cursor.execute("DELETE FROM Produtos WHERE ID = ? ", (id))

                conexao.commit(),

                #fechando a janela  de ediçao 
                janela_ediçao.destroy()

                #Recarrega os dados sem o novo resgistro   
                listar_dados()



            botao_deletar_edicao = Button(janela_ediçao, text="Deletar", font=("Arial", 16), bg="#FF0000", fg="#FFFFFF", command=deletar_registro)
            botao_deletar_edicao.grid(row=5, column=1, padx=30, pady=30)


        #Adicionar  o evento  de duplo clique  na treeview  para editar os daods do produtos 
        treeview.bind("<Double-1>", editar_dados)

        #configura  a janela para utilizar a barra de menu criada 
        menu_barra = Menu(janela)
        janela.configure(menu= menu_barra)

        #Cria o menu chamado arquivo 
        menu_arquivo = Menu(menu_barra, tearoff=0 )
        menu_barra.add_cascade(label="Arquivo", menu=menu_arquivo)

        #criando uma opção nop menu "arquivo" chamado cadrastar 
        menu_arquivo.add_command(label="Cadastar", command= cadastrar)

        #criando uma opção nop menu "arquivo" chamado Sir
        menu_arquivo.add_command(label="Sair", command= janela.destroy)
        #lrmpa os dados da treeview 
        def limparDados():
                #limpando os valores da treeview 
            for i in treeview.get_children():
                treeview.delete(i)

        #filtra os dados treeview
        def filtrar_dados(nome_produto, descriçao_produto):
            #Verifica se os campos estao vazio
            if not nome_produto.get() and not descriçao_produto.get():
                listar_dados()
                #se ambos os campos estiverem vazio nao faz nada 
                return

            sql = "SELECT * FROM Produtos"
            parametros = []

            if nome_produto.get():
                sql += " WHERE NomeProduto LIKE ?"
                parametros.append('%' + nome_produto.get() + '%')

            if descriçao_produto.get():
                if nome_produto.get():
                    sql += " AND"
                else:
                    sql += " WHERE"
                sql += " Descriçao LIKE ?"
                parametros.append('%' + descriçao_produto.get() + '%')

            cursor.execute(sql, tuple(parametros))
            produtos = cursor.fetchall()
            #limpar os dados da treeview 
            limparDados()
            #preenche com os dados filtrato 
            for dado in produtos:
                treeview.insert('', 'end', values=(dado[0], dado[1], dado[2], dado[3]))

        nome_produto.bind('<KeyRelease>', lambda e: filtrar_dados(nome_produto, descriçao_produto))
        descriçao_produto.bind('<KeyRelease>', lambda e: filtrar_dados(nome_produto, descriçao_produto))



        #deletar o registro 
        def deletar():

                #recuperando o id do registro secionado na treeview
                selected_item = treeview.selection()[0]
                id = treeview.item(selected_item)["values"][0]

                #deleta  o registro do banco de dados 
                cursor.execute("DELETE FROM Produtos WHERE ID = ? ", (id))

                conexao.commit(),

            
                #Recarrega os dados sem o novo resgistro   
                listar_dados()


        # criando o botão para grava  os dados na tela de produto  do banco de dados 
        botao_deletar = Button(janela, text= "Deletar", command=deletar, font="Arial 26")
        botao_deletar.grid(row=4, column=4, columnspan=4 ,stick="NSEW",padx=20,pady=5)





        #Inicia a janela tkinter 
        janela.mainloop()


        cursor.close()
        conexao.close()

    else:
        mesagem_lbl = Label(janela_principal, text=" Nome de Usuarios ou senha incorreta ", fg="red" )
        mesagem_lbl.grid(row=3, column=0, columnspan=2)









# criando a janela principal para tela de Login 
janela_principal = Tk()
janela_principal.title("Tela de Login")

#definindo a cores de fundo da janela 
janela_principal.configure(bg="#FFFFFF")

# Define a altura e lagura da janela 
largura_janela = 450
altura_janela = 300

#Obtem  lagura  e  altura  da tela  do computador 
largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()

#Calculando  a posiçao  da janela  para centraliza-la na tela 
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

janela_principal.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela, pos_x,pos_y))

titulo_lbl = Label(janela_principal , text="Tela de Login", font="Arial 20" , fg="blue", bg="#FFFFFF")
titulo_lbl.grid(row=0, column=0, columnspan=2, pady=20)

#Campo lebal usuario 
nome_usuario_lbl = Label(janela_principal,text="Login", font=" Arial 14 bold",bg="#FFFFFF" )
nome_usuario_lbl.grid(row=1, column=0, sticky="e")

#Campo lebal senha 
senha_usuario_lbl = Label(janela_principal,text="Senha", font=" Arial 14 bold",bg="#FFFFFF" )
senha_usuario_lbl.grid(row=2, column=0, sticky="e")

#Criando um entry para o  campo nome de Usuario com a fonte arial tamanho 14
nome_usuario_entry = Entry(janela_principal, font="Arial 14")
nome_usuario_entry.grid(row= 1, column= 1, pady=10)

#Criando um entry para o  campo nome de Senhha com a fonte arial tamanho 14
senha_usuario_entry = Entry(janela_principal, show= "*",font="Arial 14")
senha_usuario_entry.grid(row= 2, column= 1, pady=10)

entrar_btn = Button(janela_principal, text="Entrar", font="Arial 14", command=verifica_credenciais)
entrar_btn.grid(row=4, column=0, columnspan=2 , padx= 20, pady=10, stick="NSEW")

sair_btn = Button(janela_principal, text="Sair", font="Arial 14", command=janela_principal.destroy)
sair_btn.grid(row=5, column=0, columnspan=2 , padx= 20, pady=10, stick="NSEW")


for i in  range(5):
    janela_principal.grid_rowconfigure(i, weight=1)

for i in range(2):
    janela_principal.grid_columnconfigure(i, weight=1)


#Inicia a janela tkinter 
janela_principal.mainloop()


# In[ ]:





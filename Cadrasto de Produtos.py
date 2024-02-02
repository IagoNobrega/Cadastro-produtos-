{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Conectado com sucesso !\n"
     ]
    }
   ],
   "source": [
    "# Importa o modulo do pyodbc para conxçao com o banco de dados \n",
    "import pyodbc\n",
    "\n",
    "#importa o modulo tkinter para construçao da interfaces graficas \n",
    "from tkinter import *\n",
    "#importa a classe ttk do modulo tkinter \n",
    "from tkinter import ttk\n",
    "\n",
    "# Fuçao verifica as credencias estao corretas \n",
    "def verifica_credenciais():\n",
    "\n",
    "    #Database - nome do banco de dados \n",
    "    conexao = pyodbc.connect (\"DRIVER={SQLite3 ODBC Driver};Server=localhost;Database=Projetos_Compras.db\")\n",
    "    \n",
    "\n",
    "    #cursor -  ferramenta para executar os comando em SQL\n",
    "    cursor =conexao.cursor()\n",
    "\n",
    "    #executando uma query que seleciona  os  usuarios  que possuem  o nome e senha no banco de dados\n",
    "    cursor.execute(\"SELECT * FROM Usuarios WHERE NOME = ? AND SENHA =?\", (nome_usuario_entry.get(), senha_usuario_entry.get ()))\n",
    "    #recebendo o dados do query \n",
    "    usuario =  cursor.fetchone()\n",
    "\n",
    "    if usuario:\n",
    "\n",
    "        janela_principal.destroy()\n",
    "        \n",
    "        dadosconexao = (\"DRIVER={SQLite3 ODBC Driver};Server=localhost;Database=Projetos_Compras.db\")\n",
    "\n",
    "\n",
    "        #UID - LOGIN \n",
    "        #PWD - SENHA \n",
    "\n",
    "        #Criando a conexao\n",
    "        conexao = pyodbc.connect(dadosconexao)\n",
    "\n",
    "        cursor= conexao.cursor()\n",
    "\n",
    "        conexao.execute(\"Select * From Produtos\")\n",
    "\n",
    "        print('Conectado com sucesso !')\n",
    "\n",
    "\n",
    "        #limpa os valores  da treeview\n",
    "        def listar_dados():\n",
    "            for i in treeview.get_children():\n",
    "                treeview.delete(i)\n",
    "\n",
    "            cursor.execute(\"Select * From Produtos\")\n",
    "\n",
    "            #amazena os valores retornados pelo comando sql em uma variavel \n",
    "            valores =  cursor.fetchall()\n",
    "            #adicionar os valores na Treeview\n",
    "            for valor in  valores :\n",
    "\n",
    "                #popula linha por linha \n",
    "                treeview.insert(\"\",\"end\", values=(valor[0],valor[1], valor[2],valor[3], valor [4]))      \n",
    "\n",
    "        #criando uma janela tkinter com titulos \"Cadrasto de Produtos \"\n",
    "\n",
    "        janela = Tk()\n",
    "        janela.title(\" Cadrasto de Produtos \")\n",
    "\n",
    "        #Definindo a cor de fundo para janela \n",
    "        janela.configure(bg=\"#F5F5F5\")\n",
    "\n",
    "        #deixando a janela em tela cheia \n",
    "        janela.attributes(\"-fullscreen\", True)\n",
    "\n",
    "        Label(janela, text=\"Nome do Produto: \", font=\"Arial 16\", bg=\"#F5F5F5\").grid(row=0, column=2, padx=10, pady=10)\n",
    "        nome_produto = Entry(janela,font=\"Arial 16\")\n",
    "        nome_produto.grid(row=0, column=3, padx=10, pady=10)\n",
    "\n",
    "        Label(janela, text=\"Descrição do Produto : \", font=\"Arial 16\", bg=\"#F5F5F5\").grid(row=0, column=5, padx=10, pady=10)\n",
    "        descriçao_produto = Entry(janela,font=\"Arial 16\")\n",
    "        descriçao_produto.grid(row=0, column=6, padx=10, pady=10)\n",
    "\n",
    "        Label(janela, text=\"Produtos: \", font=\"Arial 16\",fg=\"blue\", bg=\"#F5F5F5\").grid(row=2, column=0, columnspan= 10,padx=10, pady=10)\n",
    "\n",
    "        Label(janela, text=\"Quantidade: \", font=\"Arial 16\",fg=\"blue\", bg=\"#F5F5F5\").grid(row=3, column=0, columnspan= 11,padx=10, pady=10)\n",
    "\n",
    "\n",
    "        #Função para cadastra produtos\n",
    "        def cadastrar():\n",
    "\n",
    "            #Cria a janela para cadrastar o produto\n",
    "            janela_cadastrar =Toplevel(janela)\n",
    "            janela_cadastrar.title(\"Cadastrar Produto\")\n",
    "\n",
    "            janela_cadastrar.configure(bg=\"#FFFFFF\")\n",
    "\n",
    "            # Define a altura e lagura da janela \n",
    "            largura_janela = 500\n",
    "            altura_janela = 230\n",
    "\n",
    "            #Obtem  lagura  e  altura  da tela  do computador \n",
    "            largura_tela = janela_cadastrar.winfo_screenwidth()\n",
    "            altura_tela = janela_cadastrar.winfo_screenheight()\n",
    "\n",
    "            #Calculando  a posiçao  da janela  para centraliza-la na tela \n",
    "            pos_x = (largura_tela // 2) - (largura_janela // 2)\n",
    "            pos_y = (altura_tela // 2) - (altura_janela // 2)\n",
    "\n",
    "            janela_cadastrar.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela, pos_x,pos_y))\n",
    "\n",
    "            \n",
    "            for i in  range(5):\n",
    "                janela_cadastrar.grid_rowconfigure(i, weight=1)\n",
    "\n",
    "            for i in range(2):\n",
    "                janela_cadastrar.grid_columnconfigure(i, weight=1)\n",
    "\n",
    "\n",
    "\n",
    "            #adiciona bordas para cada campo de entratada \n",
    "            estilo_borda = {\"borderwidth\":2, \"relief\" : \"groove\"} \n",
    "\n",
    "            Label(janela_cadastrar, text=\"Nome Do Produto\", font=(\"Arial\", 12), bg=\"#FFFFFF\").grid(row=0, column=0, padx=10, pady=10, stick=\"W\")\n",
    "            nome_produto_cadrastar = Entry(janela_cadastrar,font=(\"Arial\", 12),**estilo_borda )\n",
    "            nome_produto_cadrastar.grid(row=0, column=1, padx=5, pady=5)\n",
    "\n",
    "            Label(janela_cadastrar, text=\"Descrição Do Produto \", font=(\"Arial\", 12), bg=\"#FFFFFF\").grid(row=1, column=0, padx=10, pady=10, stick=\"W\")\n",
    "            descriçao_produto_cadrastar = Entry(janela_cadastrar,font=(\"Arial\", 12),**estilo_borda )\n",
    "            descriçao_produto_cadrastar.grid(row=1, column=1, padx=5, pady=5)\n",
    "\n",
    "            Label(janela_cadastrar, text=\"Preço Do Produto \", font=(\"Arial\", 12), bg=\"#FFFFFF\").grid(row=2, column=0, padx=10, pady=10, stick=\"W\")\n",
    "            preço_produto_cadrastar = Entry(janela_cadastrar,font=(\"Arial\", 12),**estilo_borda )\n",
    "            preço_produto_cadrastar.grid(row=2, column=1, padx=5, pady=5)\n",
    "\n",
    "            Label(janela_cadastrar, text=\" Quantidade\", font=(\"Arial\", 12), bg=\"#FFFFFF\").grid(row=3, column=0, padx=10, pady=10, stick=\"W\")\n",
    "            quantidade_produto_cadrastar = Entry(janela_cadastrar,font=(\"Arial\", 12),**estilo_borda )\n",
    "            quantidade_produto_cadrastar.grid(row=3, column=1, padx=5, pady=5)\n",
    "\n",
    "            #Cria uma função para salvar os dados no banco de dados\n",
    "            def salvar_dados():\n",
    "                \n",
    "                #Cria uma tupla com os valores dos campos de texto\n",
    "                novo_produto_cadastrar = (nome_produto_cadrastar.get(), descriçao_produto_cadrastar.get(), preço_produto_cadrastar.get(), quantidade_produto_cadrastar.get())\n",
    "                \n",
    "                #Executa um comando SQL para inserir os dados na tabela Produtos no banco de dados\n",
    "                cursor.execute(\"INSERT INTO Produtos (NomeProduto, Descriçao, Preço, Quantidade ) Values (?, ?, ?, ?)\", novo_produto_cadastrar)\n",
    "                conexao.commit() #Gravando no BD\n",
    "\n",
    "\n",
    "                print(\"Dados cadastrados com sucesso!\")\n",
    "\n",
    "            \n",
    "                        \n",
    "                #Fecha a janela de cadastro\n",
    "                janela_cadastrar.destroy()\n",
    "\n",
    "                #chama funçao para listar os valores \n",
    "                listar_dados()\n",
    "\n",
    "\n",
    "                \n",
    "                \n",
    "                \n",
    "            #columnspan - quantas colunas vai ocupar no grid   \n",
    "            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)\n",
    "            botao_salvar_dados = Button(janela_cadastrar, text=\"Salvar\", font=(\"Arial\", 12), command=salvar_dados)\n",
    "            botao_salvar_dados.grid(row=4, column=0, columnspan=3, padx=5, pady=5, stick=\"NSEW\")\n",
    "            \n",
    "            #columnspan - quantas colunas vai ocupar no grid   \n",
    "            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)\n",
    "\n",
    "            botao_cancelar = Button(janela_cadastrar, text=\"Cancelar\", font=(\"Arial\", 12), command=janela_cadastrar.destroy)\n",
    "            botao_cancelar.grid(row=5, column=0, columnspan=3, padx=5, pady=5, stick=\"NSEW\")\n",
    "\n",
    "        # criando o botão para grava  os dados na tela de produto  do banco de dados \n",
    "        botao_gravar = Button(janela, text= \"Novo\", command=cadastrar, font=\"Arial 26\")\n",
    "        botao_gravar.grid(row=4, column=0, columnspan=4 ,stick=\"NSEW\",padx=20,pady=5)\n",
    "            \n",
    "\n",
    "        #define o estilo da Treeview\n",
    "        style = ttk.Style(janela)\n",
    "\n",
    "        #criando a treeview\n",
    "        treeview = ttk.Treeview(janela,style=\"mystyle.Treeview\")\n",
    "\n",
    "        style.theme_use(\"default\")\n",
    "\n",
    "        style.configure(\"mystyle.Treeview\",font=(\"Arial\" , 14))\n",
    "\n",
    "        treeview = ttk.Treeview(janela,style=\"mystyle.Treeview\", columns=(\"ID\",\"NomeProdutos\", \"Descriçao\", \"Preço\",\"Quantidade\"),show=\"headings\",height=20)\n",
    "\n",
    "        treeview.heading(\"ID\", text=\"ID\")\n",
    "        treeview.heading(\"NomeProdutos\", text=\"Nome do Produtos\")\n",
    "        treeview.heading(\"Descriçao\", text=\"Descriçao do Porduto\")\n",
    "        treeview.heading(\"Preço\", text=\"Preço do Produto \")\n",
    "        treeview.heading(\"Quantidade\", text=\"Quantidade de Produto\")\n",
    "        treeview.column(\"#0\", width=0, stretch=NO)\n",
    "        treeview.column(\"ID\", width=100)\n",
    "        treeview.column(\"NomeProdutos\", width=300)\n",
    "        treeview.column(\"Descriçao\", width=500)\n",
    "        treeview.column(\"Preço\", width=200)\n",
    "\n",
    "        treeview.grid(row=3, column=0, columnspan=10, stick=\"NSEW\")\n",
    "\n",
    "        #chama funçao para listar os valores \n",
    "        listar_dados()\n",
    "\n",
    "        def editar_dados(event):\n",
    "\n",
    "            #obtem o intem selecionado na treeview\n",
    "            item_selecionado = treeview.selection()[0]\n",
    "\n",
    "            #Obtem os valores do intem selecionado \n",
    "            valores_selecionados = treeview.item(item_selecionado)['values']\n",
    "\n",
    "\n",
    "            #Cria a janela para cadrastar o produto\n",
    "            janela_ediçao =Toplevel(janela)\n",
    "            janela_ediçao.title(\"Editar  Produto\")\n",
    "\n",
    "            janela_ediçao.configure(bg=\"#FFFFFF\")\n",
    "\n",
    "            # Define a altura e lagura da janela \n",
    "            largura_janela = 500\n",
    "            altura_janela = 300\n",
    "\n",
    "            #Obtem  lagura  e  altura  da tela  do computador \n",
    "            largura_tela = janela_ediçao.winfo_screenwidth()\n",
    "            altura_tela = janela_ediçao.winfo_screenheight()\n",
    "\n",
    "            #Calculando  a posiçao  da janela  para centraliza-la na tela \n",
    "            pos_x = (largura_tela // 2) - (largura_janela // 2)\n",
    "            pos_y = (altura_tela // 2) - (altura_janela // 2)\n",
    "\n",
    "            janela_ediçao.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela, pos_x,pos_y))\n",
    "\n",
    "            \n",
    "            for i in  range(5):\n",
    "                janela_ediçao.grid_rowconfigure(i, weight=1)\n",
    "\n",
    "            for i in range(2):\n",
    "                janela_ediçao.grid_columnconfigure(i, weight=1)\n",
    "\n",
    "\n",
    "\n",
    "            #adiciona bordas para cada campo de entratada \n",
    "            estilo_borda = {\"borderwidth\":2, \"relief\" : \"groove\"} \n",
    "\n",
    "            Label(janela_ediçao, text=\"Nome Do Produto\", font=(\"Arial\", 16), bg=\"#FFFFFF\").grid(row=0, column=0, padx=10, pady=10, stick=\"W\")\n",
    "            nome_produto_ediçao = Entry(janela_ediçao, font=(\"Arial\", 16), bg=\"#FFFFFF\", textvariable=StringVar(value=valores_selecionados[1]), **estilo_borda)\n",
    "            nome_produto_ediçao.grid(row=0, column=1, padx=10, pady=10)\n",
    "\n",
    "            Label(janela_ediçao, text=\"Descrição Do Produto \", font=(\"Arial\", 16), bg=\"#FFFFFF\").grid(row=1, column=0, padx=10, pady=10, stick=\"W\")\n",
    "            descriçao_produto_ediçao = Entry(janela_ediçao, font=(\"Arial\", 16), bg=\"#FFFFFF\", textvariable=StringVar(value=valores_selecionados[2]), **estilo_borda)\n",
    "            descriçao_produto_ediçao.grid(row=1, column=1, padx=10, pady=10)\n",
    "\n",
    "            Label(janela_ediçao, text=\"Preço Do Produto \", font=(\"Arial\", 16), bg=\"#FFFFFF\").grid(row=2, column=0, padx=10, pady=10, stick=\"W\")\n",
    "            preço_produto_ediçao = Entry(janela_ediçao, font=(\"Arial\", 16), bg=\"#FFFFFF\", textvariable=StringVar(value=valores_selecionados[3]), **estilo_borda)\n",
    "            preço_produto_ediçao.grid(row=2, column=1, padx=10, pady=10)\n",
    "\n",
    "            Label(janela_ediçao, text=\"Quantidade de produto  \", font=(\"Arial\", 16), bg=\"#FFFFFF\").grid(row=3, column=0, padx=10, pady=10, stick=\"W\")\n",
    "            quantidade_edicao = Entry(janela_ediçao,font=(\"Arial\", 16),**estilo_borda )\n",
    "            quantidade_edicao.grid(row=3, column=1, padx=10, pady=10)\n",
    "\n",
    "            #Cria uma função para salvar os dados no banco de dados\n",
    "            def salvar_ediçao():\n",
    "                \n",
    "                #Obetem os novos valores  do item delecionado na treeview  \n",
    "                nome_produto = nome_produto_ediçao.get()\n",
    "                nova_descriçao = descriçao_produto_ediçao.get()\n",
    "                novo_proço = preço_produto_ediçao.get()\n",
    "                novo_quantidade = quantidade_edicao.get()\n",
    "\n",
    "                #atualizando os valores  dos item delecioando\n",
    "                treeview.item(item_selecionado, values=(valores_selecionados[0],nome_produto,nova_descriçao , novo_proço, novo_quantidade ))\n",
    "                \n",
    "                #Executa um comando SQL para inserir os dados na tabela Produtos no banco de dados\n",
    "                cursor.execute(\"UPDATE Produtos SET NomeProduto = ?, Descriçao = ?, Preço= ? , Quantidade =?, WHERE ID = ?\",\n",
    "                            (nome_produto, nova_descriçao, novo_proço, novo_quantidade ,valores_selecionados[0]))\n",
    "                \n",
    "                conexao.commit() #Gravando no BD\n",
    "\n",
    "\n",
    "                print(\"Dados cadastrados com sucesso!\")\n",
    "\n",
    "            \n",
    "                        \n",
    "                #Fecha a janela de cadastro\n",
    "                janela_ediçao.destroy()\n",
    "\n",
    "                #chama funçao para listar os valores \n",
    "                #listar_dados()\n",
    "\n",
    "\n",
    "                \n",
    "                \n",
    "                \n",
    "            #columnspan - quantas colunas vai ocupar no grid   \n",
    "            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)\n",
    "            botao_salvar_ediçao = Button(janela_ediçao, text=\"Altera\", font=(\"Arial\", 16), bg=\"#008000\", fg=\"#FFFFFF\", command=salvar_ediçao)\n",
    "            botao_salvar_ediçao.grid(row=5, column=0, padx=30, pady=30)\n",
    "            \n",
    "            #columnspan - quantas colunas vai ocupar no grid   \n",
    "            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)\n",
    "\n",
    "            def deletar_registro():\n",
    "\n",
    "                #recuperando o id do registro secionado na treeview\n",
    "                selected_item = treeview.selection()[0]\n",
    "                id = treeview.item(selected_item)[\"values\"][0]\n",
    "\n",
    "                #deleta  o registro do banco de dados \n",
    "                cursor.execute(\"DELETE FROM Produtos WHERE ID = ? \", (id))\n",
    "\n",
    "                conexao.commit(),\n",
    "\n",
    "                #fechando a janela  de ediçao \n",
    "                janela_ediçao.destroy()\n",
    "\n",
    "                #Recarrega os dados sem o novo resgistro   \n",
    "                listar_dados()\n",
    "\n",
    "\n",
    "\n",
    "            botao_deletar_edicao = Button(janela_ediçao, text=\"Deletar\", font=(\"Arial\", 16), bg=\"#FF0000\", fg=\"#FFFFFF\", command=deletar_registro)\n",
    "            botao_deletar_edicao.grid(row=5, column=1, padx=30, pady=30)\n",
    "\n",
    "\n",
    "        #Adicionar  o evento  de duplo clique  na treeview  para editar os daods do produtos \n",
    "        treeview.bind(\"<Double-1>\", editar_dados)\n",
    "\n",
    "        #configura  a janela para utilizar a barra de menu criada \n",
    "        menu_barra = Menu(janela)\n",
    "        janela.configure(menu= menu_barra)\n",
    "\n",
    "        #Cria o menu chamado arquivo \n",
    "        menu_arquivo = Menu(menu_barra, tearoff=0 )\n",
    "        menu_barra.add_cascade(label=\"Arquivo\", menu=menu_arquivo)\n",
    "\n",
    "        #criando uma opção nop menu \"arquivo\" chamado cadrastar \n",
    "        menu_arquivo.add_command(label=\"Cadastar\", command= cadastrar)\n",
    "\n",
    "        #criando uma opção nop menu \"arquivo\" chamado Sir\n",
    "        menu_arquivo.add_command(label=\"Sair\", command= janela.destroy)\n",
    "        #lrmpa os dados da treeview \n",
    "        def limparDados():\n",
    "                #limpando os valores da treeview \n",
    "            for i in treeview.get_children():\n",
    "                treeview.delete(i)\n",
    "\n",
    "        #filtra os dados treeview\n",
    "        def filtrar_dados(nome_produto, descriçao_produto):\n",
    "            #Verifica se os campos estao vazio\n",
    "            if not nome_produto.get() and not descriçao_produto.get():\n",
    "                listar_dados()\n",
    "                #se ambos os campos estiverem vazio nao faz nada \n",
    "                return\n",
    "\n",
    "            sql = \"SELECT * FROM Produtos\"\n",
    "            parametros = []\n",
    "\n",
    "            if nome_produto.get():\n",
    "                sql += \" WHERE NomeProduto LIKE ?\"\n",
    "                parametros.append('%' + nome_produto.get() + '%')\n",
    "\n",
    "            if descriçao_produto.get():\n",
    "                if nome_produto.get():\n",
    "                    sql += \" AND\"\n",
    "                else:\n",
    "                    sql += \" WHERE\"\n",
    "                sql += \" Descriçao LIKE ?\"\n",
    "                parametros.append('%' + descriçao_produto.get() + '%')\n",
    "\n",
    "            cursor.execute(sql, tuple(parametros))\n",
    "            produtos = cursor.fetchall()\n",
    "            #limpar os dados da treeview \n",
    "            limparDados()\n",
    "            #preenche com os dados filtrato \n",
    "            for dado in produtos:\n",
    "                treeview.insert('', 'end', values=(dado[0], dado[1], dado[2], dado[3]))\n",
    "\n",
    "        nome_produto.bind('<KeyRelease>', lambda e: filtrar_dados(nome_produto, descriçao_produto))\n",
    "        descriçao_produto.bind('<KeyRelease>', lambda e: filtrar_dados(nome_produto, descriçao_produto))\n",
    "\n",
    "\n",
    "\n",
    "        #deletar o registro \n",
    "        def deletar():\n",
    "\n",
    "                #recuperando o id do registro secionado na treeview\n",
    "                selected_item = treeview.selection()[0]\n",
    "                id = treeview.item(selected_item)[\"values\"][0]\n",
    "\n",
    "                #deleta  o registro do banco de dados \n",
    "                cursor.execute(\"DELETE FROM Produtos WHERE ID = ? \", (id))\n",
    "\n",
    "                conexao.commit(),\n",
    "\n",
    "            \n",
    "                #Recarrega os dados sem o novo resgistro   \n",
    "                listar_dados()\n",
    "\n",
    "\n",
    "        # criando o botão para grava  os dados na tela de produto  do banco de dados \n",
    "        botao_deletar = Button(janela, text= \"Deletar\", command=deletar, font=\"Arial 26\")\n",
    "        botao_deletar.grid(row=4, column=4, columnspan=4 ,stick=\"NSEW\",padx=20,pady=5)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "        #Inicia a janela tkinter \n",
    "        janela.mainloop()\n",
    "\n",
    "\n",
    "        cursor.close()\n",
    "        conexao.close()\n",
    "\n",
    "    else:\n",
    "        mesagem_lbl = Label(janela_principal, text=\" Nome de Usuarios ou senha incorreta \", fg=\"red\" )\n",
    "        mesagem_lbl.grid(row=3, column=0, columnspan=2)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "# criando a janela principal para tela de Login \n",
    "janela_principal = Tk()\n",
    "janela_principal.title(\"Tela de Login\")\n",
    "\n",
    "#definindo a cores de fundo da janela \n",
    "janela_principal.configure(bg=\"#FFFFFF\")\n",
    "\n",
    "# Define a altura e lagura da janela \n",
    "largura_janela = 450\n",
    "altura_janela = 300\n",
    "\n",
    "#Obtem  lagura  e  altura  da tela  do computador \n",
    "largura_tela = janela_principal.winfo_screenwidth()\n",
    "altura_tela = janela_principal.winfo_screenheight()\n",
    "\n",
    "#Calculando  a posiçao  da janela  para centraliza-la na tela \n",
    "pos_x = (largura_tela // 2) - (largura_janela // 2)\n",
    "pos_y = (altura_tela // 2) - (altura_janela // 2)\n",
    "\n",
    "janela_principal.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela, pos_x,pos_y))\n",
    "\n",
    "titulo_lbl = Label(janela_principal , text=\"Tela de Login\", font=\"Arial 20\" , fg=\"blue\", bg=\"#FFFFFF\")\n",
    "titulo_lbl.grid(row=0, column=0, columnspan=2, pady=20)\n",
    "\n",
    "#Campo lebal usuario \n",
    "nome_usuario_lbl = Label(janela_principal,text=\"Login\", font=\" Arial 14 bold\",bg=\"#FFFFFF\" )\n",
    "nome_usuario_lbl.grid(row=1, column=0, sticky=\"e\")\n",
    "\n",
    "#Campo lebal senha \n",
    "senha_usuario_lbl = Label(janela_principal,text=\"Senha\", font=\" Arial 14 bold\",bg=\"#FFFFFF\" )\n",
    "senha_usuario_lbl.grid(row=2, column=0, sticky=\"e\")\n",
    "\n",
    "#Criando um entry para o  campo nome de Usuario com a fonte arial tamanho 14\n",
    "nome_usuario_entry = Entry(janela_principal, font=\"Arial 14\")\n",
    "nome_usuario_entry.grid(row= 1, column= 1, pady=10)\n",
    "\n",
    "#Criando um entry para o  campo nome de Senhha com a fonte arial tamanho 14\n",
    "senha_usuario_entry = Entry(janela_principal, show= \"*\",font=\"Arial 14\")\n",
    "senha_usuario_entry.grid(row= 2, column= 1, pady=10)\n",
    "\n",
    "entrar_btn = Button(janela_principal, text=\"Entrar\", font=\"Arial 14\", command=verifica_credenciais)\n",
    "entrar_btn.grid(row=4, column=0, columnspan=2 , padx= 20, pady=10, stick=\"NSEW\")\n",
    "\n",
    "sair_btn = Button(janela_principal, text=\"Sair\", font=\"Arial 14\", command=janela_principal.destroy)\n",
    "sair_btn.grid(row=5, column=0, columnspan=2 , padx= 20, pady=10, stick=\"NSEW\")\n",
    "\n",
    "\n",
    "for i in  range(5):\n",
    "    janela_principal.grid_rowconfigure(i, weight=1)\n",
    "\n",
    "for i in range(2):\n",
    "    janela_principal.grid_columnconfigure(i, weight=1)\n",
    "\n",
    "\n",
    "#Inicia a janela tkinter \n",
    "janela_principal.mainloop()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
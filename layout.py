from tkinter import *

def get_salario():
    #Pega o salário
    salario = txt_salario.get()
    txt_salario.configure(state="disable") #desabilita escrever na caixa
    dias_no_mes = txt_dias_no_mes.get() #salva o valor
    txt_dias_no_mes.configure(state="disable") #desabilita escrever na outra caixa
    temp = float(salario)/float(dias_no_mes) #faz a divisão
    por_dia.set('{:.2f}'.format(temp))
    lbl_limite_valor = Label(janela, text=str(por_dia), bg='white', font=16)
    painel.insert(INSERT, "\n\nDados computados com sucesso!")
    
def get_saldo():
    #Pega o dia colocado na spinbox, multiplica pelo "limite diário" e diminui do gasto
    dia = spin_dia.get()
    diario = str(por_dia.get())
    entradas = int(dia) * float(diario)
    gasto = txt_gasto.get()
    entradas -= float(gasto)
    saldo.set("{:.2f}".format(entradas))
    
    
janela = Tk()
janela.title("Dia a Dia Financeiro")
janela.geometry('740x400')
janela.resizable(False,400)


#Váriaveis
por_dia = StringVar()
dias_no_mes = StringVar()
saldo = StringVar()
por_dia.set("0")
dias_no_mes.set("0")
saldo.set("0")

#Primeiro "Titulo" do programa

#Recebe a quantidade de dinheiro, salário
lbl_salario = Label(janela, text="Digite seu ganho mensal: R$", font=("Calibri",13),borderwidth=2,pady=10, padx=10)
lbl_salario.grid(column=0, row=0)
txt_salario = Entry(janela,width=10)
txt_salario.grid(column=1, row=0, ipady=3)


#Uma caixinha perguntando quantos dias faltam, o usuário insere o valor e ele é salvo
lbl_dias_no_mes = Label(janela, text='Quantos dias ainda faltam \naté o próximo salário?', font=("Calibri",13),borderwidth=2, padx=10)
lbl_dias_no_mes.grid(column=0,row=1)
txt_dias_no_mes = Entry(janela,width=10)
txt_dias_no_mes.grid(column=1, row=1, ipady=3)

#O botão computa o salário + quantos dias restam
btn_salario = Button(janela, text="Adicionar dados", command=get_salario, pady=5, bg="black", fg="white")
btn_salario.grid(column=0, row=3)

#Apresenta o quanto pode ser gasto por dia em uma caixinha
lbl_limite = Label(janela, text="Você pode gastar por dia: R$", font=('Calibri',13),borderwidth=2,padx=10)
lbl_limite.grid(column=0, row=4)
lbl_limite_valor = Label(janela, textvariable=por_dia, font=("Calibri",13))
lbl_limite_valor.grid(column=1, row=4)

#Dia atual do mês/período, podendo ser alterado pelo usuário
lbl_dias_corridos = Label(janela, text="Dias passados: ", font=('Calibri',13))
lbl_dias_corridos.grid(column=0, row=5)
spin_dia = Spinbox(janela, from_=0, to=31, width=5, font=13)
spin_dia.grid(column=1,row=5)

#Entry que pega o gasto
lbl_gasto = Label(janela, text="Gasto: R$", font=('Calibri',13),borderwidth=2, padx=10)
lbl_gasto.grid(column=0, row=6)
txt_gasto = Entry(janela,width=10)
txt_gasto.grid(column=1, row=6, ipady=3)

#Entry que pega a categoria do gasto
lbl_categoria = Label(janela, text="Categoria da despesa: ", font=('Calibri',13),borderwidth=2,padx=10)
lbl_categoria.grid(column=0, row=7)
txt_categoria = Entry(janela,width=10)
txt_categoria.grid(column=1, row=7, ipady=3)

#Botão de adicionar o gasto
btn_gasto = Button(janela, text="Computar", command=get_saldo, pady=5, bg="black", fg="white")
btn_gasto.grid(column=0, row=8)

#Apresenta o saldo atual, positivo ou negativo
lbl_saldo = Label(janela, text="Saldo: R$", font=('Calibri',13),borderwidth=2,padx=10)
lbl_saldo.grid(column=0, row=9)
lbl_saldo_valor = Label(janela, textvariable=saldo, font=("Calibri",13))
lbl_saldo_valor.grid(column=1, row=9)


#Painel de comunicação com o usuário
painel = Text(janela, width=50, borderwidth=2, relief="solid", wrap=WORD)
painel.grid(column=2, row=0,rowspan=12,pady=10, padx=20)
painel.insert(INSERT,"BEM VINDO AO DIA A DIA FINANCEIRO!"
                "\n========================================\n"
                "Comece inserindo o valor que você ganha mensalmente (ou de outra forma periódia)"
                " + o quanto de tempo você irá depender dele ================")
painel.tag_configure("center", justify="center")
painel.tag_add("center", "1.0", "end")


janela.mainloop()




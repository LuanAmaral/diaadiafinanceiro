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
    
def get_dia():
    #Pega o dia colocado na spinbox
    total = 0
        
    
    
janela = Tk()
janela.title("Dia a Dia Financeiro")
janela.geometry('380x400')
janela.resizable(False,400)
janela.configure(background="white")

#Váriaveis
por_dia = StringVar()
dias_no_mes = StringVar()
por_dia.set("0")
dias_no_mes.set("0")


#Recebe a quantidade de dinheiro, salário
lbl_salario = Label(janela, text="Digite seu ganho mensal: R$", font=("Calibri",16),bg='white',borderwidth=2,pady=10, padx=2)
lbl_salario.grid(column=0, row=0)
txt_salario = Entry(janela,width=10)
txt_salario.grid(column=1, row=0, ipady=3)


#Uma caixinha perguntando quantos dias faltam, o usuário insere o valor e ele é salvo
lbl_dias_no_mes = Label(janela, text='Quantos dias ainda faltam \naté o próximo salário?', font=("Calibri",16), bg='white',borderwidth=2,pady=10, padx=2)
lbl_dias_no_mes.grid(column=0,row=1)
txt_dias_no_mes = Entry(janela,width=10)
txt_dias_no_mes.grid(column=1, row=1, ipady=3)

#O botão computa o salário + quantos dias restam
btn_salario = Button(janela, text="Adicionar dados", command=get_salario, pady=5, bg="black", fg="white")
btn_salario.grid(column=0, row=3)

#Apresenta o quanto pode ser gasto por dia em uma caixinha
lbl_limite = Label(janela, text="Você pode gastar por dia: R$", font=('Calibri',16), bg='white',borderwidth=2,pady=10, padx=2)
lbl_limite.grid(column=0, row=4)
lbl_limite_valor = Label(janela, textvariable=por_dia, bg='white', font=("Calibri",16))
lbl_limite_valor.grid(column=1, row=4)

#Dia atual do mês/período, podendo ser alterado pelo usuário
lbl_dias_corridos = Label(janela, text="Dias passados: ", font=('Calibri',16), bg='white')
lbl_dias_corridos.grid(column=0, row=5)
spin_dia = Spinbox(janela, from_=0, to=31, width=5, font=16)
spin_dia.grid(column=1,row=5)

#Botão de adicionar o gasto

janela.mainloop()




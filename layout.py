from tkinter import *

def get_salario():
    salario = txt_salario.get()
    txt_salario.configure(state="disable")
    dias_no_mes = txt_dias_no_mes.get()
    txt_dias_no_mes.configure(state="disable")
    temp = float(salario)/float(dias_no_mes)
    por_dia.set('{:.2f}'.format(temp))
    lbl_limite_valor = Label(janela, text=str(por_dia), bg='white', font=16)
    
    
    
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

lbl_salario = Label(janela, text="Digite seu ganho mensal:", font=("Calibri",16),bg='white')
lbl_salario.grid(column=0, row=0)

txt_salario = Entry(janela,width=10)
txt_salario.grid(column=1, row=0, ipady=3)


#Uma caixinha perguntando quantos dias faltam, o usuário insere o valor e ele é salvo
lbl_dias_no_mes = Label(janela, text='Quantos dias ainda faltam \naté o próximo salário?', font=("Calibri",16), bg='white')
lbl_dias_no_mes.grid(column=0,row=1)
txt_dias_no_mes = Entry(janela,width=10)
txt_dias_no_mes.grid(column=1, row=1, ipady=3)

#O botão computa o salário + quantos dias restam
btn_salario = Button(janela, text="Salvar", command=get_salario)
btn_salario.grid(column=1, row=3)

#Apresenta o quanto pode ser gasto por dia em uma caixinha
lbl_limite = Label(janela, text="Você pode gastar por dia:", font=('Calibri',16), bg='white')
lbl_limite.grid(column=0, row=4)
lbl_limite_valor = Label(janela, textvariable=por_dia, bg='white', font=("Calibri",16))
lbl_limite_valor.grid(column=1, row=4)

janela.mainloop()




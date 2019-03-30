from tkinter import *

def get_salario():
    salario = txt_salario.get()
    txt_salario.configure(state="disable")
    temp = float(salario)/30
    por_dia.set('{:.2f}'.format(temp))
    lbl_limite_valor = Label(janela, text=str(por_dia), bg='white', font=16)
    
    

janela = Tk()
janela.title("Dia a Dia Financeiro")
janela.geometry('600x700')
janela.configure(background="white")

#Váriaveis
por_dia = StringVar()
por_dia.set("0")

lbl_salario = Label(janela, text="\tDigite seu ganho mensal:", font=("Calibri",16),bg='white')
lbl_salario.grid(column=0, row=0)

txt_salario = Entry(janela,width=10)
txt_salario.grid(column=1, row=0, ipady=3)
btn_salario = Button(janela, text="Salvar", command=get_salario)
btn_salario.grid(column=2, row=0)

lbl_limite = Label(janela, text="\tVocê pode gastar por dia:", font=('Calibri',16), bg='white')
lbl_limite.grid(column=0, row=1)
lbl_limite_valor = Label(janela, textvariable=por_dia, bg='white', font=("Calibri",16))
lbl_limite_valor.grid(column=1, row=1)

janela.mainloop()




from tkinter import *
from modula.abrir_arquivo.open_arquivo import *
from time import sleep


win = Tk()
win.geometry("312x324")
win.resizable(0, 0)
win.title("Calculator by Gusta")
arq = 'resultados.txt'
AbrirArquivo()
#tamanho do frame de resultado
frame_tela = Frame(win, width=312, height=50, bg="lightgray")
frame_tela.grid(row=0, column=0, columnspan=4)

# Entry para exibir os números/resultados
entrada_texto = Entry(win, font=("Arial", 18), justify=RIGHT, bd=2, relief=FLAT)
entrada_texto.grid(row=0, column=0, columnspan=4, ipady=10)  # ipady aumenta a altura da entrada
#----------- FUNÇÕES ---------
#numeros
def sete1():
    try:
        entrada_texto.insert(END,'7')
    except Exception as erro:
        print(f'Você tem um erro como o 8{erro}')
def oito():
    try:
        entrada_texto.insert(END,'8')
    except Exception as erro:
        print(f'Você tem um erro como o 8{erro}')
def nove():
    try:
        entrada_texto.insert(END,'9')
    except Exception as erro:
        print(f'Você tem um erro como o 9{erro}')
def quatro():
    try:
        entrada_texto.insert(END,'4')
    except Exception as erro:
        print(f'Você tem um erro como o 4{erro}')
def cinco():
    try:
        entrada_texto.insert(END,'5')
    except Exception as erro:
        print(f'Você tem um erro como o 5{erro}')
def seis():
    try:
        entrada_texto.insert(END,'6')
    except Exception as erro:
        print(f'Você tem um erro como o 6{erro}')
def um():
    try:
        entrada_texto.insert(END,'1')
    except Exception as erro:
        print(f'Você tem um erro como o 1{erro}')
def dois():
    try:
        entrada_texto.insert(END,'2')
    except Exception as erro:
        print(f'Você tem um erro como o 2{erro}')
def tres():
    try:
        entrada_texto.insert(END,'3')
    except Exception as erro:
        print(f'Você tem um erro como o 3{erro}')
def zero():
    try:
        entrada_texto.insert(END,'0')
    except Exception as erro:
        print(f'Você tem um erro como o 0{erro}')
#funções
def Ac_command ():
    try:
        entrada_texto.delete(0,END)
    except Exception as erro:
        print(f'Você tem um erro como o AC{erro}')
def parentes1():
    try:
        entrada_texto.insert(END,'(')
    except Exception as erro:
        print(f'Você tem um erro como o ({erro}')
def parentes2():
    try:
        entrada_texto.insert(END,')')
    except Exception as erro:
        print(f'Você tem um erro como o ){erro}')
def divisao():
    try:
        entrada_texto.insert(END,'/')
    except Exception as erro:
        print(f'Você tem um erro como o /{erro}')
def multiplica():
    try:
        entrada_texto.insert(END,'*')
    except Exception as erro:
        print(f'Você tem um erro como o *{erro}')
def menos():
    try:
        entrada_texto.insert(END,'-')
    except Exception as erro:
        print(f'Você tem um erro como o -{erro}')
def mais():
    try:
        entrada_texto.insert(END,'+')
    except Exception as erro:
        print(f'Você tem um erro como o +{erro}')
def ponto():
    try:
        entrada_texto.insert(END,'.')
    except Exception as erro:
        print(f'Você tem um erro como o AC{erro}')

def resultado():
    try:
        expressao = entrada_texto.get()
        resultado = eval(expressao)
        entrada_texto.delete(0, END)
        entrada_texto.insert(END, str(resultado))
        with open(arq,'a',encoding='utf-8') as file:
            file.write(f'{expressao} = {resultado}\n')

        
    except Exception as erro:
        entrada_texto.delete(0, END)
        entrada_texto.insert(END, "Erro")
        print(f'Ocorreu um erro: {erro}')
        sleep(1)
        
        return entrada_texto.delete(0,END), entrada_texto.insert(END, '0')

# ---------- BOTÕES ----------
# Linha 1
Button(win, text='AC', width=5, height=2,command=Ac_command).grid(row=1, column=0)
Button(win, text='(', width=5, height=2,command=parentes1).grid(row=1, column=1)
Button(win, text=')', width=5, height=2,command=parentes2).grid(row=1, column=2)
Button(win, text='/', width=5, height=2,command=divisao).grid(row=1, column=3)

# Linha 2
Button(win, text='7', width=5, height=2,command=sete1).grid(row=2, column=0)
Button(win, text='8', width=5, height=2,command=oito).grid(row=2, column=1)
Button(win, text='9', width=5, height=2,command=nove).grid(row=2, column=2)
Button(win, text='x', width=5, height=2,command=multiplica).grid(row=2, column=3)

# Linha 3
Button(win, text='4', width=5, height=2,command=quatro).grid(row=3, column=0)
Button(win, text='5', width=5, height=2,command=cinco).grid(row=3, column=1)
Button(win, text='6', width=5, height=2,command=seis).grid(row=3, column=2)
Button(win, text='-', width=5, height=2,command=menos).grid(row=3, column=3)

# Linha 4
Button(win, text='1', width=5, height=2,command=um).grid(row=4, column=0)
Button(win, text='2', width=5, height=2,command=dois).grid(row=4, column=1)
Button(win, text='3', width=5, height=2,command=tres).grid(row=4, column=2)
Button(win, text='+', width=5, height=2,command=mais).grid(row=4, column=3)

# Linha 5
Button(win, text='0', width=11, height=2,command=zero).grid(row=5, column=0, columnspan=2)  # ocupa 2 colunas
Button(win, text='.', width=5, height=2,command=ponto).grid(row=5, column=2)
Button(win, text='=', width=5, height=2,command=resultado).grid(row=5, column=3)

win.mainloop()


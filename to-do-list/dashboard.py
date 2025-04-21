from time import sleep
from modularização.adicionar import add,listtarefas,conclusao,remover
arq = 'tarefas.txt'

def CriarArquivo():
    try:
        with open(arq, 'a') as arquivo:
            pass  
    except Exception as erro:
        print(f'❌ Erro ao criar arquivo: {erro}')



def painel():
    sleep(1)
    opcoes = ['Adicionar Tarefas', 'Listar tarefas', 'Concluir tarefa','Remover tarefa','Sair'] 
    for c, item in enumerate(opcoes,1):
        print(f'{c} - {item}')


def options(opcoes):

    if opcoes == 1:
        sleep(1)
        add()
        

    elif opcoes == 2:
        sleep(1)
        listtarefas()    
    
    elif opcoes == 3:
        sleep(1)
        conclusao()

        
    elif opcoes == 4:
        sleep(1)
        remover()

    elif opcoes == 5:
        print('função saindo')
while True:

    CriarArquivo()
    painel()
    try:
         opcoes = int(input('Escolha a função que deseja:'))
         options(opcoes)
         if opcoes == 5:
             break
    except ValueError:
        print('\033[31mERRO: Digite um número inteiro válido.\033[m')
             







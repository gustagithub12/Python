from time import sleep
from modularizacao.sistema.funcao1 import newcadastre
from modularizacao.sistema.funcao2 import viewcadastre1, cadastrereal
from modularizacao.sistema.funcao3 import exitsystem1
from modularizacao.arquivo.arquivofuncional import arquivoExiste

arq= 'peoplecadastre.txt'
def CriarArquivo():
    try:
        with open(arq, 'w') as arquivo:
            arquivo.write('')  # Apaga tudo
            arquivo.close()

            print('Arquivo criado com sucesso.')
    except FileExistsError:
        print('Arquivo já existe.')

    except ValueError:
        print('O ARQUVIO NAO FUNFA')
CriarArquivo()
if arquivoExiste(arq):
    print('\033[31m Arquivo Existe.\033[m')

else:
    print('\033[31mERRO: Arquivo Não Existe.\033[m')

#titulo
def tittle():
    print('---'*15)
    print('MENU PRINCIPAL'.center(45))
    print('---'*15)
#painel funcão adicional com lista
def dashboard():
    sleep(2)
    opcoes = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema']
    for c, item in enumerate(opcoes, 1):
        print(f'{c} - {item}')
    print('---'*15)
#Crição do que acontecerá se cada valor for adicionado
def option(opcao):
    while True:

        try:
            if opcao == 1:
                sleep(1)
                newcadastre()#so mudou os nomes, acabei confundindo
               
                break
            elif opcao == 2:
                sleep(1)
                viewcadastre1()
                cadastrereal()
                break

            if opcao == 3:
                sleep(1)
                exitsystem1()
                
#Aqui se um número for digitado diferente de 1,2,3 a opção fica invalida
            elif opcao != 1 and 2 and 3:
                print('\033[31mERRO: Digite uma opção válida.\033[m')
                break
                
        except Exception as erro:
            print('\033[31mERRO: Digite uma opção válida.\033[m')
        except (ValueError,TypeError):
            print('\033[31mERRO: Digite um número inteiro válido.\033[m')
        

        

#tudo funcionando, inicio do programa

while True:
    tittle()
    dashboard()
    try:
        
        __option__ = int(input('Sua opção:'))
        option(__option__)
        if __option__ == 3:
            break
    except ValueError:
        print('\033[31mERRO: Digite um número inteiro válido.\033[m')



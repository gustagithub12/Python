from time import sleep
def viewcadastre1():
    print('---'*15)
    print('Opção 2'.center(45))
    print('---'*15)
    sleep(1)
    print('---'*15)
    print('Cadastre Pessoas'.center(45))
    print('---'*15)
    sleep(1)

def cadastrereal():
    arq = 'peoplecadastre.txt'
    while True:
        nome = str(input('Digite um nome:')).upper()

        try:
            idade = int(input('Digite sua idade:'))
        except ValueError:
             print('\033[31mDigite uma idade válida!\033[m')
             continue
        with open(arq, 'a', encoding='utf-8') as file:
            file.write(f'{nome};           {idade}  anos\n')

        cadastro1 = str(input('Você quer cadastrar outras pessoas? S/N:')).strip().upper()
        if cadastro1 == 'S':
            continue
        else:
            break




    

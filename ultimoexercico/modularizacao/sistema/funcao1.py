arq = 'peoplecadastre.txt'
def newcadastre():
    print('---' * 15)
    print('Opção 1'.center(45))
    print('---' * 15)

    try:
        with open(arq, 'r', encoding='utf-8') as file:
            print('\n--- Conteúdo do Arquivo ---')
            print(file.read())  
            print('--- Fim do Arquivo ---\n')
    except FileNotFoundError:
        print('\033[31mArquivo não encontrado.\033[m')

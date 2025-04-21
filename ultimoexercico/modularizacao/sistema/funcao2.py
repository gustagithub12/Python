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
        idade = int(input('Digite sua idade:'))
        

        try:
            while True:
                email = str(input('Digite seu e-mail:')).strip()
                if email.endswith("@gmail.com") and len(email)> len("@gmail.com"):
                    print("E-mail válido")
                    break
                else:
                    print('\033[31mDigite um e-mail válido!\033[m')
                  
                    
                    
                    
        except Exception as erro:
             print('\033[31mDigite uma idade válida!\033[m')
            


             
             
        
        with open(arq, 'a', encoding='utf-8') as file:
            file.write(f'{nome};           {idade}  anos;E-mail: {email}\n')

        cadastro1 = str(input('Você quer cadastrar outras pessoas? S/N:')).strip().upper()
        if cadastro1 == 'S':
            continue
        else:
            break


    


    

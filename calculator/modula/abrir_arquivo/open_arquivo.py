def AbrirArquivo():
    arq = 'resultados.txt'
    try:
        with open(arq, 'a') as arquivo:
            pass  
    except Exception as erro:
        print(f'❌ Erro ao criar arquivo: {erro}')

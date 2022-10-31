'''
Usando o arquivo texto notas_estudantes.txt escreva um programa
que imprime o nome dos alunos que têm mais de seis notas.

'''
def imprime_nome_alunos() -> str:
    arquivo = open('notas_estudantes.txt', 'r') 
    print('\nOs estudantes que tem mais de seis notas são:\n')
    for notas in arquivo:        
        x = notas.split()        
        if len(x) > 6:        
            print(f'Estudante: {x[0]}')
    arquivo.close()   

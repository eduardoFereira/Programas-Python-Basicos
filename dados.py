import random

again = True

def lance(dados, lados):
    sum = 0
    for i in range(dados):
        dado = random.randint(1, lados)
        sum += dado
        print(f'Dado {i+1} = {dado}')

    print(f'Total: {sum}')
    return 0


while again:

    dados = int(input('Quantos dados vai lançar? (default=2)' ) or 2)
    lados = int(input('Quantos lados tem os dados? (default=6) ') or 6)

    lance(dados, lados)

    denovo = input('Vai lançar de novo? (n = não) ').lower()
    if denovo == 'n':
        again = False


print('Até logo!')

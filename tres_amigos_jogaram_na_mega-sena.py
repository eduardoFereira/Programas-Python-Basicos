'''
Três amigos jogaram na mega-sena da virada. Caso eles ganhem, o prêmio deve ser
repartido proporcionalmente ao valor que cada deu para a realização ̧ao da aposta. Faça a um
programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um
ganharia do prêmio com base no valor investido (2 pontos).

'''
valor = []
nome = []
total = 0
for i in range(1, 4):
    amigo_nome = str(input(f'\n{i}-Digite seu nome: ')).title()
    amigo_valor = float(input(f'{i}-Digite o valor R$ '))
    nome.append(amigo_nome)
    valor.append(amigo_valor)    
    total += amigo_valor
    
valor_premio = float(input('\nDigite o valor do prêmio R$ '))
print(f'\n{nome[0]}, com o investimento de R${valor[0]:.2f}, o valor recebido do prêmio será R$ {(valor[0]/total)* valor_premio:.2f}.')
print(f'{nome[1]}, com o investimento de R${valor[1]:.2f}, o valor recebido do prêmio será R$ {(valor[1]/total)* valor_premio:.2f}.')
print(f'{nome[2]}, com o investimento de R${valor[2]:.2f}, o valor recebido do prêmio será R$ {(valor[2]/total)* valor_premio:.2f}.')

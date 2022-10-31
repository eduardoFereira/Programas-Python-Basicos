'''
Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é:´ C = P ∗ 2, 54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
'''
print("****************************************************")
print('******Conversor de polegadas para centímetros*******')
print("****************************************************")


p = float(input(" Digite um valor em polegadas: "))
c = float('%.2f' %(p * 2.54))
print("O valor do comprimento em centímetros é {}".format(c))


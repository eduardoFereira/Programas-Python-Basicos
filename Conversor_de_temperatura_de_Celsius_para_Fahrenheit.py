'''
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A formula de conversão e: F = C ∗(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
'''
print("****************************************************")
print('Conversor de temperatura de Celsius para Fahrenheit!')
print("****************************************************")


c = float(input(" Digite a temperatura em graus Celsius: "))
d = (c *((9.0/5.0) + 32.0))
e = ('%.1f' %(d))
print("A temperatura em Fahrenhit é {}F".format(e))

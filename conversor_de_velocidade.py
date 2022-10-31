"""
Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s ˆ
(metros por segundo). A formula de conversão e:  M = K/3.6, sendo K a velocidade em
km/h e M em m/s
"""

print("****************************************************")
print('******Conversor de velocidade km/h para m/s ********')
print("****************************************************")


k = float(input(" Digite a velocidade em km/h: "))
m = float(('%.2f' %(k/3.6)))
print("A velocidade é {} m/s".format(m))


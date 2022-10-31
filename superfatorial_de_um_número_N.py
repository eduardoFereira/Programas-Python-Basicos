'''
Faça uma função não-recursiva que receba um número inteiro positivo N e retorne o
superfatorial desse número. O superfatorial de um número N é definida pelo produto dos N
primeiros fatoriais de N. Assim, o superfatorial de 4 e sf(4) = 1! * 2! * 3! * 4! = 288
            
'''
def superfatorial(n):
    total = 1
    if n >= 0: 
        for i in range(n -1, 1, -1):
            i = 1
            for i in range(n , 1, -1):
                total = total * i            
        return total

# Exercicio 4
import math
 
a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))
 
delta = ( (b * b) - (4 * (a * c)) )
 
if delta < 0:
    print (f"A equação não possui raizes reais")
elif delta == 0:
    raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
    print (f"A raiz da equação é: ",raiz)
else:
    raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-1 * b - math.sqrt(delta)) / (2 * a)   
    print (f"As raizes são",raiz1," e ",raiz2)
# Exercicio5

import math
def calc(r):
    peri=2*math.pi*r
    area=math.pi*r**2
    return peri, area

print("Para achar o perimetro e a area de um circulo")
r=float(input('Digite o Raio: '))
a,b=calc(r)
print("Perimetro :",round(a,2))
print("Area: ",round(b,2))
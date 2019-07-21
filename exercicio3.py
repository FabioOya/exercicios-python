# Exercicio 3
import random as r
lista = []
listaImpar = []
listaPar = []
n = 0

while n<10:
    lista.append(r.randint(1, 100))
    if lista[n]%2 == 0:
        listaPar.append(lista[n])

    else:
        listaImpar.append(lista[n])
    n +=1

print('Essa é a lista gerada aleatóriamente: '+str(lista))
print('Numeros pares: '+str(listaPar))
print('Numeros impares: '+str(listaImpar))
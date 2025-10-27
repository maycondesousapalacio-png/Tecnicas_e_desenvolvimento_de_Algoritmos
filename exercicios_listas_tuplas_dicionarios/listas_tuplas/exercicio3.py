# Escreva um programa que apaga todos os
# elementos negativos de uma lista.

lista=[1,2,3,4,5,-5,-4,-3,-2,-1,0]
x=0
while x<len(lista):
    if lista[x]<0:
        del lista[x]
        continue
    x+=1
print(lista)
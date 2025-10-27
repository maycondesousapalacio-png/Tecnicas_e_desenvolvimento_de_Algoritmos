# Escreva um programa que aplica a função
# módulo a todos os elementos e uma lista.

lista=[1,2,3,4,5,-5,-4,-3,-2,-1,0]
lista2=[]
print("Lista sem módulo: ")
print(lista)

def modulo(list,list2):
    for x in list:
        num=abs(x)
        list2.append(num)

modulo(lista,lista2)
print("Lista sem módulo: ")
print(lista2)


# Escreva um programa que solicita que o
# usuário digite 5 números inteiros e os coloca
# em uma lista.
# Quando terminar, imprima a lista.
lista=[]
for x in range(1,6):
    print("Informe o ",x,"º número: ")
    num=int(input())
    lista.append(num)
print(lista)

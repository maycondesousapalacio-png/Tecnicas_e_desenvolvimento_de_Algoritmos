# Faça um programa que solicita uma
# quantidade indefinida de números positivos
# (deve parar quando um número negativo for
# digitado).
# Armazene todos os números digitados em
# uma lista, sem repetição.

numeros=[]
digitados=0

print("Informe números positivos.")
print("O comando de parada é qualquer número negativo.")
while True:
    try:
        print("Informe um número: ")
        num=int(input())

        if num<0:
            break
        if num not in numeros:
            numeros.append(num)
        
    except ValueError:
        print("Informe números...")

print(numeros)
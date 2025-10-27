# Faça um programa que solicita uma
# quantidade indefinida de números positivos
# (deve parar quando um número negativo for
# digitado).
# Armazene-os em duas listas:
# uma para os números pares;
# outra para os números ímpares.
# A seguir, mostre a porcentagem de pares e
# ímpares digitados.

impares=[]
pares=[]
digitados=0

print("Informe números positivos.")
print("O comando de parada é qualquer número negativo.")
while True:
    try:
        print("Informe um número: ")
        num=int(input())

        if num<0:
            break
        elif num%2==0:
            pares.append(num)
            digitados+=1
        elif num%2==1:
            impares.append(num)
            digitados+=1
        
    except ValueError:
        print("Informe números...")

porcentagem_pares=(len(pares)*100)/digitados
porcentagem_impares=100-porcentagem_pares

print("A porcentagem de números pares digitados é ",porcentagem_pares,"%")
print("A porcentagem de números ímpares digitados é ",porcentagem_impares,"%")
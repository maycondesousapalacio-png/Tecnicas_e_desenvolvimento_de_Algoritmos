# Faça um programa que leia um número n e imprima n linhas na tela
# com o seguinte formato (exemplo se n = 5):

num=int(input("Informe um número: "))

lista=[]
for x in range(1,num+1,1):
    lista.append(x)
    for y in lista:
        print(f'{y}',end=' ')
    print()
    
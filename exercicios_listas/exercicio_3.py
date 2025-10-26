lista1=[]
lista2=[]
valores_iguais=[]

def inserir(list):
    for x in range(1,6):
        print("Informe o ",x,"º número: ")
        num=int(input())
        list.append(num)

def iguais(list,list2):
    for x in list:
        if x in list2:
            valores_iguais.append(x)


print("Informe os valores da primeira lista")
inserir(lista1)
print("Informe os valores da segunda lista")
inserir(lista2)

iguais(lista1,lista2)

if len(valores_iguais)==0:
    print("Não tem")
else:
    print(valores_iguais)


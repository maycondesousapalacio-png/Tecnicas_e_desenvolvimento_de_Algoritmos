# Escreva um programa que solicita que o
# usuário digite a altura e o peso de 5 pessoas.
# Verifique se pelo menos duas das pessoas
# tem a mesma altura e mesmo peso.

alturas=[]
pesos=[]
iguais_pesos=[]
iguais_alturas=[]
print("Informe a altura e o peso de 5 pessoas")
for x in range(1,6):
    print("Informe a altura da ",x,"ª pessoa: ")
    altura=float(input())
    alturas.append(altura)
    print("Informe o peso da ",x,"ª pessoa: ")
    peso=float(input())
    pesos.append(peso)

def contador(list,pos_iguais):
    for x in range(0,len(list)):
        iguais=0
        for y in range(x,len(list)):
            if list[x]==list[y]:
                iguais+=1
            if iguais>1:
                pos_iguais.append((x,y))


        

contador(pesos,iguais_pesos)
contador(alturas,iguais_alturas)

for x in iguais_alturas:
    if x in iguais_alturas:
        print("Há pelo menos duas pessoas com o mesmo peso e mesma altura.")
        break
if iguais_pesos==[]:
    print("Não há pelo menos duas pessoas com o mesmo peso e mesma altura")

print(pesos,"-",iguais_pesos)
print(alturas,"-",iguais_alturas)

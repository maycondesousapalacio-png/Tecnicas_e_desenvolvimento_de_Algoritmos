# Faça um programa que solicita que o
# usuário digite o nome e a idade de diversas
# pessoas (o programa deve parar quando
# um nome vazio for informado).
# Retorne o nome da pessoa mais velha.


nomes=[]
idades=[]
idade_mais_velho=index_mais_velho=0
print("Informe nome e idade de quantas pessoas quiser")
print("Para finalizar o programa aperte Enter sem informar um nome")

x=1
while True:
    print("Informe o nome da ",x,"ª pessoa: ")
    nome=(input())

    if nome=='':
        break

    nomes.append(nome)
    print("Informe a idade da ",x,"ª pessoa: ")
    idade=int(input())
    idades.append(idade)
    x+=1

for x in range(0,len(idades)):
    if idades[x]>idade_mais_velho:
        idade_mais_velho=(idade_mais_velho - idade_mais_velho)+idades[x]
        index_mais_velho=(index_mais_velho-index_mais_velho)+x

print("A pessoa mais velha é ",nomes[index_mais_velho]," com ",idade_mais_velho," anos de idade.")



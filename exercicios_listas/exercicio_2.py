# Faça um programa que leia n notas, mostre as notas e a média.

notas=[]
parada=['P','p','Parar','parar','PARAR','PARA','para']
soma_notas=0
i=1

while True:
    print(f"Informe a {i}ª nota (o comando de parada é Parar): ")
    nota=input()

    if nota in parada:
        break
    elif nota.isalpha():
        print("Informe notas ou o comando para parar...")
        continue
    
    nota=float(nota)
    notas.append(nota)
    i+=1

for x in notas:
    soma_notas+=x
media=soma_notas/len(notas)

print(f'Suas notas são: {notas}')
print(f"A sua media é {media:.2f}")
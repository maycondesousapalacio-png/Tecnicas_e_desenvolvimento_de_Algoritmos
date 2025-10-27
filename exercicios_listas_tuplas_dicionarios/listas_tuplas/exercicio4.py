# Faça um programa que solicita uma
# quantidade indefinida de notas de uma
# prova (deve parar quando um número
# negativo for digitado).
# Armazena em uma lista.
# Após isso, o programa deve mostrar a média
# das notas.
notas=[]
x=1
print("Informe suas notas para obter sua média.")
print("O comando de parada é qualquer número negativo.")
while True:
    try:
        print("Informe a ",x,"ª nota: ")
        nota=float(input())

        if nota<0:
            break
        
        notas.append(nota)
        x+=1
    except ValueError:
        print("Informe números...")

media=sum(notas)/len(notas)
print(f'Sua média é: {media}')
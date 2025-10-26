# Solicite ao usuário três notas e seus respectivos pesos, depois calcule e exiba a média ponderada.

nota1=float(input("Digite sua primeira nota: "))
peso1=float(input("Digite o peso da primeira nota: "))
nota2=float(input("Digite sua segunda nota: "))
peso2=float(input("Digite o peso da segunda nota: "))
nota3=float(input("Digite sua terceira nota: "))
peso3=float(input("Digite o peso da terceira nota: "))

media=((nota1*peso1)+(nota2*peso2)+(nota3*peso3))/(peso1+peso2+peso3)

print(f"A media ponderada é: {media:.2f}")
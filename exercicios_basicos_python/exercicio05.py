# Solicite que o usuário digite seu nome e sua idade.
# Imprima “Olá, nome! Você tem idade anos?”
# Imprima o ano de nascimento da pessoa (ignore meses e dias)
# Imprima o nome da pessoa idade vezes (João tem 18, imprime JoãoJoão...)

nome=input("Digite o se nome: ")
idade=input("Digite sua idade: ")

print(f"Olá {nome}, voce tem {idade} anos ?")

from datetime import datetime

ano_atual=datetime.now().year

nascimento=ano_atual-int(idade)

print(f"Voce nasceu em {nascimento}")
print(f"{nome}\n"*int(idade))
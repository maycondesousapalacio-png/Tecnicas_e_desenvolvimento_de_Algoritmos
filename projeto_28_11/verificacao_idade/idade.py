
def verificar_idade():
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        print("Idade inválida.")
    elif idade < 18:
        print("Acesso negado: permitido apenas para maiores de 18.")
    elif idade < 60:
        print("Acesso liberado: nível padrão.")
    else:
        print("Acesso liberado: nível especial para idosos.")

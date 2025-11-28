
def cadastrar_alunos():
    alunos = []
    while True:
        nome = input("Nome do aluno (ou 'sair'): ")
        if nome.lower() == "sair":
            break
        alunos.append(nome)

    print("\nAlunos cadastrados:")
    for a in alunos:
        print("-", a)

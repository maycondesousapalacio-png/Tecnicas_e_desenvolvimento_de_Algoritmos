
from verificacao_idade.idade import verificar_idade
from analise_numeros.pares import mostrar_pares
from cadastro_alunos.alunos import cadastrar_alunos
from cadastro_produtos.produtos import cadastrar_produtos

def menu():
    while True:
        print("\n=== SISTEMA DE GESTÃO BÁSICA ===")
        print("1 - Verificação de Idade")
        print("2 - Análise de Números Pares")
        print("3 - Cadastro de Alunos")
        print("4 - Cadastro de Produtos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            verificar_idade()
        elif opcao == "2":
            mostrar_pares()
        elif opcao == "3":
            cadastrar_alunos()
        elif opcao == "4":
            cadastrar_produtos()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()

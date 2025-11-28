
def cadastrar_produtos():
    produtos = {}
    while True:
        nome = input("Nome do produto (ou 'sair'): ")
        if nome.lower() == "sair":
            break
        preco = float(input("Preço: R$ "))
        produtos[nome] = preco

    print("\nProdutos cadastrados:")
    for nome, preco in produtos.items():
        print(f"- {nome}: R$ {preco:.2f}")

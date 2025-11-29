# Sistema de Gerenciamento de Biblioteca

# Lista para armazenar os livros
biblioteca = []

# Dicionário para categorias de livros
categorias = {
    "1": "Ficção",
    "2": "Não-Ficção", 
    "3": "Técnico",
    "4": "Romance",
    "5": "Fantasia"
}

def menu_principal():
    """Exibe o menu principal do sistema"""
    print("\n" + "="*50)
    print("       SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
    print("="*50)
    print("1. Adicionar livro")
    print("2. Listar todos os livros")
    print("3. Buscar livro por título")
    print("4. Listar livros por categoria")
    print("5. Estatísticas da biblioteca")
    print("6. Sair")
    print("="*50)

def adicionar_livro():
    """Adiciona um novo livro à biblioteca"""
    print("\n--- ADICIONAR NOVO LIVRO ---")
    
    # Estruturas condicionais para validação
    titulo = input("Título do livro: ")
    if not titulo:
        print("Erro: Título não pode estar vazio!")
        return
    
    autor = input("Autor: ")
    if not autor:
        print("Erro: Autor não pode estar vazio!")
        return
    
    # Exibir categorias disponíveis
    print("\nCategorias disponíveis:")
    for codigo, nome in categorias.items():
        print(f"{codigo}. {nome}")
    
    # Estrutura de repetição para validação da categoria
    while True:
        categoria_codigo = input("\nDigite o número da categoria: ")
        if categoria_codigo in categorias:
            categoria = categorias[categoria_codigo]
            break
        else:
            print("Categoria inválida! Tente novamente.")
    
    # Validação do ano com estrutura condicional
    while True:
        try:
            ano = int(input("Ano de publicação: "))
            if ano > 2024 or ano < 1000:
                print("Ano inválido! Digite um ano entre 1000 e 2024.")
            else:
                break
        except ValueError:
            print("Erro: Digite um número válido para o ano!")
    
    # Criar dicionário do livro
    livro = {
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "ano": ano,
        "disponivel": True
    }
    
    # Adicionar à lista
    biblioteca.append(livro)
    print(f"\n✅ Livro '{titulo}' adicionado com sucesso!")

def listar_livros():
    """Lista todos os livros da biblioteca"""
    print("\n--- TODOS OS LIVROS ---")
    
    # Estrutura condicional para verificar se há livros
    if not biblioteca:
        print("Nenhum livro cadastrado na biblioteca.")
        return
    
    # Estrutura de repetição para percorrer a lista
    for i, livro in enumerate(biblioteca, 1):
        status = "✅ Disponível" if livro["disponivel"] else "❌ Emprestado"
        print(f"{i}. '{livro['titulo']}' - {livro['autor']} ({livro['ano']})")
        print(f"   Categoria: {livro['categoria']} | Status: {status}")
        print()

def buscar_livro():
    """Busca livros por título"""
    print("\n--- BUSCAR LIVRO ---")
    termo = input("Digite o título ou parte do título: ").lower()
    
    livros_encontrados = []
    
    # Estrutura de repetição com condicional para busca
    for livro in biblioteca:
        if termo in livro["titulo"].lower():
            livros_encontrados.append(livro)
    
    # Estrutura condicional para verificar resultados
    if livros_encontrados:
        print(f"\n📚 {len(livros_encontrados)} livro(s) encontrado(s):")
        for i, livro in enumerate(livros_encontrados, 1):
            status = "✅ Disponível" if livro["disponivel"] else "❌ Emprestado"
            print(f"{i}. '{livro['titulo']}' - {livro['autor']} | {status}")
    else:
        print("Nenhum livro encontrado com esse título.")

def listar_por_categoria():
    """Lista livros por categoria"""
    print("\n--- LIVROS POR CATEGORIA ---")
    
    # Exibir categorias
    for codigo, nome in categorias.items():
        print(f"{codigo}. {nome}")
    
    categoria_codigo = input("\nDigite o número da categoria: ")
    
    # Estrutura condicional para validar categoria
    if categoria_codigo not in categorias:
        print("Categoria inválida!")
        return
    
    categoria_selecionada = categorias[categoria_codigo]
    livros_categoria = []
    
    # Buscar livros da categoria selecionada
    for livro in biblioteca:
        if livro["categoria"] == categoria_selecionada:
            livros_categoria.append(livro)
    
    # Estrutura condicional para verificar resultados
    if livros_categoria:
        print(f"\n📚 Livros na categoria '{categoria_selecionada}':")
        for i, livro in enumerate(livros_categoria, 1):
            status = "✅ Disponível" if livro["disponivel"] else "❌ Emprestado"
            print(f"{i}. '{livro['titulo']}' - {livro['autor']} ({livro['ano']}) | {status}")
    else:
        print(f"Nenhum livro encontrado na categoria '{categoria_selecionada}'.")

def estatisticas():
    """Exibe estatísticas da biblioteca"""
    print("\n--- ESTATÍSTICAS DA BIBLIOTECA ---")
    
    # Estrutura condicional para biblioteca vazia
    if not biblioteca:
        print("Biblioteca vazia!")
        return
    
    total_livros = len(biblioteca)
    livros_disponiveis = sum(1 for livro in biblioteca if livro["disponivel"])
    livros_emprestados = total_livros - livros_disponiveis
    
    # Contar livros por categoria usando dicionário
    livros_por_categoria = {}
    for livro in biblioteca:
        categoria = livro["categoria"]
        if categoria in livros_por_categoria:
            livros_por_categoria[categoria] += 1
        else:
            livros_por_categoria[categoria] = 1
    
    print(f"📊 Total de livros: {total_livros}")
    print(f"✅ Livros disponíveis: {livros_disponiveis}")
    print(f"❌ Livros emprestados: {livros_emprestados}")
    
    print("\n📚 Livros por categoria:")
    for categoria, quantidade in livros_por_categoria.items():
        porcentagem = (quantidade / total_livros) * 100
        print(f"   {categoria}: {quantidade} livro(s) ({porcentagem:.1f}%)")

# Programa principal
def main():
    """Função principal do programa"""
    print("Bem-vindo ao Sistema de Gerenciamento de Biblioteca!")
    
    # Estrutura de repetição principal
    while True:
        menu_principal()
        
        opcao = input("\nDigite a opção desejada: ")
        
        # Estruturas condicionais para menu
        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_livro()
        elif opcao == "4":
            listar_por_categoria()
        elif opcao == "5":
            estatisticas()
        elif opcao == "6":
            print("\nObrigado por usar nosso sistema! Até logo! 👋")
            break
        else:
            print("Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

# Executar o programa
if __name__ == "__main__":
    main()
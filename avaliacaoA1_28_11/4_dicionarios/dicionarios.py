'''Desenvolver um sistema simples de cadastro de produtos com nome e preço, armazenando em dicionário.'''

produtos = {} #criando um dicionário vazio

while True:
    try:
        produto=input('Informe o nome do produto: ')     #entrada de dados
        valor=float(input("Informe o preço do produto: "))

        if produto=='':    #verifica se foi digitado um produto
            print('O nome do produto não pode ser vazio.')
            continue

        produtos[produto]=valor     #armazena os dados no dicionário

        for item,preco in produtos.items():    #exibe os itens armazenados com seus respectivos preços
            print('Nome do produto: ',item,' --- Preço: ',preco)

    except ValueError:   #tratamento de erro caso o valor do preço seja inválido
        print('Preço inválido, digite apenas números e ponto para valores decimais')
    
    else:   #verifica se o usuário deseja adicionar mais um produto
        res=input('Deseja adicionar mais algum produto? (s/n): ').lower()
        if res=='n' or res == 'nao' or res=='não':
            break

print('Programa finalizado.')
'''Criar um programa que receba nomes de alunos e armazene em uma lista, permitindo exibir todos os nomes ao final.'''

alunos = []   #criação de uma lista vazia

while True:   #executando um laço de repetição
    print('Informe o nome do(a) aluno(a): ')
    nome=input()   #coleta de dados

    if any(char.isdigit() for char in nome):    #verificando se há números no nome
        print('Nome inválido, contém número(s).')
        continue
    elif nome=='':    #verificando se o nome foi digitado
        print('É necessário digitar um nome.')
        continue
    else:
        alunos.append(nome)

    print('Aluno adicionado com sucesso. Deseja continuar? (s/n)')   #verificando se o usuário deseja informar outro aluno
    res=input().lower()
    if res=='n' or res== 'nao' or res=='não':     #condição de parada do laço de repetição
        break

alunos.sort()    #ordenação da lista em ordem alfabética
for i,aluno in enumerate(alunos):    #laço de repetição para exibição dos itens(nomes dos alunos) da lista
    print(i,'- ',aluno)
'''Criar um programa em Python que simule um sistema de verificação de idade para entrada em eventos.'''

print('Informe a idade do participante: ')
idade=input()        #coleta de dados (input)

if idade.isalpha():    #tratamento de erros
    print('Valor digitado inválido, informe apenas números.')
else:
    idade=int(idade)    #operação de casting para verificação da idade informada

    if idade<18:    #estrutura condicional para verificação de idade 
        print('O participante não tem idade necessária para entrar no evento.')
    elif idade>=18:     #estrutura condicional para verificação de idade
        print('Entrada permitida.')

print('Programa finalizado.')     #final do programa
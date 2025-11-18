'''Desenvolver um contador de 1 a 100 com for e outro com while, exibindo apenas números pares.'''

for x in range(1,101):   #cria um laço de repetição que executa 100 vezes
    if x % 2 == 0:   #estrutura condicional para verificar se o número é par
        print(x)    #output

i=1    #inicialização da variável de controle do laço while
while i<=100:     #estrutura de repetição e condição de parada
    if i % 2 == 0:   #estrutura condicional para verificar se o número é par
        print(i)   #output
    i+=1    #controle da variável de controle
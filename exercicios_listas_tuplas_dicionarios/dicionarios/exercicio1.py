#Dado o dicionário:
alunos = {
"Alice": 8.5,
"Bruno": 7.8,
"Carla": 9.2,
"Diego": 6.9,
"Eva": 8.0,
"Fernando": 7.5,
"Gabriela": 9.0,
"Henrique": 6.7,
"Isabela": 8.3,
"João": 7.2
}
#imprima os seguintes dados:
# Quantos alunos existem?
# Alguém tirou nota zero?
# Qual foi a menor nota?
# Qual foi a maior nota?

print("Na lista tem ",len(alunos)," alunos")

notas_zero=False
for x in alunos.items():
    if 0 in x:
        notas_zero=True

if notas_zero:
    print("Sim, alguém tirou nota zero")
else:
    print("Ninguém tirou nota zero")

def buscar_aluno_por_nota(nota_procurada):
    for nome,nota in alunos.items():
        if nota == nota_procurada:
            return nome
    return None

print("A menor nota foi ",min(alunos.values())," do(a) aluno(a) ", buscar_aluno_por_nota(min(alunos.values())))
print("A maior nota foi ",max(alunos.values())," do(a) aluno(a) ", buscar_aluno_por_nota(max(alunos.values())))

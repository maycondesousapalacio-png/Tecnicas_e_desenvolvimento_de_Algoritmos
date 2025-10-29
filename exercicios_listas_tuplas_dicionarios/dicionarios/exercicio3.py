# Dado o dicionário:
bandas = {
"Gangrena Gasosa": [
{"álbum": "Gente Ruim Só Manda Lembrança Pra Quem Não Presta", "ano":
2019},
{"álbum": "Se Deus É 10, Satanás É 666", "ano": 1999},
{"álbum": "Welcome to the Macumba", "ano": 1993}
],
"Rogério Skylab": [
{"álbum": "Nas Portas do Cu", "ano": 2023},
{"álbum": "Crítica da Faculdade do Cu", "ano": 2021},
{"álbum": "Cosmos", "ano": 2019}
],
"Garotos Podres": [
{"álbum": "Canções para Ninar", "ano": 2003},
{"álbum": "Com a Corda Toda", "ano": 1997},
{"álbum": "Rock de Subúrbio", "ano": 1995}
],
"Massacration": [
{"álbum": "Live Metal Espancation", "ano": 2017},
{"álbum": "Good Blood Headbanguers", "ano": 2009},
{"álbum": "Gates of Metal Fried Chicken of Death", "ano": 2005}
],
"Raimundos": [
{"álbum": "Cantigas de Roda", "ano": 2014},
{"álbum": "Roda Viva", "ano": 2006},
{"álbum": "Éramos 4", "ano": 2001}
]
}
# Imprima o álbum mais antigo
# imprima a banda que tem o maior
# intervalo entre os álbuns
# Imprima todos os álbuns do mais novo
# para o mais antigo, dizendo também o
# nome da banda

albuns=[]

ano_mais_velha=3000
for banda,lista_albuns in bandas.items():
    for albuns in lista_albuns:
        if albuns['ano'] < ano_mais_velha:
            ano_mais_velha = albuns['ano']
            album_mais_velho=albuns['álbum']
            banda_mais_antiga=banda


print("O álbum mais antigo é: ",album_mais_velho," do ano de ",ano_mais_velha," da banda ",banda_mais_antiga)
diferenca={}
for banda,lista_albuns in bandas.items():
    diferenca[banda]=(lista_albuns[0]['ano']-lista_albuns[1]['ano'])+(lista_albuns[1]['ano']-lista_albuns[2]['ano'])

diferenca_procurada=max(diferenca.values())
def encontrar_banda_com_diferenca_maior(anos_entre_albuns):
    for banda,anos_entre_albuns in diferenca.items():
        if anos_entre_albuns == diferenca_procurada:
            return banda
    
print('A banda com maior diferença entre álbuns é: ',encontrar_banda_com_diferenca_maior(diferenca_procurada),' com ',diferenca_procurada,' anos de diferença somados entre os intervalos de um álbum para o outro.')


albuns_maisnovo_maisantigo={}
for banda,lista_albuns in bandas.items():
    for album in lista_albuns:
        albuns_maisnovo_maisantigo[album['álbum']]=album['ano']

albuns_maisnovo_maisantigo_ordenada=sorted(albuns_maisnovo_maisantigo.items(), key=lambda x: x[1], reverse=True)

for x in albuns_maisnovo_maisantigo_ordenada:
    for banda,lista_albuns in bandas.items():
        for album in lista_albuns:
            if x[0] == album["álbum"]:
                print(banda,x[0],x[1])
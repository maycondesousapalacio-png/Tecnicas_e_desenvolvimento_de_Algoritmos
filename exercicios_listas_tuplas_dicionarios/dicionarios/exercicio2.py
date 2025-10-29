# Dado o dicionário:
animes = { 
"Naruto": 220,
"Jujutsu Kaisen": 47, 
"Dragon Ball Z": 291,
"Death Note": 37,
"Fullmetal Alchemist": 64,
"Evangelion": 26,
"Berserk": 25,
"Code Geass": 50, 
"Akame ga Kill!": 24, 
"Elfen Lied": 13
}

# Imprima o total de episódios
# Substitua a quantidade de episódios pelo
# percentual (ep_anime/ep_total)
# Imprima nome e percentual de cada
# anime, em ordem decrescente de
# percentual
import copy

total_episodios=sum(animes.values())
print("Total de episódios: ", total_episodios)

animes_percentual={}
for anime,episodios in animes.items():
    animes_percentual[anime]=(episodios/total_episodios)*100
animes.clear()
animes=copy.deepcopy(animes_percentual)


ordenado = sorted(animes.items(), key=lambda x: x[1], reverse=True)

print(ordenado)
for anime, percent in ordenado:
    print(f'Anime: {anime}  |||  Percentual de episódios: {percent: .2f}')
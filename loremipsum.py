import random

polska_abeceda = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']
polske_sprezky = ['sz', 'rz', 'ch', 'sz', 'dż', 'dź']


#pravděpodobnost výběru písmen
pravdepodobnosti_pismen = [0.1, 0.05, 0.08, 0.07, 0.03, 0.12, 0.1, 0.05, 0.06, 0.03, 0.02, 0.09, 0.05, 0.07, 0.04, 0.02, 0.09, 0.08, 0.03, 0.1, 0.04, 0.09, 0.08, 0.02, 0.04, 0.07, 0.05, 0.1, 0.04, 0.05, 0.06, 0.03]

#pravděpodobnost výběru spřežek
pravdepodobnosti_sprezek = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

#možnost vybrat si počet vygenerovaných slov
x = int(input("Kolik si přeješ vygenerovat slov? "))


#seznam slov který se na konci vygeneruje
text = []
for i in range(x):
    

    #výběr náhodných písmen z abecedy s určitou pravděpodobností
    vyber_z_abecedy = random.choices(polska_abeceda, weights=pravdepodobnosti_pismen, k=random.randint(2, 10))

    #výběr náhodných spřežek z listu s určitou pravděpodobností
    vyber_z_prezek = random.choices(polske_sprezky, weights=pravdepodobnosti_sprezek, k=1)
    


    #vytvoření slova končící spřežkou
    slovo = vyber_z_abecedy + vyber_z_prezek
    
    #vytvoření slova se spřežkou na začátku
    slovo_naopak = vyber_z_prezek + vyber_z_abecedy


    #všechna možná slova s náhodným generováním
    slova = [slovo, vyber_z_abecedy, slovo_naopak]
    pravdepodobnosti_slova = random.choice(slova)

    #utvoří z listu slovo bez mezer
    finalni_slovo = "".join(pravdepodobnosti_slova)

    #přidá slovo do seznamu
    text.append(finalni_slovo)
    
#tečka za větou a přidání za text
tecka = "."
text.append(tecka)


#vytvoří text ze seznamu slov s mezerou mezi slovy
finalni_text = " ".join(text)

print(finalni_text)



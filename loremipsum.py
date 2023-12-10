import random

polska_abeceda = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'w', 'x', 'y', 'z', 'ź', 'ż']
polske_sprezky = ['sz', 'rz', 'ch', 'sz', 'dż', 'dź']

carka  = [",", "", "", "", ""]
tecka_na_konci_vety = [".", "", "", "", ""]

odstavec = ["\n\n ", "", "", "", "", "", "", ""]

#pravděpodobnost výběru písmen
pravdepodobnosti_pismen = [8.91, 0.99, 1.47, 3.96, 0.40, 3.25, 7.66, 1.11, 0.30, 1.42, 1.08, 8.21, 1.49, 2.80, 2.85, 3.13, 2.25, 5.52, 0.20, 6.50, 0.15, 5.53, 0.02, 4.69, 5.91, 3.13, 2.86, 0.20, 1.46, 1.13, 3.67, 0.00, 0.69, 1.49]

#pravděpodobnost výběru spřežek
pravdepodobnosti_sprezek = [10, 10, 10, 10, 2, 2]

#pravděpodobnost čárky
pravdepodobnost_carky = [0.2, 0.2, 0.2, 0.2, 0.2]

#pravděpodobnost tečky v textu
pravdepodobnost_tecky_v_textu = [0.25, 0.2, 0.2, 0.2, 0.2]

#pravděpodobnost odstavce
pravdepodobnost_odstavce = [0.1, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9]

#možnost vybrat si počet vygenerovaných slov
x = int(input("Kolik si přeješ vygenerovat slov? "))


#seznam slov který se na konci vygeneruje
text = []
for i in range(x):
    

    #výběr náhodných písmen z abecedy s určitou pravděpodobností
    vyber_z_abecedy = random.choices(polska_abeceda, weights=pravdepodobnosti_pismen, k=random.randint(2, 10))

    #výběr náhodných spřežek z listu s určitou pravděpodobností
    vyber_z_prezek = random.choices(polske_sprezky, weights=pravdepodobnosti_sprezek, k=1)
    
    #generování čárky s pravděpodobností
    generovani_carky = random.choices(carka, weights=pravdepodobnost_carky, k=1)

    #generování tečky v textu s pravděpodobností
    generovani_tecky_v_textu = random.choices(tecka_na_konci_vety, weights=pravdepodobnost_tecky_v_textu, k=1)
    
    #generování náhodného počtu odstavců
    generovani_odstavce = random.choices(odstavec, weights=pravdepodobnost_odstavce, k=1)

    #vytvoření slova končící spřežkou
    slovo = vyber_z_abecedy + vyber_z_prezek + generovani_carky + generovani_tecky_v_textu + generovani_odstavce
    
    #vytvoření slova se spřežkou na začátku
    slovo_naopak = vyber_z_prezek + vyber_z_abecedy


    #všechna možná slova s náhodným generováním
    slova = [slovo, vyber_z_abecedy, slovo_naopak]

    #generování tečky a velkého písmena za ní
    generovani_slova_za_tecku = random.choice(slova)

    #utvoří z listu slovo bez mezer
    pravdepodobnosti_slova = random.choice(slova)
    finalni_slovo = "".join(pravdepodobnosti_slova)

    #přidá slovo do seznamu
    text.append(finalni_slovo)
    
#tečka za větou a přidání za text s přidáním posledního slova
tecka = "."

#prázdný list
posledni_slovo_s_teckou = []

#přidá list do listu
posledni_slovo_s_teckou.extend(vyber_z_abecedy)

#přidá tečku do listu
posledni_slovo_s_teckou.append(tecka)



#vytvoří text ze seznamu slov s mezerou mezi slovy a na konci textu odebere mezeru, tečku nebo čárku
finalni_text = " ".join(text).rstrip(" .,")

#udělá z finalniho textu list
finalni_text_seznam = [finalni_text]

#Lorem ipsum pro začátek textu
Lorem_ipsum = ["Lorem ipsum "]

#předělání listu na str a spojí poslední slovo s tečkou
posledni_slovo_s_teckou_text = "".join(map(str, posledni_slovo_s_teckou))

#spojení všech prvků do finálního textu
finalni_text_3 = "".join(Lorem_ipsum + finalni_text_seznam + posledni_slovo_s_teckou)

#printne celý text
print(finalni_text_3)
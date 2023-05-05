# Harjoitustyö: "hirsipuu"-peli.
# Tekijä on ennalta määritellyt sanan ja käyttäjän pitää arvata kirjain kerrallaan, minkä sanan tekijä on valinnut.
# Käyttäjällä on tekijän määrittämä määrä arvauskertoja (5 ->). Peli ilmoittaa käyttäjälle onko hän jo kertaalleen arvannut kyseisen kirjaimen.
# Peli loppuu siihen kun käyttäjä on arvannut maksimi määrän kirjaimia.
# Jos pelaaja ei arvannut sanaa, se paljastetaan lopussa.
# pelin loputtua kysy käyttäjältä haluaako pelata uudestaan kyllä tai ei.
# Peli jatkuu uudelleen jos käyttäjä antaa k. (koodi ei toimi, saan sen "e" lopettamaan mutta "k" ei anna aloittaa uudestaan. 

# Pelissä ongelmana on se, että ottaa arvauksiin mukaan kaikki merkit ja kirjaimet myös.

import random

arvattava_sana = ["tietokone", "python", "koodaus"] #tekijä voi itse määritellä sanat ja montako niitä on.
sana = random.choice(arvattava_sana) #valitse sana satunnaisesti
kirjaimet =list(sana.replace(" ", "")) #kirjaimet menee listaan

arvaukset = [] #käy listassa
arvausten_maara = 5 #arvausten määrä

oikein_arvatut =[] #tarkistaa listasta
sanan_pituus = len(sana) #katsoo sanan pituuden
#kysy = 0

print("Tervetuloa pelaamaan Arvaa sana-peliä!")
print(f"Sinulla on mahdollisuus arvata {arvausten_maara} kertaa kirjain. ")
print("Peli loppuu siihen, jos arvaat sanan oikein tai arvauskertasi loppuu.")

while len(oikein_arvatut) < sanan_pituus and arvausten_maara > 0: #Toistaa niin kauan, kunnes kirjaimet on arvattu tai arvauskerrat loppuu.
    for kirjain in sana: #kirjaimet
        if kirjain == " ":#if kirjain in oikein_arvatut: 
            print(" ", end=" ") #tulostaa _ paikalle annetun kirjaimen
        elif kirjain in oikein_arvatut:
            print(kirjain, end=" ")  
        else:
            print("_", end=" ")
    print()

    arvaus = input("Arvaa kirjain: ").lower() #Käyttäjä arvaa kirjaimen. .lower laskee mukaan isot ja pienet kirjaimet

    if arvaus in arvaukset: # tarkista onko kirjain jo arvattu aikaisemmin
        print("Olet arvannut jo tämän kirjaimen. Kokeile uudelleen. ")
    else:
        arvaukset.append(arvaus) #append lisää

        if arvaus in kirjaimet:
            oikein_arvatut.append(arvaus) #append lisää
            print("Arvasit oikein!")
            
        else:
            arvausten_maara -= 1 # Arvausten määrä vähenee aina yhdellä
            print(f"Väärin. Sinulla on enää {arvausten_maara} arvauskertaa jäljellä. ")

    if len(oikein_arvatut) == sanan_pituus:
        print(f"HIENOA! Arvasit sanan oikein: {sana}")
        break
else:
    print(f"HÄVISIT. Sana oli: {sana}")

# Pitäisi saada pelin jatkamaan, mutta en saa. Katkaisee kyllä pelin jos vastataan "e". Tämä on jostain pienestä kiinni!
jatka_pelia = True
while True:       
    kysy = input("Haluatko pelata uudestaan? Kyllä (k) vai Ei (e): ").lower() #ottaa huomioon isot ja pienet kirjaimet
    if kysy == "k":
        print("Peli alkaa uudestaan.")
        continue
    elif kysy == "e":
        print("Kiitos pelaamisesta!")
        break
    else:
        print("Väärä valinta. Vastaa uudestaan k tai e.")


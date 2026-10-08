
from tietokanta import luo_yhteys,pelaajan_lisays,pelaajan_tarkistus
from lippu import lippu
from ruumaan_matkatavarat import ruuman_matkatavarat
from turvatarkastus import turvatarkastus,laiton_lista
from lentokentta import kentta
from pelin_loppu import pelin_loppu
yhteys=luo_yhteys()

while True:
    print("1. valitse olemassa oleva pelaaja")
    print(" 2. valitse uusi pelaaja")
    valinta=input("Valitse toiminto:")

    if valinta=="1":
        matkustaja = input("anna matkustajan nimi: ")
        tarkistaminen = pelaajan_tarkistus(yhteys, matkustaja)

        if tarkistaminen:
            print("Matkustaja löytyi")
            break
        else:
           print("Nimeä ei löytynyt tietokannasta")

    elif valinta=="2":
        matkustaja = input("Luo uusi matkustaja: ")
        tarkistaminen = pelaajan_tarkistus(yhteys, matkustaja)
        if tarkistaminen:
            print("Nimi on jo käytössä")
        else:
            pelaajan_lisays(yhteys,matkustaja)
            print("Olet luonnut peliin uuden matkustajan")
            break
    else:
        print("virheelinen komento")


print(f"Peli alkaa olet valinnut {matkustaja} nimeksesi")


while True:
    pelaajan_lippu=lippu(matkustaja)

    ruuma = ruuman_matkatavarat( matkustaja)

    turvatarkastus1 = turvatarkastus( [],laiton_lista,matkustaja)
    lentokentta=kentta(matkustaja)
    pelin_loppu(kohde)

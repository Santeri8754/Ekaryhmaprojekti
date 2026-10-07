

import tietokanta
from pelin_alku import matkustaja


def turvatarkastus(matkalaukku, laiton):
    tavarat = input("Anna tavarat: ")

    while tavarat != "":
        matkalaukku.append(tavarat)


        for tavara in matkalaukku:
            if tavara in laiton:
                tarkasrus = print("Laittomia laitteita löytyi matkalaukustasi. Peli ohi!")
                break
            else:
                tarkasrus = print("ei laittomia laitteita löytynyt, voit jatkaa!")

                return tarkasrus
        break
    print("Kirjoita tavarat uudelleen.")

    tietokanta.turvatarkastus_update(matkustaja)

    print("Matkalaukkusi on hyvä. Voit jatkaa!")

lista = []
laiton_lista = ["aseet", "räjähteet", "huumeet", "piraatkit"]

turvatarkastus(lista, laiton_lista)
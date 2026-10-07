

import tietokanta


def turvatarkastus(matkalaukku, laiton):
    tavarat = input("Anna tavarat: ")

    while tavarat != "":
        matkalaukku.append(tavarat)
        tavarat = input("Anna tavarat: ")

    for tavara in matkalaukku:
        if tavara in laiton:
            print("Laittomia laitteita löytyi matkalaukustasi. Peli ohi!")
            return

    tietokanta.turvatarkastus_update(matkustaja)

    print("Matkalaukkusi on hyvä. Voit jatkaa!")

lista = []
laiton_lista = ["aseet", "räjähteet", "huumeet", "piraatkit"]

turvatarkastus(lista, laiton_lista)
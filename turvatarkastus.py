
from tietokanta import turvatarkastus_update


def turvatarkastus(matkalaukku, laiton,matkustaja):
    tavarat = input("Anna tavarat: ")

    while tavarat != "":
        matkalaukku.append(tavarat)
        tavarat = input("Anna tavarat: ")


    for tavara in matkalaukku:
        if tavara in laiton:
            tarkasrus = print("Laittomia laitteita löytyi matkalaukustasi. Peli ohi!")
            security = 0
            break
        else:
            tarkasrus = print("ei laittomia laitteita löytynyt, voit jatkaa!")
            security = 1


    turvatarkastus_update(security,matkustaja)

    print("Matkalaukkusi on hyvä. Voit jatkaa!")

lista = []
laiton_lista = ["aseet", "räjähteet", "huumeet", "piraatkit"]


#turvatarkastus(lista, laiton_lista)
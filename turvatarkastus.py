from tietokanta import tarkastus

def turvatarkastus(matkalaukku, laiton):
    matkustaja = "Heini"
    lippu = tarkastus(matkustaja)
    if lippu[0][0] == 1:
        tavarat = input("Anna tavarat: ")

        while tavarat != "":
            matkalaukku.append(tavarat)
            tavarat = input("Anna tavarat: ")

        for tavara in matkalaukku:
            if tavara in laiton:
                print("Laittomia laitteita löytyi matkalaukustasi. Peli ohi!")
                return

        print("Matkalaukkusi on hyvä. Voit jatkaa!")
    else:
        print("Virhe.")

lista = []
laiton_lista = ["aseet", "räjähteet", "huumeet", "piraatkit"]

turvatarkastus(lista, laiton_lista)

from tietokanta import luo_yhteys,matkalaukun_haku,matkalaukku_update
yhteys=luo_yhteys()
def ruuman_matkatavarat(matkustaja):
    print("\nRUUMAAN MENEVÄT MATKATAVARAT")
    if input("Onko sulla ruumaan meneviä matkatavaroita? (k/e): ").lower() == "e":
        print("Sulla ei ole ruumaan meneviä matkatavaroita.")
        return
# kommentti
    while True:
        try:
            laukkujen_maara = int(input("Kuinka monta laukkuu sulla on? "))

            if laukkujen_maara > 0:
                break

            print("anna ainakin yksi laukku ")

        except ValueError:
            print("Anna määrä numerona.")

    for i in range(1, laukkujen_maara + 1):
        while True:
            try:
                paino = float(input(f"anna laukun {i} paino kilogrammoina: "))

                if paino < 0:
                    print("Paino ei voi olla negatiivinen.")
                    continue

                break

            except ValueError:
                print("Anna paino numerona.")

        if paino > 20:
            print(f"laukku {i} on liian painava ({paino} kg)")
            print("suurin sallittu paino on 20 kg")
            matkalaukku_update(matkustaja,0)
            return

    print("\nKaikki laukut hyväksytty!")
    print("Matkatavarat voidaan laittaa ruumaan.")
    matkalaukku_update(matkustaja,1)


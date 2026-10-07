from tietokanta import luo_yhteys,lipun_haku,lipun_Update
yhteys=luo_yhteys()
def lippu(matkustaja):

    lippu=lipun_haku(yhteys,matkustaja)

    while True:
        print("1. lippua ei ole")
        print("2. lippua on")
        vaihtoehto=input("Anna komento: ")

        if vaihtoehto=="1":
            print("testaus")
            if lippu == "1":
                print("Lippua löytyi")

            else:
                print("Peli päättyi, kun sinulla ei ole lippua")
                break

        elif vaihtoehto=="2":
            lipun_Update(yhteys,matkustaja)
            print("Sinulla on lippu. ")
            break

    print("peli jatkuu")
    return lippu

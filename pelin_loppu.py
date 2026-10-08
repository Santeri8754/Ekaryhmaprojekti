def pelin_loppu(kohde):
    print(f"Olet lähtenyt Helsinki vantaa lentokentästä {kohde} lentokenttään.")

    print("Haluatko jatkaa pelii?")
    print("1. joo")
    print("2. Ei")

    valinta = input("Anna komento: ")

    if valinta == "1":
        print("Peli jatkuu!")
        return True

    elif valinta == "2":
        print("Peli on loppu. Kiitos pelaamisesta!")
        return False

    else:
        print("Virheellinen komento.")
        return pelin_loppu(kohde)

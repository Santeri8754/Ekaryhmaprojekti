from tietokanta import lentokentta

def kentta():
    lentokentan_valinta = input("Mihin lentokenttään menet?: ")
    hakeminen = lentokentta(lentokentan_valinta)

    if hakeminen is not None:
        print(f"Olet lähtenyt Helsinki-Vantaa lentokentästä {hakeminen[0]} lentokenttään.")
    else:
        print(f"Lentokenttää ei löytynyt.")
    return

kentta()
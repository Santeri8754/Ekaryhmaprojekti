from tietokanta import lentokentta,sijainnin_paivitys

def kentta(matkustaja):
    while True:
        lentokentan_valinta = input("Mihin lentokenttään menet?: ")
        hakeminen = lentokentta(lentokentan_valinta)

        if hakeminen is not None:
            kohde_koodi= hakeminen[0]
            kohde_nimi =hakeminen[1]

            print(f"Olet lähtenyt Helsinki-Vantaa lentokentästä {kohde_nimi} lentokenttään.")

            sijainnin_paivitys(kohde_koodi,matkustaja)
            print(f"Sijaintisi on päivitetty tietokantaa {kohde_koodi}")
            return True
        else:
            print(f"Lentokenttää ei löytynyt.")





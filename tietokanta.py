import mysql.connector



def luo_yhteys():
    return mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
        password="kissa12",
         autocommit=True,
        use_pure = True
         )


def pelaajan_lisays(yhteys,matkustaja):
    kursori = yhteys.cursor()
    sql = "INSERT INTO game (location,screen_name,has_ticket,security,luggage) values(%s,%s,%s,%s,%s)"
    values = ("EFHK",matkustaja,0,0,0)
    kursori.execute(sql,values)
    return matkustaja


def pelaajan_tarkistus(yhteys,matkustaja):
    kursori = yhteys.cursor()
    sql_tarkistus = f"select screen_name from game where screen_name='{matkustaja}'"
    kursori.execute(sql_tarkistus)
    tarkistus = kursori.fetchone()
    return tarkistus

def lipun_haku(yhteys,matkustaja):
    kursori = yhteys.cursor()
    sql_haku = f"select has_ticket from game where screen_name='{matkustaja}'"
    kursori.execute(sql_haku)
    tarkistus1 = kursori.fetchone()
    return  tarkistus1


def lipun_Update (yhteys,matkustaja):
    kursori = yhteys.cursor()
    sql_paivitys = f"Update game set has_ticket=1 where screen_name='{matkustaja}'"
    kursori.execute(sql_paivitys)
    return matkustaja

def lentokentta(kentta_syote):
    yhteys = luo_yhteys()
    kursori = yhteys.cursor()
    sql = f"SELECT name FROM airport WHERE name = '{kentta_syote}'"
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos

def matkalaukun_haku(yhteys, matkustaja):
    kursori = yhteys.cursor()
    sql_laukku_haku=f"select luggage from game where screen_name='{matkustaja}'"
    kursori.execute(sql_laukku_haku)
    tarkistus2 = kursori.fetchone()
    return tarkistus2

def matkalaukku_update (matkustaja, matkalaukut):
    yhteys = luo_yhteys()
    kursori = yhteys.cursor()
    sql_matkalaukku = f"Update game set luggage = {matkalaukut} where screen_name='{matkustaja}'"
    kursori.execute(sql_matkalaukku)
    return matkalaukut

def turvatarkastus_update(security,matkustaja):
    yhteys = luo_yhteys()
    kursori = yhteys.cursor()
    sql_update = f"UPDATE game SET security = {security} where screen_name='{matkustaja}'"
    kursori.execute(sql_update)
    kursori.fetchone()
    return matkustaja

def check_turvatarkastus (matkustaja):
    yhteys = luo_yhteys()
    kursori = yhteys.cursor()
    sql_select = f"select security from game where screen_name='{matkustaja}'"
    kursori.execute(sql_select)
    return kursori.fetchone()


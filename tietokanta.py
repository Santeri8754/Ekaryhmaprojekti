import mysql.connector

# from pelin_alku import matkustaja


def luo_yhteys():
    return mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='root',
        password='tietokone020',
        autocommit=True,
        use_pure = True
         )


def pelaajan_lisays(yhteys,matkustaja):
    kursori = yhteys.cursor()
    sql = "INSERT INTO game (location,screen_name,has_ticket,security,luggage) values(%s,%s,%s,%s,%s)"
    values = ("EFHK",matkustaja,1,0,1)
    kursori.execute(sql,values)
    return matkustaja


def pelaajan_tarkistus(yhteys,matkustaja):
    kursori = yhteys.cursor()
    sql_tarkistus = f"select screen_name from game where screen_name='{matkustaja}'"
    kursori.execute(sql_tarkistus)
    tarkistus = kursori.fetchone()
    return tarkistus

def tarkastus(matkustaja):
    yhteys = luo_yhteys()
    kursori = yhteys.cursor()
    sql = f"SELECT has_ticket FROM game WHERE screen_name = '{matkustaja}'"
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def lentokentta(kentta):
    yhteys = luo_yhteys()
    kursori = yhteys.cursor()
    sql = f"SELECT name FROM airport WHERE name = '{kentta}'"
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos
import mysql.connector as sql
from dotenv import load_dotenv
import os

class Connector():
    def __init__(self):
        load_dotenv()
        self.connector = sql.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.connector.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS wheather (id_ville SERIAL PRIMARY KEY,
                                                        ville VARCHAR(255),
                                                        lat FLOAT, 
                                                        lon FLOAT,
                                                        precipitation FLOAT,
                                                        description_meteo VARCHAR(255),
                                                        temperature FLOAT,
                                                        scrapp INTEGER)""")
        self.connector.commit()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS hotels (id SERIAL PRIMARY KEY,
                                                        id_ville INTEGER,
                                                        ville VARCHAR(255),
                                                        url TEXT,
                                                        nom_hotel TEXT)""")
        self.connector.commit()


    def insertWheatherData(self,id_ville,ville,lat,lon,precipitation,description_meteo,temperature,scrapp):
        requete = """
        INSERT INTO wheather (id_ville,ville,lat,lon,precipitation,description_meteo,temperature,scrapp)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (id_ville,ville,lat,lon,precipitation,description_meteo,temperature,scrapp)
        self.cursor.execute(requete,values)
        self.connector.commit()

    def insertHotels(self, id_ville,ville,url,nom_hotel):
        requete = """
        INSERT INTO hotels (id_ville,ville,url,nom_hotel)
                        VALUES (%s,%s,%s,%s)
        """
        values = (id_ville,ville,url,nom_hotel)
        self.cursor.execute(requete,values)
        self.connector.commit()

    def verifDoublonsHotels(self):
        requete = """
        SELECT id_ville, nom_hotel, COUNT(*) AS nb
        FROM hotels
        GROUP BY id_ville, nom_hotel
        HAVING COUNT(*) > 1
        """
        self.cursor.execute(requete)
        doublons = self.cursor.fetchall()
        return doublons

    def supprimerDoublonsHotels(self):
        requete = """
        DELETE FROM hotels
        WHERE id NOT IN (
        SELECT MIN(id)
        FROM hotels
        GROUP BY id_ville, nom_hotel)
        """
        self.cursor.execute(requete)
        self.connector.commit()

        





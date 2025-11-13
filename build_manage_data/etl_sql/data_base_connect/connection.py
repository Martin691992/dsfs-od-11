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
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS wheather (id_ville INTEGER PRIMARY KEY,
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
                                                        nom_hotel TEXT,
                                                        url_hotel TEXT,
                                                        note_hotel FLOAT,
                                                        description TEXT,
                                                        lat FLOAT,
                                                        lon FLOAT)""")
        self.connector.commit()


    def insertWheatherData(self,id_ville,ville,lat,lon,precipitation,description_meteo,temperature,scrapp):
        requete = """
        INSERT INTO wheather (id_ville,ville,lat,lon,precipitation,description_meteo,temperature,scrapp)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (id_ville,ville,lat,lon,precipitation,description_meteo,temperature,scrapp)
        self.cursor.execute(requete,values)
        self.connector.commit()

    def insertHotels(self, id_ville,ville,url,nom_hotel,url_hotel,note_hotel,description):
        requete = """
        INSERT INTO hotels (id_ville,ville,url,nom_hotel,url_hotel,note_hotel,description)
                        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
        values = (id_ville,ville,url,nom_hotel,url_hotel,note_hotel,description)
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

    def insertMeteo(self,id_ville,ville,latitude,longitude,precipitation,desc_meteo,temperature,scrapp):
        requete = """
        INSERT INTO wheather (id_ville,ville,lat,lon,precipitation,description_meteo,temperature,scrapp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (id_ville,ville,latitude,longitude,precipitation,desc_meteo,temperature,scrapp)
        self.cursor.execute(requete,values)
        self.connector.commit()

    def verifDoublonsMeteo(self):
        requete = """
        SELECT id_ville, ville, COUNT(*) AS nb
        FROM wheather
        GROUP BY id_ville, ville
        HAVING COUNT(*) > 1
        """
        self.cursor.execute(requete)
        doublons = self.cursor.fetchall()
        return doublons

    def supprimerDoublonsMeteo(self):
        requete = """
        DELETE FROM wheather
        WHERE id_ville NOT IN (
        SELECT MIN(id_ville)
        FROM hotels
        GROUP BY id_ville, ville)
        """
        self.cursor.execute(requete)
        self.connector.commit()

    def selectHotels(self):
        requete = """
        SELECT id, url_hotel FROM hotels WHERE lat = 0 AND lon = 0
        """
        self.cursor.execute(requete)
        return self.cursor.fetchall()
    
    def updateLatLonHotels(self, lat, lon, id_hotel):
        requete = """
        UPDATE hotels SET lat = %s, lon = %s WHERE id = %s
        """
        values = [lat,lon,id_hotel]
        self.cursor.execute(requete, values)
        self.connector.commit()

        





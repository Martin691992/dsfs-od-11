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
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS wheather (
                                                        id PRIMARY KEY INTEGER,
                                                        ville VARCHAR(255),
                                                        lat FLOAT, 
                                                        lon FLOAT,
                                                        precipitation FLOAT,
                                                        description_meteo VARCHAR(255),
                                                        temperature FLOAT,
                                                        scrapp INTEGER)""")
        self.connector.commit()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS hotels (
                                                        id PRIMARY KEY INTEGER,
                                                        id_ville INTEGER,
                                                        ville VARCHAR(255),
                                                        url TEXT,
                                                        nom_hotel)""")
        self.connector.commit()


    def insertWheatherData(self, data):
        requete = """
        INSERT INTO wheather (id,ville,lat,lon,precipitation,description_meteo,temperature,scrapp)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = ""
        self.cursor.execute()
        





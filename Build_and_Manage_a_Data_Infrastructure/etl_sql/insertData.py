from etl_sql.data_base_connect.connection import Connector
import pandas as pd

class DataInsertion():
    def __init__(self):
        self.hotels = []
        with open('./data/hotels.csv','r',encoding='utf-8') as f:
            for i in f.readlines():
                lignes = i.replace("\n","")
                self.hotels.append(lignes.split(','))

        # on supprime la 1ère colonne qui sont les titres des données
        self.hotels = self.hotels[1:]

        if not len(self.hotels) == 875 :
            return
        
        





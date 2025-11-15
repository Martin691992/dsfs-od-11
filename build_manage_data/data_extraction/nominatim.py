import requests
import time
import pandas as pd
import os

class ExtractCitiesLocation:
    def __init__(self):
        cities = ["Mont Saint Michel","St Malo","Bayeux","Le Havre","Rouen","Paris","Amiens","Lille","Strasbourg","Chateau du Haut Koenigsbourg","Colmar","Eguisheim","Besancon","Dijon","Annecy","Grenoble","Lyon","Gorges du Verdon","Bormes les Mimosas","Cassis","Marseille","Aix en Provence","Avignon","Uzes","Nimes","Aigues Mortes","Saintes Maries de la mer","Collioure","Carcassonne","Ariege","Toulouse","Montauban","Biarritz","Bayonne","La Rochelle"]
        results = []
        for i in cities:
            request = f'https://nominatim.openstreetmap.org/search?q={i}&format=json'
            headers = {
                'User-Agent': 'fullstack data science education'
            }
            response = requests.get(request,headers=headers)
            if response.raise_for_status():
                print(response.raise_for_status())
                print("Une erreur s'est produite !")
                print(response.text)
                break
            data = response.json()
            results.append(data[0])
            print(f"Données météo reçues pour : {i}")
            time.sleep(1) ## on attend une seconde pour ne pas se faire bannir de l'api

        print(f"{len(results)} resultats")
        # écriture des colonnes, je ne garde ici que l'index, name, la latitude et la longitude

        with open('./data/city_lat_lon.txt',"w") as f:
            f.write('id,name,lat,lon\n')

        for index, y in enumerate(results):
            print(f"{y['name']} : latitude = {y['lat']} - longitude {y['lon']}")
            with open('./data/city_lat_lon.txt',"a",encoding='utf-8') as f:
                f.write(f"{index},{y['name']},{y['lat']},{y['lon']}\n")


from dotenv import load_dotenv
import pandas as pd
import requests
import time
import datetime
import os


class LoadWeather():
    def __init__(self):
        load_dotenv()
        df = pd.read_table('./data/city_lat_lon.txt',encoding='utf-8',sep=',')
        df.set_index('id',inplace=True)
        df[['précipitation','description_meteo','temperature']] = df.apply(lambda row : pd.Series(self.findWeatherLatLong(row)),axis=1)
        df['scrapp'] = 0
        print('Enregistrement des résultats')
        df.to_csv('./data/wheather.csv',encoding='utf-8')

    def findWeatherLatLong(self, row):
        """
            Fonction servant à récupérer le temps qu'il fait à une latitude et logitude donnée

            row : Ligne de notre DataFrame
            docs de l'API : https://openweathermap.org/forecast5

        """
        API_KEY = os.getenv('WHEATHER_API_KEY')
        req = f"https://api.openweathermap.org/data/2.5/forecast?lat={row['lat']}&lon={row['lon']}&units=metric&appid={API_KEY}&lang=fr"
        response = requests.get(req)
        if response.raise_for_status():
            print(response.raise_for_status())
        data = response.json()
        for i in data['list'] :
            today = datetime.date.today()
            date = datetime.date.fromtimestamp(i['dt'])
            # On recherche la météo a 5 jours donc on compare à la date du jour
            ecart = date - today
            # pour avoir la prévision dans 5 jours et plutot en milieu de journée (entre 8h et 13h)
            if ecart.days >= 5 and datetime.datetime.fromtimestamp(i['dt']).hour in [8,9,10,11,12,13,14]:
                # print(i['main']['temp'])
                # print(i['weather'][0]['description'])
                # time.sleep(0.5)
                # on retourne les précipitations, la description du temps et la température (voir doc API si nécessaire)
                return (i['pop'], i['weather'][0]['description'], i['main']['temp'])







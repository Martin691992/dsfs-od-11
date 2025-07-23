from dotenv import load_dotenv
import pandas as pd
import requests
import time
import datetime
import os

load_dotenv()
API_KEY = os.getenv('WHEATHER_API_KEY')

# def findWeatherLatLong(row):
#     req = f"https://api.openweathermap.org/data/2.5/forecast?lat={row['lat']}&lon={row['lon']}&units=metric&appid={API_KEY}&lang=fr"
#     response = requests.get(req)
#     if response.raise_for_status():
#         print(response.raise_for_status())
#         return 'erreur'
#     data = response.json()
#     print(data)
#     print(f"Les temps à {row['name']} est {data["list"]['weather']['main']}")
#     time.sleep(0.5)
#     return data["list"]['pop']

# df = pd.read_table('./Build_&_Manage_a_Data_Infrastructure/data/city_lat_lon.txt',encoding='utf-8',sep=',')
# df.set_index('id',inplace=True)
# df['new_row'] = df.apply(lambda row : findWeatherLatLong(row),axis=1)
# print(df.head())
# print('Enregistrement des résultats :')
# df.to_csv('./Build_&_Manage_a_Data_Infrastructure/data/wheather.csv',encoding='utf-8')


req = f"https://api.openweathermap.org/data/2.5/forecast?lat={45.7578137}&lon={4.8320114}&units=metric&appid={API_KEY}&lang=fr"
response = requests.get(req)
if response.raise_for_status():
    print(response.raise_for_status())
    
data = response.json()
for i in data['list'] :
    today = datetime.datetime.now()
    date = datetime.datetime.fromtimestamp(i['dt'])
    ecart = date - today
    if ecart.days == 4:
        print(date)

    # print(datetime.datetime.strftime())
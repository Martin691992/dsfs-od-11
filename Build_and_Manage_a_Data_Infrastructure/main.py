# Main script
# On peut lancer ce script dans le venv et ainsi faire les extractions de données, leur traitement et enregistrement
import os
from data_extraction.wheather import LoadWeather
from data_extraction.nominatim import ExtractCitiesLocation
from scrapping.scrapBooking import Crawl
from etl_sql.insertData import DataInsertion


if __name__ == "__main__":
    if not os.path.exists('./data'):
        print("Création du dossier data pour les données temporaires")
        os.mkdir('./data')

    print("Lancement du Script ETL")
    if not os.path.exists('./data/wheather.csv'):
        print("Récupération des Latitudes et logitudes")
        ExtractCitiesLocation()
        
    if not os.path.exists('./data/wheather.csv'):
        print("Lancement de la récupération de la météo")
        LoadWeather()
        print("Fin de la récupération de la météo")
    
    print("Lancement du Scrapping")
    # On pourra relancer le script autant de fois que nécessaire pour avoir des hotels dans toutes les villes car de temps à autres les
    # les hotels ne sont pas scrappés tout de suite.
    # On pourrait mettre en place un CrawlerRunner plutot que CrawlerProcess car le pas possible de relancer plusieur fois CrawlerProcess
    scrapping = Crawl()
    if scrapping.anyVilles == True:
        print("Plus d'hotels à scrapper")
    print("Fin du scrapping")
    data = DataInsertion()
    data.insertionHotels()
    print("Insertion des données terminée")
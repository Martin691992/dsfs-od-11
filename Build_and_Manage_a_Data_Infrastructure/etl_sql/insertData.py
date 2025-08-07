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
        db = Connector()
        choix = input(f"la liste des hotels est de {len(self.hotels)} hotels, voulez-vous continuer ? (Y/n) : ")
        while choix not in ["Y", "n"]:
            print("Veuillez répondre par Y : (oui) ou n (non)")
            choix = input(f"la liste des hotels est de {len(self.hotels)} hotels, voulez-vous continuer ? (Y/n) : ")
        if choix == 'Y':
            for i in self.hotels :
                id_ville = i[0]
                ville = i[1]
                url = i[2]
                nom_hotel = i[3]
                try :
                    db.insertHotels(id_ville,ville,url,nom_hotel)
                    print(f"insertion réussie pour {nom_hotel}")
                except:
                    print(f"une erreur s'est produite pour {ville} - {nom_hotel}")

            print("l'insertion des hotels s'est bien déroulés")


        print("-------")
        doublon = input("Voulez vous vérifier s'il y a des doublons dans les hotels ? (Y/n) : ")
        while doublon not in ["Y","n"]:
            print("Veuillez répondre par Y : (oui) ou n (non)")
            doublon = input("Voulez vous vérifier s'il y a des doublons dans les hotels ? (Y/n) :")
        if doublon == "Y":
            print("Vérification des doublons")
            tab_doublons = db.verifDoublonsHotels()
            print(f"Il y a {len(tab_doublons)} doublons dans la table hotels")
            if len(tab_doublons) > 0:
                supp_doublon = input("Voulez vous supprimer les doublons ? (Y/n) ")
                while supp_doublon not in ["Y","n"]:
                    print("Veuillez répondre par Y : (oui) ou n (non)")
                    supp_doublon = input("Voulez vous supprimer les doublons ? (Y/n) ")
                if supp_doublon == 'Y':
                    db.supprimerDoublonsHotels()
                    print("Les doublons ont été supprimé")
        return

        


        





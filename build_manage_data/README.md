# Build & Manage a Data Infrastructure

Vous pouvez trouver un fichier requirements.txt
Il est recommandé d'utiliser un venv Python pour executer le code

Cmd : python -m venv venv
Cmd : venv/Scripts/activate (pour les utilisateurs de Windows)
puis : pip install -r requirements.txt


BDD personnel : Hébergement chez o2switch - MySQL
Un fichier .env avec des identifiants corrects est nécessaire pour la connexion à la base de donnée.

Bucket S3 : 


main.py est le script de scrapping et permet de : 
- récupérer les données 
- intégrer les données dans une base de donnée SQL et un bucket S3
- vérifier les doublons dans la base de donnée

visualisations.ipynb est le notebook des visualisations : 
Il interroge la base donnée et permet de retrouver les top 5 destinations et ensuite les top 20 des hotels dans ce top 5.
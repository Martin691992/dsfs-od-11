# Déploiement

## Organisation du projet

Pour des raisons pratiques, les données ne sont pas incluses dans ce dépôt.  
Pour fonctionner correctement, ce projet a besoin d’un dossier **`data`** à la racine, contenant toutes les données nécessaires.

### Getaround

Application Svelte pour l’affichage du dashboard et les endpoints de l’API.

Un sous-processus sera utilisé pour lire les résultats d’un script Python.

Le déploiement se fait grâce au **docker-compose** présent dans le projet.

### Sur Linux

```bash
sudo docker compose up --build


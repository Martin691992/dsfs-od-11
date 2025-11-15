# Deeplearning

`python -m venv venv `
`pip install -r requirements.txt `

pour fonctionner vous devez également télécharger les données et le placer dans un dossier data

## Structure du dossier

- eda : Exploration simple des données
- classifiers : Différents essais de création d'un classifiers de Ham ou Spam

3 Notebooks pour estimer la performance d'un reseau de neurone avec une, deux et trois chouches

### Conclusion : 

En entrainant un modèle avec deux couches de neurones on obtient une meilleure courbe qu'avec une seule couche ou trois.

On overfit certainement sur les trois modèles étant donné la faible quantité de données que nous avons à disposition.
Le classifier à trois couche par contre overfit clairement vu que la courb de validation remonte à partir de 5/6 epoch

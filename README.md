# Avocado Dashboard 

Application Dash interactive sur les ventes d'avocats aux États-Unis.

## Prérequis
- Python 3.10+
- UV

## Installation
uv sync

## Lancement
uv run python app.py

Ouvrir dans le navigateur : http://127.0.0.1:8050

## Pages
- **Comparaison** : comparaison des quantités vendues entre régions
- **Affichage des données** : tableau filtrable par région et type
- **Aide en ligne** : documentation sur Dash

## Structure
- app.py : point d'entrée
- pages/page1.py : layout page comparaison
- pages/page1_cb.py : callbacks page comparaison
- pages/page2.py : layout page tableau
- pages/page2_cb.py : callbacks page tableau
- pages/page3.py : layout page markdown
- datas/ : dataset avocado.csv
- assets/ : fichiers CSS
```

# Hackathon
L'objectif de l'application est de fournir à l'utilisateur la liste des évènements culturels disponibles à Nantes en fonction de ses préférences.
Une liste de catégories est fournie et permet de filtrer les évènements affichés. 

La partie back est implémenté avec le module flask de python, et le front est implémenté avec node et VueJS. 

## Backend
### Installation
```console
pip install -r "requirements.txt"
```
### Lancement
Lancer le fichier main.py avec un interpreteur python
Il se lancera avec comme addresse ip localhost:5001

### Fonctionnement
Les répertoires /src et /tests correspondent aux fichiers du back-end.  
L'application flask et ses endpoints sont définis dans le fichier src/main.py.  
Cette application utilise l'API de Nantes Métropole pour récupérer ses données. Il faut fournir la clef API avec une variable d'environnement nommé API_KEY.  
Lien de l'API de Nantes Métropole: https://data.nantesmetropole.fr/explore/dataset/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/api/

## Front-end
### Installation
```console
npm install
```

### Run le front
En mode dev : 
```console
npm run dev
```
En mode prod :
```console
npm run serve
```
Pour que le front soit opérationnelle, le back doit être lancé au préalable.

### Fonctionnement
Le répertoire /front_src correspond aux fichiers du front-end.  
L'application Vue possède pour le moment une seule vue qui correspond à la page d'accueil.  
Cette page est constituée de deux composants: la sélection de catégories pour le filtrage des événements et l'affichage des événements filtrés.


## Déploiement

Le déploiement se fait grâce à scalingo, Il se fait automatiquement après chaque push sur la branche main, une fois que tous les tests ont été effectués. La configuration du déploiement se fait dans le fichier PROCFILE ainsi que dans le fichier buildpacks.

## Tests
Les tests sont fait grâce à Github, les commandes lancées sont présentes dans le ficher workflows/PR.yml, ils se lancent à chque pull request et à chaque push sur le main et la branch develop. Ils vérifient et le frontend et le backend

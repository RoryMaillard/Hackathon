# Hackathon : Événements culturels
## Contexte
L'objectif de l'application est de fournir à l'utilisateur la liste des évènements culturels disponibles à Nantes en fonction de ses préférences.
Une liste de catégories est fournie et permet de filtrer les événements affichés.

La partie back est implémentée avec le module flask de python, et le front avec node et VueJS.

Lien du code source: https://github.com/RoryMaillard/Hackathon

## Structure du Projet :
Le projet est divisé en 2 parties, le frontend dans le dossier front_src et le back dans le dossier back.
Les deux sont un peu mélangés à cause de la manière dont Scalingo detecte les langages pour avoir un environnement correct.

## Backend

### Fonctionnement
Le répertoire /back correspond aux fichiers du backend, /src et /tests correspondent respectivement aux fichers sources et tests. 
L'application flask et ses endpoints sont définis dans le fichier src/main.py.
Une documentation openapi est disponible dans le dossier /back  et a ce lien : https://app.swaggerhub.com/apis-docs/RORYMAILLARD2_1/event-api/1.0.0
Cette application utilise l'API de Nantes Métropole pour récupérer ses données. Il faut fournir la clef API avec une variable d'environnement nommé API_KEY.  
Lien de l'API de Nantes Métropole: https://data.nantesmetropole.fr/explore/dataset/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/api/

### Installation
```console
pip install -r "requirements.txt"
```
### Lancement
Lancer le fichier main.py avec un interpreteur python
Il se lancera avec comme addresse ip localhost:5001


## Front-end

### Fonctionnement
L'application Vue possède pour le moment une seule vue qui correspond à la page d'accueil.  
Cette page est constituée de deux composants: la sélection de catégories pour le filtrage des événements et l'affichage des événements filtrés.

### Installation
```console
npm install
```

### Run le front
Pour run le front, il faut d'abord le build, avec
```console
npm run build
```
et le backend flask s'occupe de faire le lien avec le front qui a été build


## Contribution
Ce projet possède deux branches protégées, **main** et **develop**. Pour contribuer, il faut créer sa propre branche à partir de la branche **develop**. Lorsque le code sur la branche est terminé, il faut
créer une Pull Request pour merge son travail sur la branche **develop**.  
Si tous les tests passent et que la pull request est validée par un autre membre de l'équipe, on peut la merge dans **develop**.  
Une fois que tous les tests sont passés sur la branche **develop**, un membre de l'équipe peut décider de vouloir déployer en production le travail. Ainsi il pourra créer une Pull request de la branche **develop** vers la branche **main**.
Si tous les tests passent et que la pull request est validée, on peut donc la merge dans le main.  
Les tests seront effectués sur la branche main et s'ils passent, l'application sera déployée sur Scalingo 




## Déploiement

Le déploiement se fait grâce à Scalingo. Il se fait automatiquement après chaque push sur la branche main, une fois que tous les tests ont été effectués. 
La configuration du déploiement se fait dans le fichier PROCFILE, dans lequel il faut détailler les commandes pour lancer l'application web.
Scalingo prend le projet et fait le déploiment de son coté, l'avancé du déploiement est visible ici **https://dashboard.scalingo.com/apps/osc-fr1/hackathonlogin2023/deploy/list**
Une fois le site déployé, il est disponible sur ce lien :
**https://hackathonlogin2023.osc-fr1.scalingo.io/**

## Tests
Les tests sont faits grâce à Github Actions, la pipeline est écrite dans le fichier workflows/PR.yml, ils se lancent à chaque pull request et à chaque push sur le main et la branche develop.
Il y a trois jobs qui sont lancés :
- le premier teste le backend python (job flask-test)
- le deuxième teste de build le frontend (job build)
- le troisième s'occupe des tests frontend (job vue-test)

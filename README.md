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

## Déploiement

Le déploiement se fait grâce à scalingo, Il se fait automatiquement après chaque push sur la branche main, une fois que tous les tests ont été effectués. La configuration du déploiement se fait dans le fichier PROCFILE ainsi que dans le fichier buildpacks.

## Tests
Les tests sont fait grâce à Github, les commandes lancées sont présentes dans le ficher workflows/PR.yml, ils se lancent à chque pull request et à chaque push sur le main et la branch develop. Ils vérifient et le frontend et le backend

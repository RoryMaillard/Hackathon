# Hackathon

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
## Déploiement

Le déploiement se fait grâce à scalingo, Il se fait automatiquement après chaque push sur la branche main, une fois que tous les tests ont été effectués. La configuration du déploiement se fait dans le fichier PROCFILE ainsi que dans le fichier buildpacks.

## Tests
Les tests sont fait grâce à Github, les commandes lancées sont présentes dans le ficher workflows/PR.yml, ils se lancent à chque pull request et à chaque push sur le main et la branch develop. Ils vérifient et le frontend et le backend

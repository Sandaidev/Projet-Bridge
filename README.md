# Projet-Bridge

### C'est quoi ça?
Basiquement, c'est un script Python qui convertit les données des capteurs Arduino en une requête HTTP GET.
-> ça relie les repositories [Projet-Site](https://github.com/Sandaidev/Projet-Site) et [Projet-Arduino](https://github.com/Sandaidev/Projet-Arduino)

### Comment ça marche?
Pour simplifier les choses, la carte Arduino est contrôlée par PyFirmata pour pouvoir programmer avec un langage de haut niveau,
On crée un objet pour chaque capteur, on stocke leur données dans un `dict` et on les envoie par une requête GET à localhost!
Oui, aussi simple que ça!

## Setup sur un serveur de prod
- De mon côté, j'ai modifié le crontab de root (`sudo crontab -e`) et ajouté le script au démarrage (`@reboot`), ça fait le taff mais si faut sécuriser les choses, utiliser un container LXD ou Docker serait une meilleure idée.


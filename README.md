# Createur d'environnement
---

## Installation (Windows)
Après avoir cloner le projet vous avez deux étapes importantes à réaliser

- Personnalisez le lieux où sera créer l'environnement (dans le fichier python)
- Ajouter le dossier aux variables d'environnement
- Créer le fichier bat au mêmes endroit que le fichier .py :
  ```
  @echo off
  py "C:\chemin\depuis\la\racine\create_env.py" %*
  ```
---
## Utilisation 
Dans powershell ou cmd tapez juste : create_env
Rentrez le nom du projet, les fichiers seront créer.

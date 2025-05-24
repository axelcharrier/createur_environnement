### This program is here to create rapidly an environnement to code
### in php with some preset files and directories
###
### - Add this path into your environnement vars (path)

import subprocess
import os

def exec_command(command):
    try:
        subprocess.run(command, check=True)
        print(f"✅ Exécution : {' '.join(command)}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'exécution : {e}")

def write(path, content):
    with open(path, 'w') as file:
        file.write(content)
    print(f"✅ Fichier écrit : {path}")
    return path + " rempli"

def main():
    nom = input("Nom du projet PHP : ").replace(" ", "_")
    
    projet_path = f"c:\\xampp\\htdocs\\{nom}"

    commands = [
        ["cmd", "/c", "mkdir", projet_path],
        ["cmd", "/c", "mkdir", projet_path + "\\img"],
        ["cmd", "/c", "mkdir", projet_path + "\\objets"],
        ["cmd", "/c", "mkdir", projet_path + "\\actions"],
        ["cmd", "/c", "type nul >", projet_path + "\\header.php"],
        ["cmd", "/c", "type nul >", projet_path + "\\index.php"],
        ["cmd", "/c", "type nul >", projet_path + "\\footer.php"],
        ["cmd", "/c", "type nul >", projet_path + "\\style.css"],
        ["cmd", "/c", "type nul >", projet_path + "\\script.js"],
        ["cmd", "/c", "type nul >", projet_path + "\\config.php"]
    ]

    for cmd in commands:
        exec_command(cmd)

    path_content = [
        {
            "path": projet_path + "\\config.php",
            "content": """<?php
class Config {
   const SERVEUR = "";
   const BASEDEDONNEES = "";
   const UTILISATEUR = "";
   const MOTDEPASSE = "";
}
?>"""
        },
        {
            "path": projet_path + "\\header.php",
            "content": """<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
    <title>Document</title>
</head>
<body>
"""
        },
        {
            "path" : projet_path + "\\index.php",
            "content" : """<?php
include 'header.php';
?>

<?php
include 'footer.php';
?>"""
        },
        {
            "path" : projet_path + "\\footer.php",
            "content" : """</body>
</html>"""
        }
    ]

    for i in path_content:
        write(i["path"], i["content"])

if __name__ == "__main__":
    main()

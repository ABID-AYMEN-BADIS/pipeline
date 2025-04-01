import os
import sys

# Définition des extensions autorisées pour chaque dossier
allowed_extensions = {
    "site": {".html", ".php"},
    "site/img": {".png", ".jpg"},
    "site/css": {".css"},
    "site/js": {".js"}
}

def check_directory_structure():
    for directory, valid_extensions in allowed_extensions.items():
        # Vérifier si le dossier existe
        if not os.path.exists(directory):
            print(f"⚠️ Le dossier '{directory}' n'existe pas. Ignoré.")
            continue  

        # Vérifier uniquement les fichiers dans le dossier (pas de sous-dossiers)
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)

            # Vérifier si c'est bien un fichier (et pas un dossier)
            if not os.path.isfile(file_path):
                continue  

            # Récupérer l'extension du fichier
            _, file_extension = os.path.splitext(file)
            file_extension = file_extension.lower()

            # Vérification de l'extension
            if file_extension not in valid_extensions:
                print(f"❌ Erreur : {file} dans '{directory}' a une extension interdite ({file_extension}) !")
                sys.exit(1)  # Arrêt immédiat si une erreur est détectée

    print("✅ Tout est bon : arborescence et extensions conformes.")

if __name__ == "__main__":
    check_directory_structure()

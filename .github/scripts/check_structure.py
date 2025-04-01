import os
import sys

# Définition des extensions autorisées pour chaque dossier
allowed_extensions = {
    "site": [".html", ".php"],
    "site/img": [".png", ".jpg"],
    "site/css": [".css"],
    "site/js": [".js"]
}

def check_directory_structure():
    for directory, extensions in allowed_extensions.items():
        if not os.path.isdir(directory):
            continue  # Si le dossier n'existe pas, on l'ignore

        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)  # Obtenir le chemin complet
                file_extension = os.path.splitext(file)[1].lower()  # Extension en minuscule

                # Vérifie si l'extension est autorisée pour ce dossier
                if file_extension not in extensions:
                    print(f"❌ Erreur : {file_path} a une extension non autorisée ({file_extension}) !")
                    sys.exit(1)  # Arrêter l'exécution en cas d'erreur

    print("✅ Arborescence et extensions conformes.")

if __name__ == "__main__":
    check_directory_structure()

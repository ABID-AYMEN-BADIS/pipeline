import os
import sys

def check_directory_structure():
    allowed_extensions = {
        "site": [".html", ".php"],
        "site/img": [".png", ".jpg"],
        "site/css": [".css"],
        "site/js": [".js"]
    }
    
    for directory, extensions in allowed_extensions.items():
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    if not any(file.endswith(ext) for ext in extensions):
                        print(f"Erreur: {file} dans {root} n'a pas une extension autorisée.")
                        sys.exit(1)
    print("Arborescence et extensions conformes.")

if __name__ == "__main__":
    check_directory_structure()

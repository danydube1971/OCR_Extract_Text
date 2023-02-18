'''Ce script utilise la fonction input pour demander à l'utilisateur d'entrer le nom d'un image à extraire du texte. 
Ensuite, il utilise os pour définir le chemin d'accès à l'image dans le dossier courant et charge l'image en mémoire 
en utilisant PIL. Ensuite, il utilise pytesseract pour extraire le texte de l'image et stocke le résultat dans la variable text. 
Enfin, le texte est écrit dans un fichier texte nommé resultat_extraction.txt en utilisant with open().

Vous devez installer les paquets :
apt-get install tesseract-ocr
apt-get install tesseract-ocr-fra'''

# Importer les bibliothèques nécessaires
import pytesseract
import os
from PIL import Image

# Demander le nom du fichier .jpg à extraire du texte
filename = input("Entrez le nom de l'image à extraire du texte : ")

# Définir le chemin d'accès à l'image
img_path = os.path.join(os.getcwd(), filename)

# Charger l'image en utilisant PIL
img = Image.open(img_path)

# Extraire le texte de l'image en utilisant pytesseract
text = pytesseract.image_to_string(img, lang='fra') # langage français utilisé

# Créer un fichier texte et écrire le texte extrait
with open("resultat_extraction.txt", "w") as f:
    f.write(text)


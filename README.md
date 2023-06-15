# OCR_Extract_Text

Ce script utilise la fonction *input* pour demander à l'utilisateur d'entrer le nom d'une image à extraire du texte. 
Ensuite, il utilise *os* pour définir le chemin d'accès à l'image dans le dossier courant et charge l'image en mémoire en utilisant **PIL**. 
Ensuite, il utilise **pytesseract** pour extraire le texte de l'image et stocke le résultat dans la variable text. 
Enfin, le texte est écrit dans un fichier texte nommé **resultat_extraction.txt** en utilisant with *open()*.

Vous devez installer les paquets :

**apt-get install tesseract-ocr**

**apt-get install tesseract-ocr-fra**

Script python 3 testé dans Linux Mint 21



import secrets
import string
import os



alphabet = string.ascii_letters + string.digits + string.punctuation 
#Création d'une variable composé de lettres Maj/Min, chiffre et caractère spéciaux.

site = input("Entre le nom du site : ") #demande choix utilisateur via input
#L'utilisateur rentre le nom du site/appli dont il veut faire le mdp.

longueur = int(input("Choisi la longueur du mot de passe souhaité : ")) #int permet de considérer l'input comme des chiffres (donc ne pas écrire de lettre)
#Définition de la longueur du mot de passe souhaité.

password = ''.join(secrets.choice(alphabet) for i in range(longueur))
#création du mot de passe en piochant des valeurs aléatoires dans alphabet selon la longueur souhaitée

chemin_fichier = input("Entre le chemin absolu où tu veux enregistrer ton fichier csv : ")
#Utilisateur entre chemin absolu où il veut enregistrer le fichier.

fichier_csv = os.path.join(chemin_fichier, "passwords.csv")
#Création du lien total (donc avec ajout du fichier en fin de chemin via os.path.join)


"""
    A présent, on fait le code pour : 
        Créer le csv à l'endroit indiquer 
        Enregistrer dans le csv les variables site et password
        Ne pas écraser le csv si ce dernier existe déjà à cet emplacement    
"""


if os.path.exists(fichier_csv) : #si le fichier existe déjà, fait cela 
    fichier = open(fichier_csv, 'a') #ouvre le fichier. Le mode a permet de créer ET de mettre à jour si déjà existant.
    fichier.write(site + "," + password +"\n") #ajoute au format csv les variables site et password
    fichier.close() #ferme et enregistre le csv
    print("mot de passe généré et enregistré !") #log généré pour informer l'utilisateur  

else : #si le fichier n'existe pas, fait cela 
    fichier = open(fichier_csv, 'a')
    fichier.write("site,mot_de_passe\n") #créer les entêtes de colonnes site et mot_de_passe.
    fichier.write(site + "," + password +"\n")
    fichier.close()
    print("mot de passe généré et enregistré !")


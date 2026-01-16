import pandas as pd

"""
Ce code permet de : 

- Fusionner deux CSV en un seul CSV de sortie 
- Sélectionner les colonnes souhaitées en sortie 
- Trier les doublons en se basant sur les valeurs d'une colonne afin d'éviter la répition de données.

L'idée de ce code est de permettre de donner en sortie un CSV aux données nettoyées afin d'en faire un table dans une BDDR

"""



"""
Déclaration des variables
"""

CSV_2018 =  pd.read_csv('/home/florian/Desktop/groupe_4/fr-esr-parcoursup-2018.csv', sep=";") #Ici mettre le chemin absolu vers le CSV de 2018

CSV_2024 = pd.read_csv('/home/florian/Desktop/groupe_4/fr-esr-parcoursup-2024.csv', sep=";") #Ici mettre le chemin absolu vers le CSV de 2024

UAI = "Code UAI de l'établissement" #Ici préciser le nom de la colonne COMMUNE à nos CSV et sur laquelle on effectuera le trie des doublons.

CSV_sortie = "/home/florian/Desktop/groupe_4/Tables/Etablissement.csv" #Ici spécifier le chemin de sortie.




"""
Coeur du script, opération de concaténation et trie des données.
"""


CSV_Combine = pd.concat([CSV_2018, CSV_2024], ignore_index=True) # Mélanger les deux CSV en un seul afin de faciliter les opérations.

# print(len(CSV_Combine)) permet de vérifier si les deux csv sont chargés

sélection_UAI = CSV_Combine.drop_duplicates(subset=[UAI]) #Regarder la colonne spécifiée et éliminer tout les doublons.
# print("Nombre de lignes après suppression des doublons :", len(sélection_UAI)) permet de vérifier qu'il y a eu tri

colonnes_tables = [UAI, "Statut de l’établissement de la filière de formation (public, privé…)", "Établissement", "Code départemental de l’établissement"] #Ne garder que ces colonnes là avec les valeurs triées.

CSV_final = sélection_UAI[colonnes_tables] #le CSV final résulte de l'action des deux variables précédemment déclarées. Permet de les actionner.

# print(CSV_final.head()) permet de vérifier que ça marche




"""
Export des résultats en CSV 
"""


CSV_final.to_csv(CSV_sortie, index=False) #Conserver le fichier dans un CSV stocké et nommé selon la variable CSV_sortie.
print(f"le fichier csv à été enregistré à : {CSV_sortie}") #Message de confirmation.
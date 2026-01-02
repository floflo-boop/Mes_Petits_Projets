import pandas as pd
import os

donnees="/home/florian/Desktop/groupe_4/fr-esr-parcoursup-2024.csv"
donnees_chargees = pd.read_csv(donnees, sep=";")
colonnes = donnees_chargees.columns

output = pd.DataFrame({
    "colonnes" : colonnes
})

output.to_csv("liste_colonnes.csv", index=False, sep=";")
print("📄 Rapport généré : liste_colonnes.csv")

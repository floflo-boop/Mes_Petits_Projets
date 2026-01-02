import pandas as pd
import os

csv1="/home/florian/Desktop/groupe_4/fr-esr-parcoursup-2018.csv"
csv2="/home/florian/Desktop/groupe_4/fr-esr-parcoursup-2024.csv"

if os.path.exists(csv1):
    print("le fichier csv1 existe")
else :
    print("le fichier csv1 n'existe pas")

if os.path.exists(csv2):
    print("le fichier csv2 existe")
else:
    print("le fichier csv2 n'existe pas")

csv1_chargé = pd.read_csv(csv1, sep=";")
csv2_chargé = pd.read_csv(csv2, sep=";")

print(f"Le fichier {csv1} a {len(csv1_chargé)} lignes et {len(csv1_chargé.columns)} colonnes")
print(f"Le fichier {csv2} a {len(csv2_chargé)} lignes et {len(csv2_chargé.columns)} colonnes")

"""
code suivant pour afficher le nombres de lignes, le nombre de colonnes, le noms des colonnes et le type de données de chaque colonne.


print(f"Le fichier {csv1} a {len(csv1_chargé)} lignes et {len(csv1_chargé.columns)} colonnes")
print(f"Les colonnes de {csv1} sont : {csv1_chargé.columns}")


for col in csv1_chargé.columns:
    print(f"{col} : {csv1_chargé[col].dtype}")
"""



cols1 = set(csv1_chargé.columns)
cols2 = set(csv2_chargé.columns)

cols_communes = sorted(list(cols1 & cols2))
cols_csv1 = sorted(list(cols1 - cols2))
cols_uniques2 = sorted(list(cols2 - cols1))

"""for col in cols_communes:
    type1 = csv1_chargé[col].dtype
    type2 = csv2_chargé[col].dtype

    if type1 != type2:
        print(f"⚠️ Type différent pour {col}: CSV1={type1}, CSV2={type2}")
    else:
        print(f"✅ Type identique pour {col}: {type1}")

print("Colonnes communes :", cols1 & cols2)
print("Colonnes uniquement dans CSV1 :", cols1 - cols2)
print("Colonnes uniquement dans CSV2 :", cols2 - cols1)
"""
max_len = max(len(cols_communes), len(cols_csv1), len(cols_uniques2))

cols_communes += [""] * (max_len - len(cols_communes))
cols_csv1 += [""] * (max_len - len(cols_csv1))
cols_uniques2 += [""] * (max_len - len(cols_uniques2))


output = pd.DataFrame({
    "colonne communes": cols_communes,
    "colonne csv 2018" : cols_csv1,
    "colonne csv 2024" : cols_uniques2
})

output.to_csv("rapport_colonnes.csv", index=False, sep=";")
print("📄 Rapport généré : rapport_colonnes.csv")

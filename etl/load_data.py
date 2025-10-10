import sqlite3
import os
import pandas as pd
import random

# ===========================
# 🍕 Connexion à la base SQLite
# ===========================

# Définir le chemin vers la base SQLite
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'pizza_dw.db')
 
# Établir la connexion
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("✅ Connexion établie avec succès :", DB_PATH)

# (Test simple : afficher les tables existantes)
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("📂 Tables trouvées :", tables)


# ===========================
# 📥 ETAPE 1 : EXTRACTION
# ===========================

# Définir les chemins des fichiers
pizza_sales_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'pizza_sales.csv')
clients_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'clients.csv')

# Lire les fichiers CSV
pizza_df = pd.read_csv(pizza_sales_path)
clients_df = pd.read_csv(clients_path)

# Afficher un aperçu
print("\n🍕 Aperçu du dataset Pizza Sales :")
print(pizza_df.head())

print("\n👤 Aperçu du dataset Clients :")
print(clients_df.head())


# ===========================
# ⏳ ETAPE 2 : TRANSFORMATION (DIM_TEMPS)
# ===========================

#Si on souhaite affichier quelque ligne de la colonne
#print("\n🧾 Vérification du format de la colonne 'order_date' :")
#print(pizza_df['order_date'].head())

# Convertir la colonne 'order_date' en datetime
pizza_df['order_date'] = pd.to_datetime(pizza_df['order_date'], format='%Y-%m-%d')

# Créer la clé 'date_id' (format AAAAMMJJ)
pizza_df['date_id'] = pizza_df['order_date'].dt.strftime('%Y%m%d').astype(int)

# Construire la dimension temps unique
dim_temps = pizza_df[['date_id', 'order_date']].drop_duplicates().copy()
dim_temps['jour'] = dim_temps['order_date'].dt.day
dim_temps['mois'] = dim_temps['order_date'].dt.month
dim_temps['annee'] = dim_temps['order_date'].dt.year
dim_temps['trimestre'] = dim_temps['order_date'].dt.to_period('Q').astype(str)
dim_temps['jour_semaine'] = dim_temps['order_date'].dt.day_name(locale='fr_FR')

# Nettoyage final
dim_temps = dim_temps[['date_id', 'order_date', 'jour', 'mois', 'annee', 'trimestre', 'jour_semaine']].sort_values('date_id')

print("\n🕓 Aperçu de la dimension temps :")
print(dim_temps.head())


# ===========================
# 🍕 ETAPE 2 BIS : TRANSFORMATION (DIM_PIZZA)
# ===========================

# Sélectionner les colonnes utiles
dim_pizza = pizza_df[['pizza_id', 'pizza_name', 'pizza_category', 'pizza_size', 'unit_price', 'pizza_ingredients']].drop_duplicates()

# Renommer les colonnes pour correspondre au schéma en étoile
dim_pizza = dim_pizza.rename(columns={
    'pizza_id': 'pizza_id',
    'pizza_name': 'nom_pizza',
    'pizza_category': 'categorie',
    'pizza_size': 'taille',
    'unit_price': 'prix_unitaire',
    'pizza_ingredients': 'ingredients'
})

# Vérifier les types
dim_pizza['prix_unitaire'] = dim_pizza['prix_unitaire'].astype(float)

print("\n🍕 Aperçu de la dimension pizza :")
print(dim_pizza.head())


# ===========================
# 👤 ETAPE 2 TER : TRANSFORMATION (DIM_CLIENT)
# ===========================

# Sélectionner les colonnes pertinentes du fichier clients.csv
dim_client = clients_df[['client_id', 'nom', 'prenom', 'genre', 'age', 'email', 'telephone', 'pays', 'ville', 'code_postal']].drop_duplicates()

# Nettoyage de base : suppression des espaces, valeurs manquantes, types
dim_client['nom'] = dim_client['nom'].astype(str).str.strip()
dim_client['prenom'] = dim_client['prenom'].astype(str).str.strip()
dim_client['email'] = dim_client['email'].astype(str).str.lower()

# Gestion des valeurs manquantes dans le code postal
dim_client['code_postal'] = dim_client['code_postal'].fillna('')

# Vérification rapide
print("\n👤 Aperçu de la dimension client :")
print(dim_client.head())


# ===========================
# 💰 ETAPE 2 QUATER : TRANSFORMATION (FACT_VENTES)
# ===========================

# Pour cet exemple, on va attribuer aléatoirement des clients aux ventes d'ou import random


# On s'assure que le nombre de clients correspond bien à la taille du fichier clients.csv
nb_clients = len(dim_client)

# Ajouter un client_id aléatoire à chaque vente
pizza_df['client_id'] = [random.randint(1, nb_clients) for _ in range(len(pizza_df))]

# Sélectionner les colonnes nécessaires pour la table de faits
fact_ventes = pizza_df[['order_details_id', 'date_id', 'client_id', 'pizza_id', 'quantity', 'total_price']].copy()

# Renommer les colonnes pour correspondre au schéma SQL
fact_ventes = fact_ventes.rename(columns={
    'order_details_id': 'vente_id',
    'quantity': 'quantite',
    'total_price': 'total_prix'
})

# Vérification du résultat
print("\n💰 Aperçu de la table de faits (fact_ventes) :")
print(fact_ventes.head())


# ===========================
# 🏁 ETAPE 3 : LOAD (CHARGEMENT)
# ===========================

print("\n🚀 Démarrage du chargement dans la base SQLite...")

# Connexion à la base (au cas où elle était fermée plus haut)
conn = sqlite3.connect(DB_PATH)

# Charger les tables dans la base
dim_temps.to_sql('dim_temps', conn, if_exists='replace', index=False)
dim_pizza.to_sql('dim_pizza', conn, if_exists='replace', index=False)
dim_client.to_sql('dim_client', conn, if_exists='replace', index=False)
fact_ventes.to_sql('fact_ventes', conn, if_exists='replace', index=False)

# Validation et fermeture
conn.commit()
conn.close()

print("✅ Chargement terminé avec succès dans pizza_dw.db !")


# ===========================
# 🔒 Fin de la session
# ===========================

# Fermer proprement la connexion
conn.close()
print("🔒 Connexion fermée.")


# ===========================
# 🏁 ETAPE 3 : LOAD (CHARGEMENT)
# ===========================

print("\n🚀 Démarrage du chargement dans la base SQLite...")

# Connexion à la base (au cas où elle était fermée plus haut)
conn = sqlite3.connect(DB_PATH)

# Charger les tables dans la base
dim_temps.to_sql('dim_temps', conn, if_exists='replace', index=False)
dim_pizza.to_sql('dim_pizza', conn, if_exists='replace', index=False)
dim_client.to_sql('dim_client', conn, if_exists='replace', index=False)
fact_ventes.to_sql('fact_ventes', conn, if_exists='replace', index=False)

# Validation et fermeture
conn.commit()
conn.close()

print("✅ Chargement terminé avec succès dans pizza_dw.db !")


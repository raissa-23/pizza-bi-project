import pandas as pd
from faker import Faker
import random

# Initialiser Faker en français
fake = Faker('fr_FR')

# Nombre de clients à générer
N = 9000

# Pays et leurs villes associées
pays_villes = {
    "France": ["Paris", "Lyon", "Marseille", "Bordeaux", "Toulouse"],
    "Italie": ["Rome", "Milan", "Naples", "Turin", "Florence"],
    "Espagne": ["Madrid", "Barcelone", "Valence", "Séville", "Bilbao"],
    "Portugal": ["Lisbonne", "Porto", "Coimbra", "Faro", "Braga"],
    "Allemagne": ["Berlin", "Munich", "Hambourg", "Francfort", "Cologne"]
}

clients = []

for i in range(1, N+1):
    genre = random.choice(["M", "F"])
    age = random.randint(17, 70)
    prenom = fake.first_name_male() if genre == "M" else fake.first_name_female()
    nom = fake.last_name()
    email = f"{prenom.lower()}.{nom.lower()}_{i}@example.com"  # email unique
    telephone = fake.phone_number()
    pays = random.choice(list(pays_villes.keys()))
    ville = random.choice(pays_villes[pays])
    code_postal = fake.postcode() if pays == "France" else ""  # garder cohérent

    clients.append([i, nom, prenom, genre, age, email, telephone, pays, ville, code_postal])

# Convertir en DataFrame
df = pd.DataFrame(clients, columns=[
    "client_id","nom","prenom","genre","age","email","telephone","pays","ville","code_postal"
])

# Sauvegarder en CSV
df.to_csv("./data/clients.csv", index=False)

print("✅ clients.csv généré avec succès !")
print(df.head())

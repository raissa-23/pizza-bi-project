-- ===========================
-- 🍕 Pizza BI Data Warehouse
-- Schéma en étoile
-- ===========================

-- Supprime les tables si elles existent déjà (utile pour rejouer le script)
DROP TABLE IF EXISTS fact_ventes;
DROP TABLE IF EXISTS dim_client;
DROP TABLE IF EXISTS dim_pizza;
DROP TABLE IF EXISTS dim_temps;

-- ===========================
-- Table dimension client
-- ===========================
CREATE TABLE dim_client (
    client_id INTEGER PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    genre TEXT,
    age INTEGER,
    email TEXT,
    telephone TEXT,
    pays TEXT,
    ville TEXT,
    code_postal TEXT
);

-- ===========================
-- Table dimension pizza
-- ===========================
CREATE TABLE dim_pizza (
    pizza_id INTEGER PRIMARY KEY,
    nom_pizza TEXT,
    categorie TEXT,
    taille TEXT,
    prix_unitaire REAL,
    ingredients TEXT
);

-- ===========================
-- Table dimension temps
-- ===========================
CREATE TABLE dim_temps (
    date_id INTEGER PRIMARY KEY,
    date TEXT,
    jour INTEGER,
    mois INTEGER,
    annee INTEGER,
    trimestre TEXT,
    jour_semaine TEXT
);

-- ===========================
-- Table de faits : ventes
-- ===========================
CREATE TABLE fact_ventes (
    vente_id INTEGER PRIMARY KEY,
    date_id INTEGER,
    client_id INTEGER,
    pizza_id INTEGER,
    quantite INTEGER,
    total_prix REAL,
    FOREIGN KEY (date_id) REFERENCES dim_temps(date_id),
    FOREIGN KEY (client_id) REFERENCES dim_client(client_id),
    FOREIGN KEY (pizza_id) REFERENCES dim_pizza(pizza_id)
);

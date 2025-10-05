# 🍕 Pizza Data Warehouse Project

## 🎯 Objectif du projet
Ce projet a pour but de construire un mini **Data Warehouse** à partir d’un dataset de ventes de pizzas.  
Il simule un cas réel où une entreprise de restauration souhaite analyser ses ventes et mieux comprendre ses clients.  

## 🏛️ Architecture du projet

- **OLTP (source)** : dataset de ventes de pizzas (CSV).  
- **ETL** : extraction, transformation et chargement avec Python (pandas + SQLAlchemy).  
- **OLAP (cible)** : Data Warehouse en schéma en étoile (fact + dimensions).  
- **BI** : tableau de bord Power BI pour visualiser les KPIs.  

## 📊 Questions business adressées
- Quelles sont les pizzas les plus vendues ?  
- Quels sont mes meilleurs clients ?  
- Quels jours/heures enregistrent le plus de ventes ?  
- Quelle est l’évolution des ventes au fil du temps ?  

## 🛠️ Outils & technologies
- **Python** : pandas, SQLAlchemy (ETL).  
- **SQL** : PostgreSQL ou SQLite (Data Warehouse).  
- **Power BI** (visualisation).  
- **Git/GitHub** (versionning).  

## 🗂️ Structure du repo

```text
pizza-bi-project/
│── data/ # Fichiers CSV (source + clients fictifs)
│── sql/ # Schéma SQL (create_schema.sql)
│── etl/ # Scripts ETL en Python
│── bi/ # Dashboard Power BI ou captures d’écran
│── docs/ # Documentation (roadmap, Gantt, diagrammes)
│── README.md # Présentation du projet
```


## 🛣️ Roadmap (provisoire)
- [X] Collecte et préparation des données (pizza_sales.csv + clients.csv)  
- [ ] Modélisation du schéma en étoile (SQL)  
- [ ] Développement du pipeline ETL (Python)  
- [ ] Création du Data Warehouse (PostgreSQL/SQLite)  
- [ ] Tableaux de bord Power BI  
- [ ] Documentation finale + screenshots


## 📂 Datasets disponibles

- **pizza_sales.csv** : dataset des ventes de pizzas (source Kaggle).
- **clients.csv** : dataset fictif généré (9 000 clients) avec noms, prénoms, genre, âge, email, téléphone, pays, ville, code postal.

## Diagramme du schéma en étoile de notre Data Warehouse
    
```mermaid
erDiagram
    dim_client {
        int client_id PK
        string nom
        string prenom
        string genre
        int age
        string email
        string telephone
        string pays
        string ville
        string code_postal
    }

    dim_pizza {
        int pizza_id PK
        string nom_pizza
        string categorie
        string taille
        float prix_unitaire
        string ingredients
    }

    dim_temps {
        int date_id PK
        date date
        int jour
        int mois
        int trimestre
        int annee
        string jour_semaine
    }

    fact_ventes {
        int vente_id PK
        int client_id FK
        int pizza_id FK
        int date_id FK
        int quantite
        float total_prix
    }

    dim_client ||--o{ fact_ventes : "client_id"
    dim_pizza ||--o{ fact_ventes : "pizza_id"
    dim_temps ||--o{ fact_ventes : "date_id"
</div>
```

---
🚀 Projet en cours de développement

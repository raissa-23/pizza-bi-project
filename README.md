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
- [ ] Collecte et préparation des données (pizza_sales.csv + clients.csv)  
- [ ] Modélisation du schéma en étoile (SQL)  
- [ ] Développement du pipeline ETL (Python)  
- [ ] Création du Data Warehouse (PostgreSQL/SQLite)  
- [ ] Tableaux de bord Power BI  
- [ ] Documentation finale + screenshots  

---
🚀 Projet en cours de développement

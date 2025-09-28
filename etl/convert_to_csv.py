import pandas as pd
from pathlib import Path

# Définir chemins
data_dir = Path("./data")
excel_file = data_dir / "Data Model - Pizza Sales.xlsx"
csv_file = data_dir / "pizza_sales.csv"

# Charger l'Excel
df = pd.read_excel(excel_file)

# Sauvegarder en CSV
df.to_csv(csv_file, index=False)

print(f"✅ Conversion terminée : {csv_file}")
print(df.head())

# eda_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("data/covid_sample.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Summary stats
print("\n--- Dataset Info ---")
print(df.info())
print("\n--- Basic Statistics ---")
print(df.describe())

# Total confirmed cases by country
total_by_country = df.groupby('Country')['Confirmed'].sum().sort_values(ascending=False)
print("\n--- Total Confirmed Cases by Country ---")
print(total_by_country)

# Plot: Total confirmed cases by country
plt.figure(figsize=(8,5))
sns.barplot(x=total_by_country.index, y=total_by_country.values)
plt.title("Total Confirmed Cases by Country")
plt.ylabel("Total Confirmed Cases")
plt.xlabel("Country")
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df[['Confirmed', 'Deaths', 'Recovered', 'Active']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

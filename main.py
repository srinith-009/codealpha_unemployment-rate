import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For parsing and working with dates
from datetime import datetime
# Load data
df = pd.read_csv("Unemployment in India.csv")

# Rename columns for simplicity
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Remove leading/trailing spaces from date strings
df['Date'] = pd.to_datetime(df['Date'].str.strip(), format='%d-%m-%Y')

# Check for missing values
print(df.isnull().sum())
print(df.describe())
print(df['Region'].nunique(), "states/regions available")
# Group by date for national trends
national_avg = df.groupby('Date')['Estimated_Unemployment_Rate_(%)'].mean()

plt.figure(figsize=(12,6))
plt.plot(national_avg.index, national_avg.values, color='blue')
plt.title("Average Unemployment Rate in India Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.show()
covid_df = df[(df['Date'] >= "2020-03-01") & (df['Date'] <= "2021-03-31")]
covid_avg = covid_df.groupby('Date')['Estimated_Unemployment_Rate_(%)'].mean()

plt.figure(figsize=(12,6))
plt.plot(covid_avg.index, covid_avg.values, color='red')
plt.title("Unemployment Rate During COVID-19 (India)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.show()
df['Month'] = df['Date'].dt.strftime('%Y-%m')

heatmap_df = df.groupby(['Region', 'Month'])['Estimated_Unemployment_Rate_(%)'].mean().unstack()

plt.figure(figsize=(14,10))
sns.heatmap(heatmap_df, cmap="YlGnBu", linewidths=0.5)
plt.title("Heatmap of Unemployment Rate by Region & Month")
plt.ylabel("Region")
plt.xlabel("Month")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

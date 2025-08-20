#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a plot style for better aesthetics
plt.style.use('seaborn-v0_8-whitegrid')

# URL to the raw COVID-19 confirmed cases data from JHU CSSE
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

# Read the data into a Pandas DataFrame
df = pd.read_csv(url)

# Display the first few rows to inspect the data structure
print(df.head())


# In[2]:


# Melt the DataFrame to convert from wide to long format
df_melted = df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    var_name='Date',
    value_name='Confirmed'
)

# Convert the 'Date' column to datetime objects
df_melted['Date'] = pd.to_datetime(df_melted['Date'], format='%m/%d/%y')

# Aggregate the data to get total confirmed cases per country per day
df_cleaned = df_melted.groupby(['Country/Region', 'Date']).sum().reset_index()

print(df_cleaned.head())


# In[3]:


# Select a few countries for comparison
countries_to_plot = ['US', 'India', 'Brazil', 'United Kingdom', 'China']
df_filtered = df_cleaned[df_cleaned['Country/Region'].isin(countries_to_plot)]

# Use Seaborn's lineplot for an easy-to-read, professional plot
plt.figure(figsize=(12, 6))
sns.lineplot(
    data=df_filtered,
    x='Date',
    y='Confirmed',
    hue='Country/Region',
    marker='o',
    dashes=False
)
plt.title('Cumulative Confirmed COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Confirmed Cases')
plt.legend(title='Country')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[4]:


# Choose a single country to analyze daily new cases
country_to_analyze = 'India'
df_country = df_cleaned[df_cleaned['Country/Region'] == country_to_analyze].copy()

# Calculate daily new cases using .diff()
df_country['New Cases'] = df_country['Confirmed'].diff().fillna(0)

# Calculate a 7-day rolling average to smooth the trend
df_country['Rolling Average'] = df_country['New Cases'].rolling(window=7).mean()

# Plot both the raw daily new cases and the rolling average
plt.figure(figsize=(12, 6))
plt.plot(df_country['Date'], df_country['New Cases'], label='Daily New Cases', alpha=0.5)
plt.plot(df_country['Date'], df_country['Rolling Average'], color='red', linewidth=3, label='7-Day Rolling Average')
plt.title(f'Daily New COVID-19 Cases and Rolling Average in {country_to_analyze}')
plt.xlabel('Date')
plt.ylabel('Number of New Cases')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[5]:


# Get the latest date in the dataset
latest_date = df_cleaned['Date'].max()

# Filter data for the latest date and get the top 15 countries
df_latest = df_cleaned[df_cleaned['Date'] == latest_date].sort_values(by='Confirmed', ascending=False).head(15)

# Create a bar plot using Seaborn
plt.figure(figsize=(12, 8))
sns.barplot(
    data=df_latest,
    x='Confirmed',
    y='Country/Region',
    palette='viridis'
)
plt.title(f'Total Confirmed COVID-19 Cases by Country (As of {latest_date.strftime("%B %d, %Y")})')
plt.xlabel('Total Confirmed Cases')
plt.ylabel('Country/Region')
plt.tight_layout()
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: Set a clean style for the plots
sns.set_style("whitegrid")
plt.style.use("seaborn-v0_8-whitegrid")

# Load the built-in Iris dataset from Seaborn
iris = sns.load_dataset('iris')

# Display the first few rows to confirm the data is loaded correctly
print(iris.head())


# In[2]:


# Plot the distribution of petal_length, colored by species
plt.figure(figsize=(10, 6))
sns.histplot(data=iris, x='petal_length', hue='species', multiple='stack', kde=True)
plt.title('Distribution of Petal Length by Species')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()


# In[3]:


# Create a scatter plot of petal length vs. petal width
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=iris,
    x='petal_length',
    y='petal_width',
    hue='species',
    style='species',
    s=100
)
plt.title('Petal Length vs. Petal Width')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.show()


# In[5]:


# Create a pair plot for the entire dataset
sns.pairplot(iris, hue='species')
plt.suptitle('Pair Plot of the Iris Dataset', y=1.02)
plt.show()


# In[ ]:





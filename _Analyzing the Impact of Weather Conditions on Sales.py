#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create and define the sales data
np.random.seed(42)
sales_data = pd.DataFrame({
    'date': pd.date_range(start='2022-01-01', end='2022-12-31', freq='D'),
    'sales': np.random.normal(1000, 200, 365)
})

# Create and define the weather data
weather_data = pd.DataFrame({
    'date': pd.date_range(start='2022-01-01', end='2022-12-31', freq='D'),
    'temperature': np.random.normal(60, 10, 365),
    'precipitation': np.random.uniform(0, 1, 365)
})

# Merge the sales and weather data
data = pd.merge(sales_data, weather_data, on='date')

# Visualize the relationship between sales and temperature
sns.scatterplot(x='temperature', y='sales', data=data)
plt.title('Impact of Temperature on Sales')
plt.xlabel('Temperature (F)')
plt.ylabel('Sales')
plt.show()

# Visualize the relationship between sales and precipitation
sns.scatterplot(x='precipitation', y='sales', data=data)
plt.title('Impact of Precipitation on Sales')
plt.xlabel('Precipitation (Inches)')
plt.ylabel('Sales')
plt.show()


# In[ ]:





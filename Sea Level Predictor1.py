#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


sea_level_data=pd.read_csv(r'/Users/user/Documents/FreeCodeCamp/epa-sea-level.csv')


# In[4]:


sea_level_data.head()


# In[5]:


import matplotlib.pyplot as plt
from scipy.stats import linregress


# In[6]:


# Scatter plot of Year vs CSIRO Adjusted Sea Level
plt.figure(figsize=(10, 5))
plt.scatter(sea_level_data['Year'], sea_level_data['CSIRO Adjusted Sea Level'], edgecolor='k', alpha=0.7)


# In[7]:


# Perform linear regression on all data
slope_all, intercept_all, r_value, p_value, std_err = linregress(sea_level_data['Year'], sea_level_data['CSIRO Adjusted Sea Level'])


# In[8]:


# Predict sea level change through year 2050 for all data
years_extended = pd.Series(range(1880, 2051))
sea_level_predicted_all = intercept_all + slope_all * years_extended


# In[9]:


# Plot the line of best fit for all data
plt.plot(years_extended, sea_level_predicted_all, 'r', label='All years fit')


# In[10]:


# Perform linear regression using data from year 2000 through the most recent year in the dataset
data_from_2000 = sea_level_data[sea_level_data['Year'] >= 2000]
slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(data_from_2000['Year'], data_from_2000['CSIRO Adjusted Sea Level'])


# In[11]:


# Predict sea level change through year 2050 from 2000
sea_level_predicted_2000 = intercept_2000 + slope_2000 * years_extended


# In[12]:


# Plot the line of best fit from 2000
plt.plot(years_extended, sea_level_predicted_2000, 'g', label='Year 2000 onward fit')


# In[13]:


# Adding the labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')


# In[14]:


# Show legend
plt.legend()


# In[15]:


# Show the plot
plt.show()


# In[ ]:





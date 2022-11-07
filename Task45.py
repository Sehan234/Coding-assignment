#!/usr/bin/env python
# coding: utf-8

# In[343]:


# Task 4

import json
import requests

# Defining the API with latitudes and longitudes for Helsinki, product as CIVIL and output type to be JSON
api = 'http://www.7timer.info/bin/api.pl?lon=24.945831&lat=60.192059&product=civil&output=json'

# Making a request from the API, the JSON response is converted to a Python dictionary object
response = requests.get(api).json() 


# In[344]:


response # Display the Python dict


# In[345]:


type(response)


# In[346]:


type(response['dataseries'])


# In[347]:


# Task 5
import pandas as pd

df1 = pd.DataFrame(response)   # Convert the dict object to pandas dataframe


# In[348]:


# Convert the 'dataseries' dictionary to a pandas dataframe

df2 = pd.DataFrame(response['dataseries']) 


# In[349]:


# Convert 'wind10m' to a dataframe
wind = df2.wind10m 
df3 = pd.DataFrame.from_records(wind) 

# Change column names
df3 = df3.rename(columns={'direction': 'wind direction','speed': 'wind speed'})


# In[350]:


# Drop 'wind10m' from df2 and concatenate df4 and df3
df4 = df2.drop(['wind10m'], axis = 1)
df5 = pd.concat([df4, df3], axis=1)


# In[351]:


# Drop 'dataseries' from df1 and concatenate df6 and df5
df6 = df1.drop(['dataseries'], axis = 1)
df_final = pd.concat([df6,df5], axis=1)
print(df_final)


# In[352]:


df_final.to_csv('helsinkiweather.csv') # Export dataframe into csv format


# In[ ]:





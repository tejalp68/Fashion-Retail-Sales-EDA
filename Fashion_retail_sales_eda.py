#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis

# ### Exploratory Data Analysis (EDA) is an approach to analyzing data sets to summarize their main characteristics, often using statistical graphics and other data visualization methods

# In[4]:


# importing libraries


# In[5]:


import pandas  as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')


# In[6]:


# importing dataset


# In[7]:


df=pd.read_csv("Fashion_Retail_Sales.csv")
df


# In[8]:


df.info()


# In[9]:


df.describe()


# In[10]:


# finding null values per column
df.isnull().sum()


# In[11]:


df.nunique


# In[12]:


df.columns


# In[13]:


df.head(20)


# In[14]:


df['Review Rating'] = df['Review Rating'].fillna(df['Review Rating'].mode()[0])
df['Purchase Amount (USD)'] = df['Purchase Amount (USD)'].fillna(df['Purchase Amount (USD)'].mean())


# In[15]:


df


# In[16]:


df.isnull().sum()


# In[17]:


plt.hist(df['Purchase Amount (USD)'].head(50) , color= 'orange',edgecolor='black')
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("ITEM PRICE")
plt.show()


# In[18]:


df.head(20)


# In[25]:


plt.pie(df['Review Rating'].head(10) ,labels=df["Item Purchased"].head(10) ,autopct ='%1.0f%%')
plt.title("Pie chart of Review Rating and Item Purchased")

plt.show()


# In[ ]:


df['Payment Method'].head(10).info


# In[ ]:


count = df['Payment Method'].value_counts()
print(count)



# In[ ]:





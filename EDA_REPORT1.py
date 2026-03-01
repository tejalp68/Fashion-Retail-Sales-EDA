# In[]:
# importing libraries

# In[]:
import pandas  as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

import warnings
warnings.filterwarnings('ignore')

# In[]:
# importing dataset


# In[]:
df=pd.read_csv("Fashion_Retail_Sales.csv")
df

# In[]:
df.info()

# In[]:
df.describe()

# In[]:
# finding null values per column
df.isnull().sum()

# In[]:
df.nunique

# In[]:
df.columns

# In[]:
df.head(20)

# In[]:
df['Review Rating'] = df['Review Rating'].fillna(df['Review Rating'].mode()[0])
df['Purchase Amount (USD)'] = df['Purchase Amount (USD)'].fillna(df['Purchase Amount (USD)'].mean())


# In[]:
df

# In[]:
df.isnull().sum()

# In[]:
plt.hist(df['Purchase Amount (USD)'].head(50) , color= 'orange',edgecolor='black')
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("ITEM PRICE")
plt.show()

# In[]:
df.head(20)

# In[]:
plt.pie(df['Review Rating'].head(10) ,labels=df["Item Purchased"].head(10) ,autopct ='%1.0f%%')
plt.title("Pie chart of Review Rating and Item Purchased")

plt.show()

# In[]:
df['Payment Method'].head(10).info

# In[]:
count = df['Payment Method'].value_counts()
print(count)



# In[]:



#!/usr/bin/env python
# coding: utf-8

# # Method 1: using isnull function

# In[23]:


import pandas as pd
import numpy as np

data = {'x': [1,2,3,4,5,np.nan,6,7,np.nan,8,9,10,np.nan],
        'y': [11,12,np.nan,13,14,np.nan,15,16,np.nan,np.nan,17,np.nan,19]}
df = pd.DataFrame(data)

print (df)


# In[36]:


# checking NaN in a cell

pd.isnull(df.iloc[5,0])


# # Method 2: using isnan function

# In[42]:


# We can also check the cell NaN value in dataframe
data = {'x': [1,2,3,4,5,np.nan,6,7,np.nan,8,9,10,np.nan],
        'y': [11,12,np.nan,13,14,np.nan,15,16,np.nan,np.nan,17,np.nan,19]}
df = pd.DataFrame(data)
print(df)
value = df.at[5, 'x']  #nan
isNaN = np.isnan(value)
print("===============")
print("Is value at df[5, 'x'] NaN :", isNaN)


# # Method 3: using isnan in series

# In[34]:


# We can also check the cell NaN value in dataframe series

series_df = pd.Series([2,3,np.nan,7,25])

print(series_df)
value = series_df[2]  #nan
isNaN = np.isnan(value)
print("===============")
print("Is value at df[2] NaN :", isNaN)


# # Method 4: using pandas.isna

# In[41]:



data = {'x': [1,2,3,4,5,np.nan,6,7,np.nan,8,9,10,np.nan],
        'y': [11,12,np.nan,13,14,np.nan,15,16,np.nan,np.nan,17,np.nan,19]}
df = pd.DataFrame(data)

print (df)

print("checking NaN value in cell [5, 0]")
pd.isna(df.iloc[5,0])


# # Method 5: using pandas.notnull method

# In[39]:



data = {'x': [1,2,3,4,5,np.nan,6,7,np.nan,8,9,10,np.nan],
        'y': [11,12,np.nan,13,14,np.nan,15,16,np.nan,np.nan,17,np.nan,19]}
df = pd.DataFrame(data)

print (df)

print("checking NaN value in cell [5, 0]")
pd.notnull(df.iloc[5,0])


# In[ ]:





# In[ ]:





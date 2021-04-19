#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


path = '../data/'


# In[3]:


df = pd.read_csv(path+'sp500_closefull.csv', index_col='Date', parse_dates=True)


# In[4]:


df.head()


# In[6]:


df.shape


# In[7]:


# drop any columns with more 10 or more missing values
df.dropna(axis=1, thresh=len(df) - 10, inplace=True)


# In[8]:


# forward fill and backfill
df.fillna(method='ffill', inplace=True)


# In[9]:


df.fillna(method='bfill', inplace=True)


# In[10]:


all_dates = df.index.unique().sort_values()


# In[11]:


start = all_dates.get_loc('2014-01-02')
end = all_dates.get_loc('2017-06-30')
dates = all_dates[start:end+1]


# In[12]:


# empty dataframe
returns = pd.DataFrame(index=all_dates[1:])


# In[13]:


for name in df.columns:
  current_returns = np.log(df[name]).diff()
  returns[name] = current_returns.iloc[1:]


# In[14]:


X = returns.to_numpy()


# In[15]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)


# In[16]:


X.shape


# In[17]:


from sklearn.decomposition import PCA
model = PCA()
Z = model.fit_transform(X)


# In[18]:


plt.plot(model.explained_variance_ratio_);


# In[19]:


plt.plot(model.explained_variance_ratio_[:10]);


# In[20]:


cumulative_variance = np.cumsum(model.explained_variance_ratio_)
plt.plot(cumulative_variance);


# In[21]:


# Plot first principal component vs S&P
plt.plot(Z[:,0]);


# In[22]:


Z_df = pd.DataFrame(index=returns.index)
Z_df['PC1'] = Z[:,0]


# In[24]:


spy = pd.read_csv(path+'SPY.csv', index_col='Date', parse_dates=True)


# In[25]:


spy_returns = -np.log(spy['Close']).diff().dropna()
spy_returns.plot();


# In[26]:


joined = Z_df.join(spy_returns)


# In[27]:


joined.columns = ['PC1', 'SPY']

scaler2 = StandardScaler()
joined[['PC1', 'SPY']] = scaler2.fit_transform(joined)


# In[28]:


joined.plot(figsize=(10, 5), alpha=0.7);


# In[ ]:





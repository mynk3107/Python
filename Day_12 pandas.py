#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
#df = pd.read_csv('orders.txt',parse_dates=['order_date'])

df = pd.read_csv('orders.txt')
df['order_date']=pd.to_datetime(df['order_date'])
df.dtypes


# In[26]:


print(pd. __version__)


# In[28]:


dates = ['2020/15/01','2021-04-05']
#pd.to_datetime(dates, format = '%Y$%m$%d')
pd.to_datetime(dates, format='mixed',errors='ignore')


# In[54]:


df = pd.read_csv('orders.txt',parse_dates=['order_date'],index_col='order_date')
df.loc['2020-01-01':'2020-01-05']
df.sort_index(inplace=True)
df.loc['2020-01-01' :'2020-03-01']
df.loc['2020-01-01':'2020-01-05']


# In[57]:


df.dtypes


# In[63]:


df['order_date'].dt.day_name()


# In[64]:


#pip install matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')


# In[67]:


df.plot('category','sales',kind='bar')


# In[68]:


df = pd.read_csv('orders.txt',parse_dates=['order_date'],index_col='order_date')


# In[70]:


df['sales'].plot(kind=)


# In[74]:


df.groupby('city')['sales'].sum().plot(kind='bar')


# In[81]:


df['profit'].resample('Q').sum().plot(title='my first chart')


# In[ ]:





# In[86]:


#df['sales_int']= df['sales'].astype('int')
df


# In[ ]:





# In[96]:


#import numpy as np
#df = pd.read_csv('orders.txt')
#df.dtypes
#df['sales'].fillna(0).astype('int')
df[df['sales'].isna()]


# In[101]:


df.pivot_table(index = 'city' , columns ='category' , values='sales' , aggfunc='sum')


# In[116]:


#pip install openpyxl
df=pd.read_excel('orders.xlsx',sheet_name=1)
df


# In[118]:


#df.to_excel('orders_2.xlsx',sheet_name='orders')
#df.to_json('returns.json')
df_json = pd.read_json('returns.json')


# In[119]:


df_json


# In[126]:


import pyarrow
#df.to_parquet('orders_p.parquet',engine='pyarrow')
df_pd1=pd.read_parquet('orders_p.parquet',engine='pyarrow')
df_pd1


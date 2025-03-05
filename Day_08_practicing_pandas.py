# the code is written in jupyter kernel

#!/usr/bin/env python
# coding: utf-8

# In[3]:
emp = {'name':'Ankit', 'gender':'Male', 'email':'ankit@gmail.com'}
emp= {"name":["Ankit","Rahul","Priya"],"gender":["Male","Male","Female"], "email":["ankit@gmail.com","rahul@gmail.com","priya@gmail.com"] }
emp


# In[4]:
import pandas as pd


# In[6]:
df_emp = pd.DataFrame(emp)
df_emp


# In[16]:
type(df_emp['name'])
#df_emp.info()
#df_emp.describe()


# In[17]:
df_emp


# In[21]:


#iloc is index/integer based
df_emp.iloc[1,2]
df_emp.iloc[1:3,0:2]
df_emp.iloc[1:3,0:2]


# In[25]:


# specific rows / columns
df_emp.iloc[[0,2],[0,2]]


# In[26]:


#loc is labeled based
df_emp


# In[34]:


df_emp.loc[0:2,'name':'gender']


# In[48]:


df_emp.set_index('email',inplace=True)


# In[59]:


df_emp
df_emp.sort_index(ascending=False)


# In[56]:


df_emp.loc['priya@gmail.com','name']
df_emp.loc['ankit@gmail.com':'priya@gmail.com','name':'gender']
df_emp.iloc[0:2]


# In[61]:


df_emp.reset_index(inplace=True)


# In[47]:


df_emp


# In[63]:


fc= (df_emp['gender']=='Male')
fc


# In[67]:


df_emp[fc]


# In[69]:


fci = ~(df_emp['gender']=='Male')
fci


# In[70]:


df_emp[fci]


# In[71]:


fcn = (df_emp['gender']!='Male')
df_emp[fcn]


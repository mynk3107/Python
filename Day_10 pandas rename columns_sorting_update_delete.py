 #!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd
emp= {"name":["Ankit","Rahul","Priya"],"gender":["Male","Male","Female"], "email":["ankit@gmail.com","rahul@gmail.com","priya@gmail.com"] }
df1 = pd.DataFrame(emp)
df1


# In[10]:


#pandas #dataframe #how to create #iloc #loc #filter data
fc = (df_emp['name']=='Ankit')
#df_emp[fc]
df.loc[fc , ['gender']]


# In[16]:


df.index  = [0,1,2]
df


# In[19]:


#df[fc]
df.loc[fc]


# In[21]:


df.columns


# In[31]:


df.columns = ['emp','gender','emp_email' ]
df


# In[27]:


df.rename(columns = {'emp_name':'name', 'emp_email':'email'},inplace=True)
df


# In[35]:


df.loc[0] = ['Ankitt','Male','ankitt@gmail.com']
df


# In[39]:


df.loc[0] = ['Ankitt','Male','ankitt@gmail.com']


# In[46]:


df.loc[0,['name','email']] = ['Ankit','ankit@gmail.com']


# In[47]:


df


# In[51]:


fc = (df['gender'] == 'Male')
df.loc[fc,'gender'] = 'Female'


# In[52]:


df


# In[57]:


#fc = (df['gender'] == 'Male')
df.loc[fc,'gender'] = 'Male'


# In[58]:


df


# In[55]:


df.iloc[:,1] = 'female'


# In[56]:


df


# In[61]:


df['gender'].apply(len)


# In[69]:


def update_email(inputval):
    return inputval.upper()


# In[63]:


df['email'].apply(update_email)


# In[65]:


df['email'] = df['email'].apply(update_email)


# In[66]:


df


# In[70]:


df.applymap(update_email)


# In[71]:


df


# In[79]:


df['name'].str.lower()


# In[84]:


df['name'] = df['name'].str.startswith('a')


# In[86]:


df.info()


# In[87]:


df


# In[88]:


emp= {"name":["Ankit","Rahul","Priya"],"gender":["Male","Male","Female"], "email":["ankit@gmail.com","rahul@gmail.com","priya@gmail.com"] }
df = pd.DataFrame(emp)
df


# In[89]:


df['salary'] = 10000
df


# In[90]:


df['name_gender'] = df['name'] + ' ' + df['gender']


# In[91]:


df


# In[92]:


df['salary'] = 20000
df


# In[93]:


df.loc[(df['name']=='Ankit') , 'salary'] = 5000


# In[98]:


df


# In[97]:


df['salary1'] = [5000,6000,7000]


# In[102]:


#delete rows
#df.drop(index = 0 , inplace=True)
df.drop(index = 0 )


# In[105]:


fc = (df['salary'] >= 6000)
fc


# In[110]:


df.drop(index = df[fc].index )


# In[112]:


df[fc].index


# In[113]:


df


# In[115]:


#delete a column
df.drop(columns='salary1')


# In[126]:


df


# In[128]:


df.sort_values(by = 'name', inplace=True)


# In[130]:


df.sort_values(by = 'salary', ascending=False)


# In[133]:


df.sort_values(by = ['gender','salary'], ascending=[False,True])


# In[135]:


df.sort_values(by = ['gender','salary'], ascending=False, inplace=True)


# In[ ]:





# In[141]:


df.sort_index(ascending=False)


# In[ ]:





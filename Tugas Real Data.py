#!/usr/bin/env python
# coding: utf-8

# # TUGAS DATA MINING

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


beeptest=pd.read_csv('beeptest.csv','sep',';')
beeptest


# In[3]:


vo2max=pd.read_csv('vo2max.csv','sep',';')
vo2max


# In[4]:


hasil=pd.merge(beeptest,vo2max,on='Nama')
hasil


# In[8]:


hasil1 = hasil.drop(['Keterangan'], axis=1)


# In[9]:


hasil1


# In[11]:


hasil2=hasil.drop([6])
hasil2


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# ##LATIHAN##

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


import csv
siswa=[
    ('adinda','A','90'),
    ('bayu','AB','84'),
    ('caca','A','89'),
    ('dodi','C','65'),
    ('eline','B','75')
]


# In[5]:


siswa


# In[6]:


f = open('siswa.csv', 'w')
w = csv.writer(f)
w.writerow(('Nama','Kelas','Nilai'))


# In[7]:


siswa


# In[8]:


f


# In[10]:


for s in siswa:
    w.writerow(s)


# In[11]:


f.close()


# In[14]:


reader = csv.reader(f)


# In[ ]:





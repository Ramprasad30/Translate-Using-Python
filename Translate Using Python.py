#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install googletrans==3.1.0a0


# In[3]:


import pandas as pd
from googletrans import Translator


# In[4]:


translator = Translator()


# In[5]:


data = pd.read_csv("hindi.csv")
print(data)


# In[6]:


translations = {}
for column in data.columns:
    unique = data[column].unique()
    for element in unique:
        translations[element] = translator.translate(element).text
for i in translations.items():
    print(i)


# In[7]:


data.replace(translations, inplace=True)
print(data)


# In[ ]:





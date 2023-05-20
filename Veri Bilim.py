#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


# In[5]:


netflix= pd.read_csv ("netflix_titles.csv")


# In[6]:


netflix.head()


# In[12]:


netflix.shape


# In[13]:


netflix.columns


# In[14]:


netflix.isnull().sum()


# In[16]:


netflix.nunique()


# In[11]:


data=netflix.copy()


# In[12]:


data.shape


# In[87]:


data=data.dropna()


# In[15]:


data



# In[16]:


data.shape


# In[92]:


plt.figure(figsize=(2,1))
sns.countplot(data=netflix, x="type");
plt.title("tür ve reyting oranları");
plt.show()


# In[ ]:





# In[72]:


sns.countplot(data=netflix, x="rating");


# In[73]:


plt.figure(figsize=(17,5))
sns.countplot(x="rating", hue="type",data=netflix);
plt.title("tür ve reyting oranları");
plt.show()


# In[86]:


labels=["Movie","TV show"]
size=netflix["type"].value_counts()
colors=plt.cm.nipy_spectral(np.linspace(0,1,2))
explode=[0,0.1]
plt.rcParams["figure.figsize"]=(9,9)
plt.pie(size,labels=labels,colors=colors,explode=explode,shadow=True,startangle=90)
plt.title("Tür görünümü",fontsize=25)
plt.legend()
plt.show()


# In[96]:


netflix["rating"].value_counts().plot.pie(autopct="%1.1f%%",shadow=True,figsize=(10,8))  
plt.show()






# In[147]:


pip install WordCloud


# In[152]:


from wordcloud import WordCloud  


# In[160]:


plt.subplots(figsize=(25,15))
worldcloud=WordCloud(
    background_color="turquoise",
    mode="RGB",
    width=1920,
    height=1080,
).generate(" ".join(data.country))
plt.imshow(worldcloud)
plt.axis("off")
plt.savefig("country.png")
plt.show()


# In[158]:


plt.subplots(figsize=(25,15))
worldcloud=WordCloud(
    background_color="gray",
    mode="RGB",
    width=1920,
    height=1080,
).generate(" ".join(data.director))
plt.imshow(worldcloud)
plt.axis("off")
plt.savefig("director.png")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





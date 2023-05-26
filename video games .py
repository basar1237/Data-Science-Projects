#!/usr/bin/env python
# coding: utf-8

#  # VİDEO GAMES SALES

# In[194]:


import numpy as np
import pandas as pd
import scipy.stats as st
pd.set_option("display.max_columns",None)


# In[195]:


import sklearn
print(sklearn.__version__)


# In[196]:


pip install --upgrade scikit-learn


# In[197]:


from sklearn.preprocessing import StandardScaler


# In[198]:


pip install missingno


# In[199]:


import math
import seaborn as sns
sns.set_style("whitegrid")
import missingno as msno #veri setindeki eksik verileri görselleştirirsek işimize yarar
from sklearn.preprocessing import StandardScaler


# In[200]:


data=pd.read_csv("vgsales.csv")
data


# In[207]:


data.shape


# In[208]:


data.head()


# In[209]:


data.isnull().sum()# yıl dütununda eksik veriler var ve publisher da 


# In[210]:


drop_row_index=data[data["Year"]>2015].index
data=data.drop(drop_row_index)


# In[211]:


data.info()


# In[212]:


data.shape


# In[213]:


data.describe()


# In[214]:


data.describe(include=["object","bool"])


# In[215]:


data["Genre"].value_counts()


# In[216]:


import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
sns.countplot(x="Genre",data=data,order=data["Genre"].value_counts().index)
plt.xticks(rotation=90)
plt.show()


# In[217]:


plt.figure(figsize=(15,10))
sns.countplot(x="Year",data=data_year)
plt.xticks(rotation=90)
plt.show()


# In[218]:


plt.figure(figsize=(30,10))
sns.countplot(x="Year",data=data,hue="Genre",order=data.Year.value_counts().iloc[:5].index)
plt.xticks(rotation=90,size=10)
plt.show()#en çok oyunun çıktığı 5 yılı gösterdk 


# # dünya genelinde en yüksek satış değerlerine sahip olanları belirleme 

# In[219]:


data_year=data.groupby(by=["Year"])["Global_Sales"].sum()
data_year=data_year.reset_index()
                                    


# In[ ]:





# In[220]:


plt.figure(figsize=(15,10))
sns.barplot(x="Year",y="Global_Sales",data=data_year)
plt.xticks(rotation=90)
plt.show() # küresel satış sütununu kullaranark hangi yılın dünya genelinde en yüksek satışa sahip olduğunu  görebilriiz
## 2008 en fazla 2009 da da çok am asonr adüşmüşş


# # bir yılda en çok ahangı oyun turunun yayımlandıgını  belırleyebılırız  bunun ıcın yıl ve tur sutunlarına göre  grupkama yapabılrız 

# In[ ]:





# In[221]:


year_max_df=data.groupby(by=["Year","Genre"]).size().reset_index(name="count")
year_max_idx=year_max_df.groupby(["Year"])["count"].transform(max)==year_max_df["count"]
year_max_genre=year_max_df[year_max_idx].reset_index(drop=True)
year_max_genre=year_max_genre.drop_duplicates(subset=["Year","count"],keep="last").reset_index(drop=True)


# In[222]:


genre=year_max_genre["Genre"].values


# In[223]:


genre


# In[224]:


plt.figure(figsize=(30,15))
g=sns.barplot(x="Year",y="count",data=year_max_genre)
index=0
for value in year_max_genre["count"].values:
     g.text(index,value+5,str(genre[index]+"------" +str(value)),color="#000",size=14,rotation=90,ha="center")
     index+=1
plt.xticks(rotation=90)
plt.show()

       
       


# # BİR YILDA EN ÇOK SATIŞ MİKTARI 

# In[225]:


year_sale_dx=data.groupby(by=["Year","Genre"])["Global_Sales"].sum().reset_index()
year_sale=year_sale_dx.groupby(["Year"])["Global_Sales"].transform(max)==year_sale_dx["Global_Sales"]
year_sale_max=year_sale_dx[year_sale].reset_index(drop=True)


# In[226]:


genre=year_sale_max["Genre"]


# In[227]:


plt.figure(figsize=(30,15))
g=sns.barplot(x="Year",y="Global_Sales",data=year_sale_max)
index=0
for value in year_sale_max["Global_Sales"]:
     g.text(index,value+5,str(genre[index]+"------" +str(value)),color="#000",size=14,rotation=90,ha="center")
     index+=1
plt.xticks(rotation=90)
plt.show()


# # küresel olarak en yuksek satış fıyatına sahıp oyun türü hangi tür oyunlar daha fazla satılmış

# In[ ]:





# In[228]:


data_genre=data.groupby(by=["Genre"])["Global_Sales"].sum()
data_genre=data_genre.reset_index()
data_genre=data_genre.sort_values(by=["Global_Sales"],ascending=False)


# In[229]:


plt.figure(figsize=(30,15))
sns.barplot(x="Genre",y="Global_Sales",data=data_genre)
plt.xticks(rotation=90)
plt.show()


# #  küresel anlamda en yuksek satıs fıuaytına ya da degerıene sahıp oyun platformunu bulalaım 

# In[230]:


data_platform=data.groupby(by=["Platform"])["Global_Sales"].sum()


# In[231]:


data_platform=data_platform.reset_index()
data_platform=data_platform.sort_values(by=["Global_Sales"],ascending=False)
plt.figure(figsize=(30,15))
sns.barplot(x="Platform",y="Global_Sales",data=data_platform)
plt.xticks(rotation=90)
plt.show()


# # en yuksek satısa sahıp bıreysel oyun 

# In[232]:


top_game_sale=data.head()
top_game_sale=top_game_sale[["Name","Year","Genre","Global_Sales"]]
top_game_sale=top_game_sale.sort_values(by=["Global_Sales"],ascending=False)


# In[233]:


name=top_game_sale["Name"]
name=top_game_sale["Year"]
y=np.arange(0,20)


# In[234]:


plt.figure(figsize=(30, 18))
g = sns.barplot(x="Name", y="Global_Sales", data=top_game_sale)
index = 0
for value in top_game_sale["Global_Sales"]:
    g.text(index, value - 18, name[index], color="#000", size=14, rotation=90, ha="center")
    index += 1
plt.xticks(rotation=90, fontsize=14)
plt.xlabel("Yıl")
plt.show()


# In[235]:


comp_genre=data[["Genre","NA_Sales","EU_Sales","JP_Sales","Other_Sales"]]
comp_map=comp_genre.groupby(by=["Genre"]).sum()


# In[236]:


plt.figure(figsize=(15,10))
sns.set(font_scale=1)
sns.heatmap(comp_map,annot=True,fmt=".1F")
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show() 


# In[268]:


comp_table=comp_map.reset_index()
comp_table=pd.melt(comp_table,id_vars=["Genre"],value_vars=["Genre","NA_Sales","EU_Sales","JP_Sales","Other_Sales"],var_name="Sale_Area",value_name="Sale_Price")  
comp_table.head()                
                # melt ile sütunlar üzerinde yeni işlemler yaptık   
            


# In[238]:


plt.figure(figsize=(15,10))
sns.barplot(x="Genre",y="Sale_Price",hue="Sale_Area",data=comp_table);

# ülkelerde kıtalarda satılan oyun türlerinin şehirlerin iinde dağılımı 


# In[239]:


data.head()


# In[269]:


comp_platform=data[["Platform","NA_Sales","EU_Sales","JP_Sales","Other_Sales"]]
comp_platform.head()


# In[304]:


comp_platform=comp_platform.groupby(by=["Platform"]).sum().reset_index()


# In[305]:


comp_table = pd.melt(comp_platform, id_vars=["Platform"], value_vars=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"],var_name="Sale_Area", value_name="Sale_Price")
comp_table.head()


# In[306]:


plt.figure(figsize=(15,10))
sns.barplot(x="Platform",y="Sale_Price",hue="Sale_Area",data=comp_table);
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show() 


# In[ ]:





# In[307]:


data.head()


# # en iyi 20 yayıncı 
# 

# In[310]:


import matplotlib.pyplot as plt
import seaborn as sns

top_publisher = data.groupby(by=["Publisher"])["Year"].count().sort_values(ascending=False).head(20)
top_publisher = pd.DataFrame(top_publisher).reset_index()

plt.figure(figsize=(15, 10))
sns.countplot(x="Publisher", data=data, order=top_publisher["Publisher"])
plt.xticks(rotation=90)
plt.show()



# # yayıncılar arasında en yuksek satıslar kıme aıt 

# In[320]:


sale_pbl = data[["Publisher","Global_Sales"]]
sale_pbl = sale_pbl.groupby("Publisher")["Global_Sales"].sum().sort_values(ascending=False).head()
sale_pbl = pd.DataFrame(sale_pbl.reset_index())


# In[321]:


plt.figure(figsize=(15,10))
sns.barplot(x="Publisher",y="Global_Sales",data=sale_pbl)
plt.xticks(rotation=90)
plt.show()


# # yayıcıları karşılaştırabılırız

# In[354]:


comp_publisher=data[["Publisher","NA_Sales","EU_Sales","JP_Sales","Other_Sales","Global_Sales"]]
comp_publisher.head()


# In[355]:


comp_publisher = comp_publisher.groupby(by=["Publisher"]).sum().reset_index().sort_values(by=["Global_Sales"], ascending=False)
comp_publisher = comp_publisher.head(20)






# In[356]:


comp_publisher = pd.melt(comp_publisher, id_vars=["Publisher"], value_vars=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"],var_name="Sale_Area", value_name="Sale_Price")
comp_publisher.head(20)


# # barplot alarak kürsel anlamda kı satışlara bakacaz

# In[357]:


plt.figure(figsize=(15,10))
sns.barplot(x="Publisher",y="Sale_Price",hue="Sale_Area",data=comp_publisher);
plt.xticks(fontsize=14,rotation=90)
plt.yticks(fontsize=14)
plt.show() 


# # her yıl için yayıncıların  sayısına göre  en ust sıradakı yayıncılarıo bulalım 

# In[363]:


top_publisher = data[["Year","Publisher"]]
top_publisher_df = top_publisher.groupby(by=["Year","Publisher"]).size().reset_index(name='Count')
top_publisher_idx=top_publisher_df.groupby(by=["Year"])['Count'].transform(max)==top_publisher_df['Count']
top_publisher_count=top_publisher_df[top_publisher_idx].reset_index(drop=True)
top_publisher_count=top_publisher_count.drop_duplicates(subset=["Year","Count"],keep='last').reset_index(drop=True)


# In[366]:


publisher=top_publisher_count["Publisher"]


# In[368]:


plt.figure(figsize=(30, 15))
g = sns.barplot(x="Year", y="Count", data=top_publisher_count)
index = 0
for value in top_publisher_count['Count'].values:
    g.text(index, value +5, str(publisher[index]+'----'+str(value)), color="#000", size=14, rotation=90, ha="center")
    index += 1
plt.xticks(rotation=90)
plt.show();


# In[ ]:





# In[ ]:





# In[ ]:





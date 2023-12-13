#!/usr/bin/env python
# coding: utf-8

# #                      Iphone Analysis in India on Flipkart

# For the iPhone sales analysis task, I have collected a dataset from Kaggle containing data about the sales of iPhones in India on Flipkart. It will be an ideal dataset to analyze the sales of iPhones in India. 

# In[1]:


import pandas as pd
import numpy as np
import  plotly.express as px
import plotly.graph_objects as go
data =pd.read_csv(r"C:\Users\User\Downloads\archive (5)\apple_products.csv")
print(data.head(10))


# In[2]:


print(data.isnull().sum())


# In[3]:


print(data.describe())


# In[5]:


highest_rated =data.sort_values(by=["Star Rating"],
                              ascending =False)
highest_rated =highest_rated.head(10)
print(highest_rated['Product Name'])


# In[14]:


iphone =highest_rated["Product Name"].value_counts()
#print(iphone)
label =iphone.index
#print(label)
counts =highest_rated["Number Of Ratings"]
print(counts)
fig =px.bar(highest_rated,x=label,y=counts,title= "number of ratings")
fig.show()


# In[15]:


iphone =highest_rated["Product Name"].value_counts()
#print(iphone)
label =iphone.index
#print(label)
counts =highest_rated["Number Of Reviews"]
print(counts)
fig =px.bar(highest_rated,x=label,y=counts,title= "number of reviews")
fig.show()


# In[17]:


fig=px.scatter(data_frame=data,x='Number Of Ratings',y='Sale Price',size ="Discount Percentage",
              trendline ='ols',title ="Relationship between sale and ratings")
fig.show()


# In[18]:


fig=px.scatter(data_frame=data,x='Number Of Ratings',y='Discount Percentage',size ="Sale Price",
              trendline ='ols',title ="Relationship between sale and ratings")
fig.show()


# In[ ]:





# In[ ]:





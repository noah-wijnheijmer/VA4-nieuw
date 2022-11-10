#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st


# In[9]:


unemp = pd.read_csv('unemployment analysis.csv')


# In[10]:


unemp_long= pd.melt(unemp, id_vars=['Country Name','Country Code'], var_name="Year", value_name= 'Unemployment Rate')
#unemp_long


# In[12]:


unemp.drop(columns = ['Country Code'], inplace = True)
unemp.set_index('Country Name', inplace = True)


# In[13]:


df1 = unemp.T
#df1


# In[25]:


fig = px.line(df1[['Africa Eastern and Southern', 'Africa Western and Central',"Middle East & North Africa", 'Central Europe and the Baltics',
                    "Europe & Central Asia",
                    'East Asia & Pacific', "Latin America & Caribbean", 'United States', 'Australia']])
fig.show()
#st.pyplot(fig=None, clear_figure=None)


# In[15]:


highun=df1.mean(axis=0).nlargest(10)
highun


# In[16]:


df3 = {'Lesotho':30.396452 , 'North Macedonia':29.789677 , 'South Africa':28.232581 , 'Djibouti':27.733226, 
       'Eswatini':24.391290, 'Bosnia and Herzegocina':24.044516, 'Montenegro':23.048387, 'Namibia':21.033548, 
       'Cong, Rep.':20.291613, 'Botswana':19.814839}


# In[26]:


courses = list(df3.keys())
values = list(df3.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='r',
        width = 0.4)
 
plt.xticks(rotation = 45) 
plt.ylabel("% Unemployed")
plt.title("Highest Unemployed Countries")
plt.show()
#st.pyplot(fig=None, clear_figure=None)


# In[18]:


lowun=df1.mean(axis=0).nsmallest(10)
lowun


# In[19]:


df5 = {'Qatar':0.569355, 'Cambodia':0.767419, 'Myanmar':0.916774, 'Rwanda':0.916774, 
       'Chad':0.950000, 'Bahrain':1.164839, 'Thailand':1.315806, 'benin':1.346452, 
       'Solomon Islands':1.370645, 'Niger':1.376452}


# In[20]:


courses = list(df5.keys())
values = list(df5.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='r',
        width = 0.4)
 
plt.xticks(rotation = 45) 
plt.ylabel("% Unemployed")
plt.title("Highest Unemployed Countries")
plt.show()


# In[21]:


gk = unemp_long.groupby('Year')
gk.get_group('1991')


# In[22]:


sns.scatterplot(x="Year", y="Unemployment Rate", data=unemp_long)
plt.title("Unemployment Rate", size=20, color="red")
plt.xlabel("Year")
plt.xticks(rotation = 90) 
#plt.ylabel("Unemployment Rate")
plt.show()


# In[28]:


st.set_page_config(page_title="Dashboard Noah Wijnheijmer en Julius Slobbe", layout = "wide", initial_sidebar_state="expanded")


# In[29]:


st.sidebar.title('Navigatie')


# In[31]:


pages = st.sidebar.radio('paginas', options=['Home','Datasets', 'Visualisaties', 'Einde'], label_visibility='hidden')

if pages == 'Home':
    st.markdown("Welkom op het dashboard van Noah Wijnheijmer. Gebruik de knoppen in de sidebar om tussen de verschillende paginas te navigeren. ")
elif pages == 'Datasets':
    st.subheader('Gebruikte Datasets.')
    st.markdown("Hieronder wordt de dataset met data over het gebruik van de laadpaal weergegeven.")
    st.dataframe(data=lph, use_container_width=False)
    st.subheader('Dataset RDW.')
    st.markdown("Dataset met kentekeninformatie. ")
    st.dataframe(data=rdwh, use_container_width=False)
    st.markdown("Bron Dataset: https://opendata.rdw.nl/Voertuigen/M1-tenaamstelling-toelating-01-01-2022-/qn6h-6bru")
    st.subheader('Dataset Open Charge Map')
    st.markdown("Dataset met locaties van laadpalen, gebruikt om een kaart van laadpalen in Nederland te maken. Als API ingeladen van open charge map.")
    st.dataframe(data=df5h, use_container_width=False)
    st.markdown("Bron Dataset: https://openchargemap.org/site/develop#api")
elif pages == 'Visualisaties':
    st.subheader("Hier worden de visualisaties weergegeven die wij hebben opgesteld."), st.image("map.png", width=None ,output_format='auto'), folium_static(m), st.plotly_chart(fig10), st.plotly_chart(fig11), st.plotly_chart(fig1), st.plotly_chart(fig2), st.plotly_chart(fig3) 
elif pages == 'Einde':
    st.markdown('Bedankt voor het bezoeken.')


# In[ ]:





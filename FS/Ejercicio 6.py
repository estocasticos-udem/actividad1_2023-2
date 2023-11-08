#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Crear un DataFrame con los datos
df = pd.DataFrame({'Homo/Bi': [0,2146], 
                   'Consumidor': [70, 463],
                   'Contacto': [136,60],
                   'Otros': [49,135],},
             index=['Hombre', 'Mujer'])

# Mostrar el DataFrame
print(df)

genero = df.sum(axis = 1)
# Filas
metodo = df.sum()

N = df.sum().sum() 


# In[3]:


genero


# In[4]:


metodo


# In[5]:


N


# In[8]:


#Probabilidad que una persona elegida al azar sea mujer
N_mujer = genero[0]
P_mujer = N_mujer/N
print(f"P(mujer)= {P_mujer*100:.3f}")


# In[10]:


#Probabilidad de que una persona tenga un factor de riesgo por contacto heterosexual
N_contacto = metodo[2]
P_contacto = N_contacto/N
print(f"P(contacto)= {P_contacto*100:.3f}")


# In[12]:


#Probabilidad de que una mujer tenga un factor de riesgo por consumir drogas intravenosas
N_drogas = metodo[1]
N_mujer = genero[0]
P_mudro = (N_drogas+N_mujer)/N
print(f"P(mu_dro)= {P_mudro*100:.3f}")


# In[14]:


#Probabilidad de que una mujer tenga un factor de riesgo por contaco homosexual/bisexual
N_drogas = metodo[1]
N_mujer = genero[0]
P_muhomo = (0*N_mujer)/N
print(f"P(mu_homo/bi)= {P_muhomo*100:.3f}")


# In[18]:


#Probabilidad de que un hombre tenga un factor de riesgo por consumidor de drogas intravenosa
N_drogas = metodo[1]
N_hombre = genero[1]
P_homdro = (463)/N
print(f"P(hom_dro)= {P_homdro*100:.3f}")


# In[19]:


#Probabilidad de que una mujer tenga un factor de riesgo por contacto hetero
N_drogas = metodo[1]
N_homo = metodo[2]
P_homdro = (136)/N_homo
print(f"P(hom_dro)= {P_homdro*100:.3f}")


# In[ ]:





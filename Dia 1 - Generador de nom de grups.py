#!/usr/bin/env python
# coding: utf-8

# # Dia 1 - Generador de nom de grups

# In[56]:


print("Benvingut al generador de noms de grup")


# In[57]:


ciutat = input("A quina ciutat vas passar la teva infantesa? ")


# In[61]:


mascota = input("Com es deia la teva primera mascota? ")


# In[62]:


nom = ""

if mascota[-1] == "a":
    nom = mascota[:-1]
    nom = nom + "es"

else: 
    nom = mascota + "s"


# In[63]:


print("Un bon nom per al teu grup pot ser: " + nom + " de " + ciutat)


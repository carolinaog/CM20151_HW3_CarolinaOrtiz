
# coding: utf-8

# In[1]:

import sys
import os
import codecs
import itertools
import unicodedata
import string
from itertools import islice


# In[3]:

userNumber = raw_input('Escriba un numero entero: ')

try:
    # convierte el número en entero
    userNumber = int(userNumber)
# Evalúa la excepción
except ValueError:
    userNumber = 0
else:
    #Asigna el valor que entra a s, el número de lineas
    s = userNumber

with open("Sainte-Beuve.txt") as f:
    lines =[]
    lines.extend(f.readline() for i in xrange(s))
    

for letras in lines:
    uTexto = unicode(letras, 'utf8') #Convierte en unicode 
    uTexto=uTexto.lower() #volver todas las letras a  minúsculas
    uTexto=unicodedata.normalize('NFKD',uTexto).encode('ASCII','ignore')  #eliminar tíldes
    
    a=0
    e=0
    i=0
    o=0
    u=0
    
    for letters in letras:
        if(letters=='a'):
            a=a+1
        if(letters=='e'):
            e=e+1
        if(letters=='i'):
            i=i+1
        if(letters=='o'):
            o=o+1
        if(letters=='u'):
            u=u+1
        vocales=a+e+i+o+u
     
    print uTexto, vocales
    


# In[ ]:




# In[ ]:




# In[124]:




# In[124]:




# In[ ]:




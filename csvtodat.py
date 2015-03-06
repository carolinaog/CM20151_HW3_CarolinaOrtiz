
# coding: utf-8

# In[24]:

import csv
import os


# In[25]:

#Metodo para leer el archivo Notas.csv y guardar un nuevo archivo Notas.dat con el separador +
with open("Notas.csv", 'r') as f:
    with open("Notas.dat", 'w') as t:
        for line in f:
            new_line = line.replace(",","+")
            t.write(new_line)


# In[26]:

#Metodo para ejecutar el comando sed desde la terminal para reemplazar la ',' por '+' en el archivo Notas.csv y guardar un nuevo archivo Notas.dat 
os.system("sed 's/,/+/g' Notas.csv > csvtodat.csv")


# In[ ]:




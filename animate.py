
# coding: utf-8

# In[1]:

import urllib
import numpy as np
import matplotlib.pyplot as plt



# In[2]:

#Se descargan los archivos 
for x in range(0,5801,50):
    
    if x<=50:
        urllib.urlretrieve("https://github.com/forero/ComputationalMethods/raw/master/homework/2015-01/hw3/Test/test00003.txt","test00003.txt")
        urllib.urlretrieve("https://github.com/forero/ComputationalMethods/raw/master/homework/2015-01/hw3/Test/test00050.txt","test00050.txt")
        
        
    elif x>50:
        urllib.urlretrieve("https://github.com/forero/ComputationalMethods/raw/master/homework/2015-01/hw3/Test/test00"+str(x)+".txt","test00"+str(x)+".txt")


# In[3]:


#Animación de las dos primeras columnas


for x in range(0,5801,50):
   
   
    if x<=50:
        print x
        
        archivo=np.loadtxt('test00003.txt') 
        columna3=archivo[:,0]
        columna4=archivo[:,1]
        plt.figure(0)
        plt.plot(columna3, columna4, 'ro')
        plt.show()
        
        archivo2=np.loadtxt('test00050.txt') 
        columna5=archivo2[:,0]
        columna6=archivo2[:,1]
        plt.figure(1)
        plt.plot(columna5, columna6, 'ro')
        plt.show()

       
        
    elif x>50:
        print x
        
        archivo3=np.loadtxt('test00'+str(x)+'.txt')
        columna7=archivo3[:,0]
        columna8=archivo3[:,1]
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        ax1.plot(columna7, columna8, 'ro')
        plt.show()
        
        
    


# In[ ]:




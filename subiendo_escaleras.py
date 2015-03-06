
# coding: utf-8

# In[3]:

import random


# In[4]:

#Cuantas maneras distintas existen para subir N escaleras?
def fib(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fib(n-1) + fib(n-2)
print "Existen",fib(13),"distintas maneras de subir las escaleras de 13 escalones"
print "Existen",fib(15),"distintas maneras de subir las escaleras de 15 escalones"


# In[5]:

#Escriba una función escaleras (A,B) que retorna especificando las respuestas consecutivas de las maneras distintas de subir una escalera \n dados dos arreglos A y B.
L=random.randrange(1,50)
a=[]
b=[]

for i in range (L):    
        a.append(random.randrange(1,L)) 
        b.append(random.randrange(1,20))
        

def escaleras(a,b):  
    c=[]
    d=[]
    for i in range (0,L):    
            A=a[i]
            B=b[i]
            modu=((A)%(2*B))
            c.append(modu)
    
        
        
    for j in range(0,L):
          y=fib(c[j]) 
          d.append(y)
    
        
    return d



# In[6]:

esc=escaleras(a,b)
print "El resultado de la función escaleras(A,B) es"

print esc


# In[ ]:




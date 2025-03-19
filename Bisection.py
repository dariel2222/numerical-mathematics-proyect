# Programa que calcula el cero de la función: X^3 + X - 1, aplicando el Método de bisección en un rango dado

from tabulate import tabulate

print("Programa que calcula el cero de la función: X^3 + X - 1, aplicando el Método de bisección en un rango dado")

data = []

i = 0
a = 0
b = 1
c = 0
fa = 0
fb = 0
rango = 0.005
tol=abs(b-a)

while(abs(tol)>rango):
    
    i+=1
         
    c=(a+b)/2
    
    fa = pow(a,3)+a-1
    fb= pow(b,3)+b-1
    fc= pow(c,3)+c-1
   
    data.append(i,a,b,c,fa,fb,fc,a,b,tol)
   
   # if(fa*fc>0):
        
    #    a=c        
    
    #else:
     #   b=c
    
    tol = abs(b-a)
    
headers = ["I","a","b","c","f(a)","f(b)","f(c)","New a","New b","Tolerance"] 

print(tabulate(data, headers=headers, tablefmt="grid"))   
        
# Programa que calcula el cero de la función: X^3 + X - 1, aplicando el Método de bisección en un rango dado

#inclución de librerias

from tabulate import tabulate

#Función de f(n)

def fn(n):
    
    return pow(n,3)+n-1

#Declaracion de variables y listas

data = []
headers = ["I","a","b","c","f(a)","f(b)","f(c)","New a","New b","Tolerance"]

i = 1
a = 0
b = 1
c = 0
new_a=a
new_b=b
rango = 0.0005
tol=abs(b-a)

#Bucle para llevar a cabo el algoritmo necesario

while True:
    
    a=new_a
    b=new_b
    
         
    c=(a+b)/2
    
    fa = fn(a)
    fb = fn(b) 
    fc = fn(c)
   
   
    if(fa*fc>0):
        
        new_a=c        
    
    else:
        new_b=c
    
    tol = abs(b-a)
    
    data.append([i,a,b,c,fa,fb,fc,new_a,new_b,tol])
    
    if abs(tol)<rango:
        
        break
    
    i+=1
    
 

print(tabulate(data, headers=headers, tablefmt="rounded_grid"))   
        
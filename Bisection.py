# Programa que calcula el cero de la función: X^3 + X - 1, aplicando el Método de bisección en un rango dado

#inclución de librerias

from tabulate import tabulate

#Declaracion de variables y listas

data = []
headers = ["I","a","b","c","f(a)","f(b)","f(c)","New a","New b","Tolerance"]

i = 0
a = 0
b = 1
c = 0
new_a=a
new_b=b
fa = 0
fb = 0
rango = 0.0005
tol=abs(b-a)

#Bucle para llevar a cabo el algoritmo necesario

while(abs(tol)>rango):
    
    a=new_a
    b=new_b
    
    i+=1
         
    c=(a+b)/2
    
    fa = pow(a,3)+a-1
    fb= pow(b,3)+b-1
    fc= pow(c,3)+c-1
   
   
    if(fa*fc>0):
        
        new_a=c        
    
    else:
        new_b=c
    
    tol = abs(b-a)
    
    data.append([i,a,b,c,fa,fb,fc,new_a,new_b,tol])
    
 

print(tabulate(data, headers=headers, tablefmt="rounded_grid"))   
        
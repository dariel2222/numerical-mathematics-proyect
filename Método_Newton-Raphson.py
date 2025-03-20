# Programa que calcula el cero de la función: 3 - X - 2ln(x), aplicando el Método de Newton Raphson

#inclución de librerias 

import math
from tabulate import tabulate 

#Fución f(x)

def f(x):
    return 3 - x - 2 * math.log(x,e)

#Función f'(x)

def f_prime(x):
    return -1 - 2 / x

#Declaracion de variables y listas

data = []
headers = ["I","Xn","f(Xn)","f'(Xn)","Xn+1"]

i=1
Xn=1.5
rango = 0.0005
e = math.e


#Bucle para llevar a cabo el algoritmo necesario

while True:
    
    fXn = f(Xn)
    
    fpXn = f_prime(Xn)
    
    Xnplus = Xn - fXn / fpXn
    
    data.append([i,Xn,fXn,fpXn,Xnplus])
    
    if abs(Xnplus-Xn) < rango:
        break
    
    Xn = Xnplus
    
    i += 1
    


#impresion por consola de la tabla de valores del Método Newton Raphson

print(tabulate(data, headers=headers, tablefmt="rounded_grid"))    
    

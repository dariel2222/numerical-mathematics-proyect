# Programa que calcula el cero de la función: 3 - X - 2ln(x), aplicando el Método de Newton Raphson
import math
from tabulate import tabulate

def f(x):
    return 3 - x - 2 * math.log(x,e)

def f_prime(x):
    return -1 - 2 / x

data = []
headers = ["I","Xn","f(Xn)","f'(Xn)","Xn+1"]

i=1
Xn=1.5
rango = 0.0005
e = math.e

while True:
    
    fXn = f(Xn)
    
    fpXn = f_prime(Xn)
    
    Xnplus = Xn - fXn / fpXn
    
    data.append([i,Xn,fXn,fpXn,Xnplus])
    
    if abs(Xnplus-Xn) < rango:
        break
    
    Xn = Xnplus
    
    i += 1
    


print(tabulate(data, headers=headers, tablefmt="rounded_grid"))    
    

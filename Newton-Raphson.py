# Programa que calcula el cero de la función: 3 - X - 2ln(x), aplicando el Método de Newton Raphson
import math

from tabulate import tabulate

date = []
header = ["I","Xn","f(Xn)","f'(Xn)","Xn+1"]

i=0
Xn=1.5
fXn = Xn
fpXn = 0
Xnplus = 0
rango = 0.0005

while(fXn>rango):
    
    Xn = Xnplus
    
    fXn = 3 - 1.5 - 2(math.log(1.5,math.e))
    
    fpXn = - 1 - 2 / 1.5
    
    Xnplus = Xn-fXn/fpXn
    
    date.append([Xn,fXn,fpXn,Xnplusn])


    
    
    
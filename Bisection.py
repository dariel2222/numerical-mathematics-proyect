# Programa que calcula el cero de la función: X^3 + X - 1, aplicando el Método de bisección 

i = 0
a = 0
b = 1
c = 0
fa = 0
fb = 0
rango = 0.0005
tol=abs(b-a)

while(abs(tol)>rango):
    
    i+=1
    
    print(i, " -->  ",end="")
    print(" a: ", a,end=" ")
    print(" b: ", b,end=" ")
        
    c=(a+b)/2
    
    print(" c: ", c,end=" ")
    
    fa = pow(a,3)+a-1
    fb= pow(b,3)+b-1
    fc= pow(c,3)+c-1
   
    print(" f(a): ", fa,end=" ")
    print(" f(b): ", fb,end=" ")
    print(" f(c): ", fc,end=" ")

    if(fa*fc>0):
        
        a=c        
    
    else:
        b=c
    
    tol = abs(b-a)
    
    print(" New a: ", a,end=" ")
    print(" New b: ", b,end=" ")
    print(" Tolerancia: ", tol)
        
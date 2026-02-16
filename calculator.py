import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    if b==0:
        print("ERROR: No se puede dividir entre 0")
    else:
        return a/b
    
def modulo(a,b):
    return a%b
def sucesora(n):  
    return n + 1

def antecesora(n):  
    return n - 1



def sucesora_suma(a, b):
    if b == 0: 
        return a 
    return sucesora(sucesora_suma(a, antecesora(b)))

def sucesora_resta(a, b):
    if b == 0:
        return a
    return antecesora(sucesora_resta(a, antecesora(b)))



def sucesora_multi(a, b):
    if b == 0:
        return 0
    return sucesora_suma(a, sucesora_multi(a, antecesora(b)))

def sucesora_div(a, b):
    if b == 0:
        return "No se puede dividir por 0"
    if a < b:
        return 0
    return sucesora(sucesora_div(sucesora_resta(a, b), b)) 

'''
No se puede usando la antecesora. De usarla, arroja un valor negativo. 
Las soluciones para ello no se pueden emplear según las condiciones del profesor.
'''

a = int(input("Ingrese el valor del primer número: "))
b = int(input("Ingrese el valor del segundo número: "))

print ("La suma de los dos números es:", sucesora_suma(a, b))
print ("La resta de los dos números es:", sucesora_resta(a, b))
print ("El producto de los dos números es:", sucesora_multi(a, b))
print ("La división de los dos números es:", sucesora_div(a, b))



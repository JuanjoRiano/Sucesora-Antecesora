# Sucesora-Antecesora

Implementación en Python de las operaciones suma, resta, multiplicación y división utilizando únicamente las funciones sucesora y antecesora.

```python
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
```

## Notas
- No se utilizan operadores aritméticos tradicionales.





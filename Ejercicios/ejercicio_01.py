#Desarrollo de un script que realiza 8 tipos de operaciones algebraicas

import math

a = float(input("ingrese el valor de a: "))
b = float(input("ingrese el valor de b: "))

suma = a + b
diferencia = a - b
producto = a * b
cociente = a / b
logaritmoBase10 = math.log10(a)
potencia = a ** b
euler = math.exp(a)
raiz = a ** (1 / b)

print(f"suma: {suma}")
print(f"diferencia: {diferencia}")
print(f"producto: {producto}")
print(f"cociente: {cociente}")
print(f"logaritmoBase10: {logaritmoBase10}")
print(f"potencia: {potencia}")
print(f"euler: {euler}")
print(f"raiz: {raiz}")

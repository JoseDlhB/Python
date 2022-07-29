import math


def funcion(x):
    return math.exp(x) + x ** 3 - 5


def derivada_funcion(x):
    return math.exp(x) + (3 * (x ** 2))


vector = []
resultado = 0


print("Seleccione que solucion desea:")
print("Presione 1 para seleccionar el primer ejercicio")
print("Presione 2 para seleccionar el segundo ejercicio")
seleccion = input("Ejercicio seleccionado: ")

for i in range(101):
    vector.append(i)


def newtonRaphson():
    if seleccion == "1":
        print("i\tresultado")
        for i in range(1, 101):
            vector[i] = vector[i - 1] - (
                funcion(vector[i - 1]) / derivada_funcion(vector[i - 1])
            )
            resultado = abs(vector[i] - vector[i - 1])
            print(f"{i}.\t{resultado:.16f}")

    if seleccion == "2":
        off = 0
        i = 0
        e = float(input("Ingrese valor para e:"))
        print("i\tresultado")
        while off == 0:
            i += 1
            vector[i] = vector[i - 1] - (
                funcion(vector[i - 1]) / derivada_funcion(vector[i - 1])
            )
            resultado = abs(vector[i] - vector[i - 1])
            if resultado < e:
                off = 1
            print(f"{i}.\t{resultado:.16f}")


newtonRaphson()

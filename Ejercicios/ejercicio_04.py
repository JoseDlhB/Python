# Script que realiza la suma y producto de una matriz

import numpy as np

fila = int(input("Ingrese cantidad de filas: "))
columna = int(input("Ingrese cantidad de columnas: "))

matriz1 = []
matriz2 = []

print("Ingrese valores para la matriz 1:")
for i in range(fila):
    matriz1.append([])
    for j in range(columna):
        matriz1[i].append(float(input(f"Posicion[{i},{j}]:\t")))

print("\nIngrese valores para la matriz 2:")
for i in range(fila):
    matriz2.append([])
    for j in range(columna):
        matriz2[i].append(float(input(f"Posicion[{i},{j}]:\t")))

print("\n")


def suma():
    print("Suma matriz1+matriz2:")
    for i in range(fila):
        print("[", end=" ")
        for j in range(columna):
            print(f"{matriz1[i][j]+matriz2[i][j]:.2f}", end=" ")
        print("]")
    print("\n")


def producto():
    print("Producto matriz1*matriz2:")
    for i in range(fila):
        print("[", end=" ")
        for j in range(columna):
            print(f"{matriz1[i][j]*matriz2[i][j]:.2f}", end=" ")
        print("]")
    print("\n")


def mensajeErrorInversa(matrizX):
    return print(
        f"El determinante de la {matrizX} es cero, por lo cual no se puede hallar la inversa de la matriz"
    )


def determinanteAndInversa():
    if fila == columna:
        print(f"Determinante de matriz1: {np.linalg.det(matriz1):.2f}")
        print(f"Determinante de matriz2: {np.linalg.det(matriz2):.2f}\n")

        if np.linalg.det(matriz1) != 0:
            print(f"inversa de matriz1:\n{np.linalg.inv(matriz1)}\n")
        else:
            mensajeErrorInversa("matriz1")
        if np.linalg.det(matriz2) != 0:
            print(f"inversa de matriz2:\n{np.linalg.inv(matriz2):}\n")
        else:
            mensajeErrorInversa("matriz2")
    else:
        print(
            "Los tamaños de fila y columna ingresados no permiten hallar el determinante ni inversa de las matrices"
        )


suma()
producto()
determinanteAndInversa()

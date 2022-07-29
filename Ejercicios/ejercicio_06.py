# Script que calcula la media y desviacion de un vector

from numpy import sqrt

tamanoDeVector = int(input("ingrese tamaño del vector: "))
vector = []

print("Ingrese valores del vector:")

for i in range(tamanoDeVector):
    vector.append(float(input(f"valor {i}: ")))


def mediaAndDesviacion():

    sumatoria = 0
    media = sum(vector) / tamanoDeVector

    print(f"\nMedia: {media:.2f}")

    for j in range(tamanoDeVector):
        sumatoria += (vector[j] - media) ** 2

    desviacion = sqrt((sumatoria) / (tamanoDeVector - 1))

    print(f"Desviación: {desviacion:.2f}\n")


mediaAndDesviacion()

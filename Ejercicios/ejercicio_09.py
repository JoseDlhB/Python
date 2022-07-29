# Script que ordena una lista mediante Bubblesort

tamanoVector = int(input("Ingrese tamano de vector: "))
vector = []
for i in range(tamanoVector):
    vector.append(float(input(f"Ingrese valor en la posición [{i}]: ")))


def bubblesort():
    for i in range(tamanoVector - 1):
        for j in range(tamanoVector - 1):
            if vector[j] > vector[j + 1]:
                print(f"{vector}", end="-->")
                z = vector[j]
                vector[j] = vector[j + 1]
                vector[j + 1] = z
                print(vector)


bubblesort()
print("Resultado:")
print(vector)

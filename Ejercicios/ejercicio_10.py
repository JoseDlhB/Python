seleccion = int(input("Seleccione que inciso desea 1, 2 o 3: "))
iteraciones = int(input("Ingrese cantidad de iteraciones: "))


def steepestDescent(alfa):
    x, gradiente = [0.5, 0.5], []
    auxGradiente, aux = [], []
    print(f"K\t GRADIENTE\t\tFUNCION\t\tX")
    for i in range(iteraciones):
        gradiente = [2 * x[0], 50 * x[1]]
        print(f"{i+1} \t [{gradiente[0]:.4f} , {gradiente[1]:.4f}]", end="\t")
        auxGradiente = [
            alfa * gradiente[0],
            alfa * gradiente[1],
        ]
        aux = [
            x[0] - auxGradiente[0],
            x[1] - auxGradiente[1],
        ]
        funcion = (x[0] ** 2) + (25 * x[1] ** 2)
        print(f"f(x{i}): {funcion:.4f}", end="\t")
        print(f"[{x[0]:.4f}  , {x[1]:.4f}]")
        x = aux
    print()


def steepestDescent2(alfa2):
    x, gradiente = 3, 0
    auxGradiente, aux = 0, 0
    print(f"K\t GRADIENTE\tDolares\t\tUnidades producidas")
    for i in range(iteraciones):
        gradiente = -3 * x ** 2 + 900 * x + 52500
        print(f"{i+1} \t [{gradiente:.4f}]", end="\t")
        auxGradiente = alfa2 * gradiente
        aux = x + auxGradiente
        funcion = (-(x ** 3)) + (450 * x ** 2) + 52500 * x
        print(f"{funcion:.4f}", end="\t")
        print(f"{x:.4f}")
        x = aux
    print()


if seleccion == 1:
    print("Para alfa = 0.01")
    steepestDescent(0.01)
elif seleccion == 2:
    print("Para alfa = 0.035")
    steepestDescent(0.035)
elif seleccion == 3:
    print("Para alfa = 0.001")
    steepestDescent2(0.001)

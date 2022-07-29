# Script que identifica el tipo de triangulo basado en los angulos ingresados

print("Ingrese valor de los angulos")
angulo1 = float(input(("Angulo 1:  ")))
angulo2 = float(input(("Angulo 2:  ")))
angulo3 = float(input(("Angulo 3:  ")))

if angulo1 == angulo2 == angulo3:
    print("Triangulo equilatero")
elif angulo1 == angulo2 or angulo1 == angulo3 or angulo2 == angulo3:
    print("Triangulo isósceles")
elif angulo1 != angulo2 != angulo3:
    print("Triangulo escaleno")

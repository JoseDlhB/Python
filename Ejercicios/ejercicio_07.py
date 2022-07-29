# Script que identifica si el año es bisiesto

mes = int(input("ingrese mes (en numero): "))
anho = int(input("Ingrese año: "))
bisiesto = anho % 4

calendario = {
    1: "31",
    2: "29",
    3: "31",
    4: "30",
    5: "31",
    6: "30",
    7: "31",
    8: "31",
    9: "30",
    10: "31",
    11: "30",
    12: "31",
}


def mensaje():
    return print(f"El mes {mes} del año tiene {calendario[mes]} días")


if bisiesto == 0:
    print("Año bisiesto")
    calendario["febrero"] = "30"
    mensaje()
else:
    print("Año NO bisiesto")
    mensaje()

## ¿Qué es un algoritmo? ##
# - Serie de paasos ordenados para resolver un problema.
# - Finito.
# - No ambiguo.

## Operadores aritmeticos ##
# - Suma (+)
# - Resta (-)
# - Multiplicación (*)
# - División (/)
# - División entera (//)
# - Modulo (%)
# - Potencia (**)
# - Raiz cuadrada (**0.5)

## Variables ##
# Es un lugar en memoria (una especie de caja) en el que podemos 
# guardar objetos (números, texto, etc). Esta variable posee un 
# identificador o nombre con el cual podemos llamarla cuando la 
# necesitemos.

# - num = 15

## Los primitivos: Tipos de datos senscillos ##
# - Números enteros 
# - num = 15
# print(num)

# - Números de punto flotante (decimales)
# num = 15.5
# print(num)

# - Texto (Cadenas de caracteres)
# nombre1 = 'Jose'
# nombre2 = 'Alfredo'
# print(nombre)
# print(nombre1 + nombre2) #Concatenando dos string

# - Booleanos
#es_estudiante = True
# print(es_estudiante)

## Convirtiendo un dato a un tipo diferente "Castear" ##
# num1 = 25
# num2 = 12.5

# print(int(num2))
# print(str(num2))
# print(float(num1))

## Operadores lógicos ##
# - and (&): Compara dos o más valores, si tan solo uno es False
#  el resultado será False, de lo contrario será True.
# - or (|): Compara dos o más valores, si tan solo uno es True
#  el resultado será True, de lo contrario será False.
# - not: devuelve el valor contrario de la variable evaluada.

## Operadores comparación ##
# - ==: Determina si dos valores son iguales o no.
# - !=: Determina si dos valores son diferentes o no.
# - >: Determina si el primer termino es mayor que el segundo.
# - <: Determina si el primer termino es menor que el segundo.
# - >=: Determina si el primer termino es mayor o igual que el segundo.
# - <=: Determina si el primer termino es menor o igual que el segundo.

## Condicionales ##
# Son decisiones que se establecen de acuerdo a los parámetros que indiquemos.
# edad = int(input("Escribe tu edad: "))
# if edad > 17:
#   print("Eres mayor de edad")
# else:
#   print("Eres menor de edad")

# num = int(input("Ingresa un numero: "))
# if num > 5:
#   print("Es mayor a 5")
# elif: num == 5:
#   print("Es igual a 5")
# else:
#   print("Es mayor a 5")

## Crear un menu
#menu = """
#💰 Bienvenido al conversor de monedad  💰
#1 - ARS a USD
#2 - COP a USD
#3 - MXN a USD
#4 - COP a USD
#Elige una opción: """
#opc = int(input(menu))

## Metodos para trabajar con Python
# - variable.strip(): El método strip eliminará todos los caracteres vacíos 
# que pueda contener la variable
# - variable.lower(): El método lower convertirá a las letras en minúsculas.
# - variable.upper(): El método upper convertirá a las letras en mayúsculas.
# - variable.capitalize(): El método capitalize convertirá a la primera letra
# de la cadena de caracteres en mayúscula.
# - variable.replace (‘o’, ‘a’): El método replace remplazará un caracterer 
# por otro. En este caso remplazará todas las ‘o’ por el caracter ‘a’.
# - len(variable): Te indica la longitud de la cadena de texto dentro de la 
# variable en ese momento.

## Trabajando con slices ##
# En Python, los slices, traducidos al español como “rebanadas”, nos permiten 
# dividir los caracteres de un string de múltiples formas.
# nombre = "Ballena"
# nombre[0:2] >> del indice 0 al 2
# nombre[:4] >> desde el indice inicial al 4
# nombre[0:5:2] >> de 2 pasos en dos pasos
# nombre[::-1] >> regresa el dato al revés 

## Bucles
# Un bucle es un ciclo continuo en todos los lenguajes de programación que 
# nos permite iterar sobre nuestros pasos.

## Ciclo for ##
# for i in range(0,10,[pasos]):
#     num = 2**i
#     print(num)

## Ciclo while ##
# cont = 1
# print(cont)
# while cont < 100:
#   contador += 1
#   print(cont)

## Recorriendo un string con for
# nomnre = input("Escribe tu nombre: ")
# for letra in nombre:
#   print(letra)

## Listas ##
# Las listas nos permiten guardar múltiples valores en una sola variable. 
# Estas listas en Python nos permiten guardar elementos del mismo tipo o 
# diferentes, por lo que podemos tener strings, números enteros y decimales 
# juntos en una misma variable. Las listas también son conocidas como 
# arrays en otros lenguajes programación.
# numeros = [1, 2.5, 25]
# objetos = ['Hola', 3, 4.5, True]
# Se usa el metodo append() para agregar elementos al objeto lista.
# Se usa el metodo pop() para borrar elementos del objeto o lista.
# for elemento in objetos: >> para recorrer una lista.
# print(elementos)

## Tuplas ##
# Las tuplas son estructuras de datos inmutables. Es decir, no puedes 
# modificar una tupla a agregando o quitando un valor. Lo único que puedes
# hacer es definir de nuevo esa tupla a. Los objetos inmutables (como los
# strings) son tipos de datos para Python que apuntan a un lugar específico
# en memoria y que su contenido no puede ser cambiado. Al cambiar el contenido
# predefiniendo el contenido de la variable a, entonces cambiará su posición 
# en memoria.
# mi_tupla = (1, 2, 3)

## Diccionarios ##
# Los diccionarios en Python son una estructura de datos mutable las cuales 
# almacenan diferentes tipos de valores sin darle importancia a su orden. 
# Identifican a cada elemento por una clave (Key). Se escriben entre {}.
# mi_diccionario = {
#   'llave1' : 1,
#   'llave2' : 2,
#   'llave3' : 3,
# }
# print(mi_diccionario[llave1])

#Complete la función que toma un número entero no negativo 'n' como entrada 
#y devuelve una lista de todas las potencias de '2' con el exponente que va 
#de '0' a n(incluido).

def powers_of_two(n):
    pow = []
    for i in range(n+1):
        pow.append(2**i)
    return pow

def even_or_odd(number):
    if number%2 == 0:
        return('Even')
    else:
        return('Odd')

#Es bastante sencillo. Su objetivo es crear una función que elimine el 
#primer y el último carácter de una cadena. Se le da un parámetro, la 
#cadena original. No tiene que preocuparse por cadenas con menos de dos
#caracteres.

def remove_char(s):
    return(s[1:len(s)-1])

#Escriba la función bmi que calcula el índice de masa corporal
#  (bmi = peso / altura 2 ).
#si bmi <= 18.5 devuelve "Bajo peso"
#si bmi <= 25.0 devuelve "Normal"
# #si bmi <= 30.0 devuelve "Sobrepeso"
#si bmi > 30 devolver "Obeso"

def bmi(weight, height):

    bmi = weight/height**2
    if bmi <= 18.5:
        return 'Underweight'
    elif bmi <= 25.0:
        return 'Normal'
    elif bmi <= 30.0:
        return 'Overweight'
    else:
        return 'Obese'

#Escriba una función que indique si el numero ingresado tiene
#raiz exacta o no.

def raiz_InExact(num):
    respuesta = 0
    while respuesta**2 < num:
        respuesta += 1
        print(respuesta)
    if respuesta**2 == num:
        return(f'La raiz cuadrada de {num} es {respuesta}')
    else:
        return(f'{num} no tiene raiz cuadrada exacta')

def aproximacion_raiz_cuadrada(num):
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - num) >= epsilon and respuesta**2 <= num:
        respuesta += paso
    if abs(respuesta**2 - num) >= epsilon:
        return(f'No se encontro la raiz cuadrada {num}')
    else:
        return(f'La raiz cuadrada de {num} es {respuesta}')

def busqueda_binRaices(num):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, num)
    respuesta = (alto+bajo)/2
    while abs(respuesta**2 - num) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < num:
            bajo = respuesta
        else: 
            alto = respuesta
        respuesta = (alto+bajo)/2
    return(f'La raiz cuadrada de {num} es {respuesta}')

print(busqueda_binRaices(12456))


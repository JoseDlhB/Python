#Realice una función que calcule la raiz cuadrada de un numero e
#indique si es exacta o inexacta, realizar funciones para los
#diferentes metodos numericos.

#Función enumeración exhaustiva
def raiz_InExact(num):
    respuesta = 0
    while respuesta**2 < num:
        respuesta += 1
        #print(respuesta)
    if respuesta**2 == num:
        return(f'La raiz cuadrada de {num} es {respuesta}')
    else:
        return(f'{num} no tiene raiz cuadrada exacta')

#Función aproximación de soluciones
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

#Función búsqueda binaria
def busqueda_binRaices(num):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, num)
    respuesta = (alto+bajo)/2
    while abs(respuesta**2 - num) >= epsilon:
        #print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < num:
            bajo = respuesta
        else: 
            alto = respuesta
        respuesta = (alto+bajo)/2
    return(f'La raiz cuadrada de {num} es {respuesta}')

def run():
    num = int(input('Ingrese un numero: '))
    print(raiz_InExact(num))
    print(aproximacion_raiz_cuadrada(num))
    print(busqueda_binRaices(num))

if __name__ == '__main__':
    run()
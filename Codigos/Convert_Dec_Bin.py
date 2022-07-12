
from operator import xor


def Convert_Decimal_Binary(numero):
    """
    Ingresa un número entero y retorna una lista con
    el número equivalente en binario
    """
    binario = []
    while(numero >= 1):
        if numero%2==0: 
            binario.append(0) #Agergar a la lista un '0' si el numero es módulo 2
            numero//=2
        else:           #Agregar un '1' a la lista si el numero no es módulo de 2
            numero//=2
            binario.append(1)
    return(binario[::-1])


def run():
    numero = int(input('Ingrese un numero entero: '))
    binario = Convert_Decimal_Binary(numero)
    print(f'{binario} es el numero en Binario de {numero}')

if __name__ == '__main__':
    run()

    
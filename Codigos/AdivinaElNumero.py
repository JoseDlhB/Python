import random


def run():
    num_rand = random.randint(1,100)
    count = 0
    while(1):
        date = int(input("Ingrese un numero: "))
        if date < 1 | date > 100:
            print("Ingese numero entre 1 - 100: ")
        elif date < num_rand:
            print("Ingrese un numero mayor")
            count += 1
        elif date > num_rand:
            print("Ingrese un numero menor")
            count += 1
        elif date == num_rand:
            print("¡Ganaste!")
            print("Intentos realizados " + str(count))
            menu = """
            ¿Desea seguir jugando?
                    1 - si.
                    2 - no.
            """ 
            opc = int(input(menu))
            if opc == 1:
                count = 1
                num_rand = random.randint(1,100)
                date = int(input("Ingrese un numero: "))
            else:
                print("adiós vaquero ")
                break


if __name__ == '__main__':
    run()
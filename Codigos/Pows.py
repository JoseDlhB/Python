def whilePotencia_2(LIMITE):
    cont = 0
    potencia_2 = 2**cont
    while potencia_2 < LIMITE:
        print("2 elevado a " + str(cont) + " es igual a: " + str(potencia_2))
        cont += 1
        potencia_2 = 2**cont

def forPotencia_2(LIMITE):
    for cont in range(0,LIMITE):
        potencia_2 = 2**cont
        if potencia_2 >= LIMITE:
            break
        else:
            print("2 elevado a " + str(cont) + " es igual a: " + str(potencia_2))
            continue

def run():
    LIMITE = 100
    #whilePotencia_2(LIMITE)
    forPotencia_2(LIMITE)


if __name__ == '__main__':
    run()
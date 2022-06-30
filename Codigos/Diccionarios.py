def run():

    pobracion_paises = {
        'Argentina' : 44938712,
        'Brasil' : 210147125,
        'Colombia' : 50372424,
    }

    #for pais in pobracion_paises.keys():  # Me arroja las llaves del diccionario
    #   print (pais)

    #for pais in pobracion_paises.values():  # Me arroja los valores del diccionario
    #    print (pais)

    for pais, poblacion in pobracion_paises.items():  # Me arroja las llaves y los valores del diccionario
       print (pais + " tiene " + str(poblacion) + " habitantes")


if __name__ == '__main__':
    run()
def run():
    my_dict1 = {}
    my_dict2 = {}
    """
    Generar llaves del 1 al 100 con su respectivo valor elevado al cubo
    """
    for i in range (1,101):
        my_dict1[i] = i**3
    print(my_dict1, end='\n\n')
    """
    Generar llaves del 1 al 100 con su respectivo valor elevado al cubo, 
    pero solo los que no son multiplos de 3.
    """
    for i in range (1,101):
        if i%3 != 0:
            my_dict2[i] = i**3
    print(my_dict2, end='\n\n')
    """
    Generar llaves del 1 al 100 con su respectivo valor elevado al cubo, 
    pero solo los que no son multiplos de 3 con dict comprehensions..
    """   
    my_dict3 = {i: i**3 for i in range(1,101) if i%3!=0}
    print(my_dict3, end='\n\n')
    """
    Crear, con un dictionary comprehension, un diccionario cuyas llaves sean
    los 1000 primeros números naturales con sus raíces cuadradas como valores.
    """
    my_dict4 = {i: i**0.5 for i in range(1,1001)}
    print(my_dict4)

if __name__ == '__main__':
    run()
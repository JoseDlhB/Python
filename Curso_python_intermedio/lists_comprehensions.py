
def run():
    """
    Almacenar en una lista los 100 primeros numeros naturales al cuadrado
    """
    list_natural_num = []
    for num in range(1,101):
        list_natural_num.append(num**2)

    print(list_natural_num)    
    
    """
    Almacenar en una lista los 100 primeros numeros naturales que no
    son divisibles por 3
    """
    list_non_div3 = []   
    for num in list_natural_num:
        if num%3!=0:
            list_non_div3.append(num)

    print(list_non_div3)

    """
    Almacenar en una lista los 100 primeros numeros naturales que no
    son multiplos por 3 haciendo uso de list comprehensions
    """
    list_non_div3 = [num**2 for num in range(1,101) if num%3!=0]

    print(list_non_div3)

    """
    Almacenar en una lista los numeros naturales que son multiplos de 4,
    que a la vez también son múltiplos de 6 y 9, hasta 5 dígitos. 
    """    
    list_multp = [num for num in range(1,100000) if num%4==0 and num%6==0 and num%9==0]

    print(list_multp)

    
if __name__ == '__main__':
    run()
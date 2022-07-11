"""
Programa que solicite el nombre y la edad de dos 
usuarios y posteriormente compare las edades
"""
def run():
    name_1 = input('Ingrese nombre usuario 1: ')
    age_1 = int(input('Ingrese edad de usuario 1: '))
    name_2 = input('Ingrese nombre usuario 2: ')
    age_2 = int(input('Ingrese edad de usuario 2: '))

    if age_1 > age_2:
        print(f'{name_1} es mayor que {name_2}')
    elif age_1 < age_2:
        print(f'{name_2} es mayor que {name_1}')
    else:
        print(f'{name_2} y {name_1} tienen la misma edad')

if __name__ == "__main__":
    run()

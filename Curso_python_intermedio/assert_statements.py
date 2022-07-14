def divisors(num):
        divisors = [i for i in range(1, num+1) if num%i == 0]
        return divisors


def run():  
    num = input(f'Ingrese un número: ')
    assert int(num) > 0 and num.isnumeric(), "Debes ingresar un número positivo"
    print(divisors(int(num)))
    print('Terminó mi programa')
   


if __name__ == '__main__':
    run()
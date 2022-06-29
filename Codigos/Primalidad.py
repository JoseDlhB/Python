def primo(num):
    cont = 0
    for i in range(1, num+1):
        if i == 1 or i == num:
            continue
        if num % i ==0:
            cont += 1
    if cont == 0:
        return True
    else:
        return False


def factorial(n):
    if n < 0:
        print("Factorial de un numero negativo no exite")
    elif n == 0:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact


def primoWilson(num):
    if (factorial(num-1) + 1) % num == 0:
        return True
    else:
        return False


def run():
    num = int(input("Escribe un número: "))
    if primoWilson(num):
        print(str(num) + " es primo")
    else:
        print(str(num) + " no es primo")



if __name__=='__main__':
    run()
def run():
    nombre = input('Ingrese nombre: ')
    saludo = f'Mucho gusto {nombre}, bienvenido al mundo de python.'
    print(saludo)
    print(f'El mensaje anterior tiene {len(saludo)} caracteres')
    

if __name__ == '__main__':
    run()
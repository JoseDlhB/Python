import random

def PassGenerators():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
    'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S',
     'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
     'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
      't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{',
     '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^',
      '&', '$', '#', '"']

    charact = MAYUS + MINUS + NUMS + CHARS
    passW = []
    
    for i in range(15):
        charact_random = random.choice(charact)
        passW.append(charact_random)
    passW = "".join(passW)
    return passW


def run():
    passw = PassGenerators()
    print("Tu nueva contraseña es: " + passw)


if __name__ == '__main__':
    run()
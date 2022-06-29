
def coinChangeDolar(tipoPesos, valor_dolar):
    moneda = float(input("Ingrese pesos " + tipoPesos + ": "))
    dolares = str(round((moneda / valor_dolar), 2))
    print('Ud tiene $' + dolares + ' USD')

    

menu = """
💰 Bienvenido al conversor de monedad  💰

1 - ARS a USD
2 - COP a USD
3 - MXN a USD
4 - COP a USD

Elige una opción: """

opc = int(input(menu))
if opc == 1:
    coinChangeDolar("argentinos",124.89)
elif opc == 2:
    coinChangeDolar("colombianos",4113.56)
elif opc == 3:
    coinChangeDolar("colombianos",20.13)
elif opc == 4:
    moneda = float(input("Ingrese dolares: "))
    valor_pesos = 0.00024
    pesos = str(round((moneda / valor_pesos), 2))
    print('Ud tiene $' + pesos + ' COP')
else:
    print("Ingrese una opción valida")
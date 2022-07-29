# Script que calcula la aproximacion mas cercana a pi

den_1 = 2
den_2 = 3
den_3 = 4
ope = 3
lista = []
for i in range(1, 16):
    if i % 2 == 0:
        div = 4 / (den_1 * den_2 * den_3)
        ope = ope - div
    else:
        div = 4 / (den_1 * den_2 * den_3)
        ope = ope + div

    lista.append(ope)
    den_3 = den_3 + 2
    den_1 = den_1 + 2
    den_2 = den_2 + 2
print(lista)
# print(ope)

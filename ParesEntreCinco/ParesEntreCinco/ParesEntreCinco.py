numero_pares = 0
for n in range(5):
    numero = int(input())
    if (numero % 2 == 0):
        numero_pares += 1

print(numero_pares, "valores pares")
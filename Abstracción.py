def sumar_numeros(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

numeros = [1, 2, 3, 4, 5]
print(sumar_numeros(numeros))
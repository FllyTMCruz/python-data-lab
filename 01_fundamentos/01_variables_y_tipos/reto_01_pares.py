# Reto 1: 1. El Reto consiste en crear una función 
# que filtre los números pares de una lista y 
# cuente los impares descartados.
# muestre los pares
# Entrada de prueba: [3, 8, 12, 17, 20, 25]


def filtrar_pares(numeros):
    pares = []
    descartados = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            descartados = descartados +1 
    print(f"Numeros descartados: {descartados} impares")
    return pares

if __name__ == "__main__":
    Entrada_prueba = [3, 8, 12, 17, 20, 25]
    resultado = filtrar_pares(Entrada_prueba)
    print(f"Numeros pares: {resultado}")
    




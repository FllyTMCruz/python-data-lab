"""
El Reto:
Escribe una función llamada analizar_ventas(montos) que reciba una lista
de números enteros o decimales (representando ventas diarias) y realice lo siguiente:

1. Recorrer la lista para calcular la suma total acumulada de todas las ventas.
2. Calcular el valor promedio de las ventas (suma_total / total_elementos).
3. En una segunda pasada (o ciclo), filtrar y guardar en una nueva lista únicamente
   aquellas ventas que sean estrictamente mayores al promedio obtenido.
4. Imprimir en consola el resumen con el formato:
   "Ventas: Total = $X | Promedio = $Y | Superiores al promedio = Z"
   (Redondea el promedio a 2 decimales en la impresión usando f-string: {promedio:.2f})
5. Retornar la nueva lista con las ventas que superaron el promedio.

Casos de validación:
- Entrada de prueba: [120.0, 450.0, 80.0, 600.0, 310.0, 95.0, 520.0]
- Salida esperada en consola: Ventas: Total = $2175.0 | Promedio = $310.71 | Superiores al promedio = 3
- Retorno de la función: [450.0, 600.0, 520.0]
"""
def analizar_ventas(montos):
    if len(montos) == 0:
        return []

    suma_total = 0.0

    for i in montos:
        suma_total = suma_total + i

    promedio= suma_total/len(montos)
    ventas_sup = []

    for i in montos:
        if i > promedio:
            ventas_sup.append(i)

    print(f"Ventas: Total = {suma_total}| Promedio = {promedio:.2f}| Superiores al promedio = {len(ventas_sup)} ")

    return ventas_sup



if __name__ == "__main__":
    datos = [120.0, 450.0, 80.0, 600.0, 310.0, 95.0, 520.0]
    resultado = analizar_ventas(datos)
    print("Ventas destacadas:", resultado)
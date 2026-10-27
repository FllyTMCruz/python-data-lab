"""
Escribe una función llamada clasificar_desempeno(puntajes) que reciba una lista
de calificaciones numéricas (enteros de 0 a 100) y realice lo siguiente:

1. Recorrer la lista evaluando cada valor con la siguiente escala:
   - >= 90: Clasificar como "Excelente".
   - >= 70 y < 90: Clasificar como "Aprobado".
   - < 70: Clasificar como "Reprobado".
2. Guardar las etiquetas resultantes en una nueva lista en el mismo orden de llegada.
3. Llevar contadores independientes para saber cuántos elementos cayeron en cada categoría.
4. Imprimir en consola el resumen de conteos usando un f-string.
5. Retornar la lista final con las etiquetas asignadas.

Casos de validación:
- Entrada de prueba: [45, 88, 93, 68, 72, 99, 81]
- Salida esperada en consola: Resumen: 2 excelentes | 3 aprobados | 2 reprobados
- Retorno de la función: ["Reprobado", "Aprobado", "Excelente", "Reprobado", "Aprobado", "Excelente", "Aprobado"]
"""

def clasificar_desempeno(puntajes):
    calificaciones = []
    cal_excelentes = 0
    cal_aprobados = 0
    cal_reprobados = 0

    for puntaje in puntajes:
        if puntaje >= 90:
            calificaciones.append("Excelente")
            cal_excelentes += 1
        elif puntaje >= 70:
            calificaciones.append("Aprobado")
            cal_aprobados += 1
        else:
            calificaciones.append("Reprobado")
            cal_reprobados += 1

    print(
        f"Resumen de conteos:\n {cal_excelentes} Excelentes\n {cal_aprobados} Aprobados\n {cal_reprobados} Reprobados"
    )
    return calificaciones


if __name__ == "__main__":
    datos = [45, 88, 93, 68, 72, 99, 81]
    res = clasificar_desempeno(datos)
    print("Resultado retornado:", res)


          







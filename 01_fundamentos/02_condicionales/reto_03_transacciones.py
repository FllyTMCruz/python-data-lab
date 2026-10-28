"""
El Reto:
Escribe una función llamada auditar_transacciones(montos) que reciba una lista
de valores numéricos (float o int) y realice lo siguiente:

1. Recorrer la lista y clasificar cada monto bajo los siguientes criterios:
   - monto <= 0: "Invalida" (error en registro o monto nulo)
   - monto > 0 y monto <= 100: "Micro"
   - monto > 100 y monto <= 1500: "Estandar"
   - monto > 1500: "Alerta" (requiere verificación)
2. Guardar cada etiqueta en una nueva lista en el mismo orden de llegada.
3. Contar de forma independiente:
   - Cantidad de transacciones invalidas.
   - Cantidad de transacciones validas (suma de "Micro" + "Estandar").
   - Cantidad de transacciones de "Alerta".
4. Imprimir en consola el resumen con formato:
   "Auditoria: X validas | Y alertas | Z invalidas"
5. Retornar la lista final con las etiquetas asignadas.

Casos de validación:
- Entrada de prueba: [50.0, 1800.0, -12.5, 300.0, 0.0, 2400.0, 99.99]
- Salida esperada en consola: Auditoria: 3 validas | 2 alertas | 2 invalidas
- Retorno de la función: ["Micro", "Alerta", "Invalida", "Estandar", "Invalida", "Alerta", "Micro"]
"""

def auditar_transacciones(montos):
    valores = []
    invalida = 0
    micro_estandar = 0
    alerta = 0

    for monto in montos:
        if monto <= 0:
            valores.append("Invalida")
            invalida += 1
        elif monto > 0:
            if monto > 100:
                if monto > 1400:
                    valores.append("Alerta (Requiere verificacion)")
                    alerta += 1
                else:
                    valores.append("estandar")
                    micro_estandar += 1
            else:
                valores.append("Micro")
                micro_estandar += 1
    print(f"Resumen: {micro_estandar} validas | {alerta} alerta | {invalida} invalidas")
    return(valores)

if __name__ == "__main__":
    datos = [50.0, 1800.0, -12.5, 300.0, 0.0, 2400.0, 99.99]
    resultado = auditar_transacciones(datos)
    print("Resultado obtenido:", resultado)


        





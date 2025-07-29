"""
🧠 Reto: “El Número Perdido en la Secuencia”
🏷️ Nivel: Intermedio
🧩 Descripción:
Tienes una lista de números enteros consecutivos, pero falta uno. La lista está desordenada y tiene un solo número faltante.

Escribe una función que encuentre el número que falta usando lógica y operaciones matemáticas básicas (sin usar set() o estructuras avanzadas).

🎯 Objetivo:
Escribe una función numero_perdido(lista) que reciba una lista de enteros consecutivos desordenados con un número faltante y devuelva cuál falta.
"""

lista = [40, 43, 42]

def numero_perdido(lista):
    # Ordenamos la lista de menor a mayor
    lista.sort()
    print(f"Lista ordenada: {lista}")

    resta = []

    #print(range(len(lista)-1))

    for i in range(len(lista) - 1):
        # Calculamos la diferencia entre el número actual y el siguiente
        diferencia = lista[i + 1] - lista[i]
        if diferencia > 1:
            # Si la diferencia es mayor a 1, significa que hay un número faltante
            resta.append(lista[i] + 1)
            print(f"El valor faltante es: {lista[i] + 1}")


numero_perdido(lista)
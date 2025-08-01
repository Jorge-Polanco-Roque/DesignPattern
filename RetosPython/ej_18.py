"""
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
 */
"""
import asyncio
from collections import Counter

async def piepaptij(p1,p2):
    try:
        p1 = p1.lower()
        p2 = p2.lower()

        opciones = ["piedra", "papel", "tijera"]
        if p1 not in opciones or p2 not in opciones:
            raise ValueError("Parámetros incorrectos.")

        if p1 == p2:
            return "Empate"
        elif (p1 == "piedra" and p2 == "tijera") or (p1 == "papel" and p2 == "piedra") or (p1 == "tijera" and p2 == "papel"):
            return "Gana Player 1"
        
        elif (p2 == "piedra" and p1 == "tijera") or (p2 == "papel" and p1 == "piedra") or (p2 == "tijera" and p1 == "papel"):
            return "Gana Player 2"

    except ValueError as e:
        print(f"Error: {e}")

# Ejecutar varias llamadas en paralelo
async def main():
    resultados = await asyncio.gather(
        (piepaptij("piedra", "tijera")),
        piepaptij("papel", "tijera"),
        piepaptij("papel", "papel")
    )

    conteo = Counter(resultados)

    for resultado, cantidad in conteo.items():
        print(f"{resultado}:{cantidad}")

asyncio.run(main())



"""
🧠 Reto de Lógica en Python: “La Isla de los Caballeros y los Mentirosos”
🏷️ Nivel: Intermedio
🧩 Descripción:
En una isla, hay dos tipos de personas:
* Caballeros, que siempre dicen la verdad.
* Mentirosos, que siempre mienten.

Tres personas (A, B y C) viven en la isla. Cada una hace la siguiente declaración:
* A dice: “B es un mentiroso.”
* B dice: “C es un mentiroso.”
* C dice: “A y B son del mismo tipo.”

Tu tarea es escribir una función que determine qué tipo es cada persona.

🎯 Objetivo:
Escribe una función resolver_isla() que imprima el tipo de cada persona (Caballero o Mentiroso) de acuerdo con las reglas lógicas.
"""


def resolver_isla():
    opciones = ['Caballero', 'Mentirosos']

    for A in opciones:
        for B in opciones:
            for C in opciones:
                #escenarios.append((A, B, C))
                #print(escenarios[-1])  # Imprimir cada escenario generado
                # Verificamos las declaraciones
                if (A == 'Caballero' and B == 'Mentirosos') or (A == 'Mentirosos' and B == 'Caballero'):
                    if (B == 'Caballero' and C == 'Mentirosos') or (B == 'Mentirosos' and C == 'Caballero'):
                        if (C == 'Caballero' and A == B) or (C == 'Mentirosos' and A != B):
                            print(f"A: {A}, B: {B}, C: {C}")

resolver_isla()
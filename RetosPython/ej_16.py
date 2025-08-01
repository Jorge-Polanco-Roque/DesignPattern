"""
/*
 * Crea una función que sume 2 números y retorne su resultado pasados
 * unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que
 *   debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
 *   asíncrona, es decir, sin detener la ejecución del programa principal.
 *   Se podría ejecutar varias veces al mismo tiempo.
 */
 """

import asyncio
import time

num1 = 312
num2 = 543
segundos = 2

async def suma_tiempo(num1:float, num2:float, segundos:int):
    
    inicio = time.perf_counter()
    await asyncio.sleep(segundos)
    
    suma = num1 + num2
    
    fin = time.perf_counter()

    print(f"Resultado: {suma}")
    print(f"Lapso de tiempo del proceso: {inicio-fin:.6f}")
    
# Ejecutar varias llamadas en paralelo
async def main():
    await asyncio.gather(
        suma_tiempo(431,432,2),
        suma_tiempo(10,26,1),
        suma_tiempo(455,4,4)
    )

asyncio.run(main())

# Síncrono: Cada instrucción espera a que la anterior termine para empezar
# Asíncrono: Puedes lanzar varias tareas al mismo tiempo, y el programa no se bloquea mientras espera.
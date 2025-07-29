"""
🧠 Reto: “El FizzBuzz Lógico Invertido”
🏷️ Nivel: Intermedio
🧩 Descripción:
Te dan una lista de números entre 1 y 100. Pero en vez de darte los números directamente, te dan una lista de cadenas que pueden ser:
* "Fizz" si el número original era divisible por 3
* "Buzz" si el número original era divisible por 5
* "FizzBuzz" si era divisible por ambos
* El número como string, si no era divisible ni por 3 ni por 5

Tu tarea es escribir una función que reconstruya los números originales a partir de esta lista.

🎯 Objetivo:
Escribe una función reconstruir_numeros(lista) que convierta una lista de cadenas como ["1", "2", "Fizz", "4", "Buzz"] en [1, 2, 3, 4, 5].
"""

lista = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def reconstruir_numeros(lista):
    
    nueva_lista = []
    
    for i in lista:
        if i % 3 == 0 and i % 5 == 0:
            nueva_lista.append("FizzBuzz")
        elif i % 3 == 0:
            nueva_lista.append("Fizz")
        elif i % 5 == 0:
            nueva_lista.append("Buzz")
        else:
            nueva_lista.append(str(i))

    print(f"Lista original: {lista}")
    print(f"Lista reconstruida: {nueva_lista}")

reconstruir_numeros(lista)



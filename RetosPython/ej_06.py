"""
 * Escribe un programa que imprima los X primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 """

def fibonacci(n):
    a, b = 0, 1
    fibonacci_sequence = []
    
    # "_" es un placeholder para una variable que no se usará en el bucle, ya que solo nos interesa el valor de a.
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    print(f"Los primeros {n} números de la sucesión de Fibonacci son: {fibonacci_sequence}")
    return fibonacci_sequence

fibonacci(4)
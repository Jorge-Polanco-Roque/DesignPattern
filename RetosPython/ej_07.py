"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def imprimir_primos(hasta):
    lista_primos = [i for i in range(1, hasta + 1) if es_primo(i)]
    print(f"Números primos entre 1 y {hasta}: {lista_primos}")

imprimir_primos(25)


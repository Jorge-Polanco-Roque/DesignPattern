"""
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
"""

def capitalizar_manual(texto):
    resultado = ""
    nueva_palabra = True  # Indicador para saber si estamos al inicio de una palabra

    for c in texto:
        if c == " ":
            resultado += c
            nueva_palabra = True
        else:
            if nueva_palabra and 'a' <= c <= 'z':  # si es una letra minúscula al inicio
                resultado += chr(ord(c) - 32)  # convertir a mayúscula con ASCII
            else:
                resultado += c
            nueva_palabra = False

    print(resultado)

capitalizar_manual("e12e21 gvcewd dqwd")
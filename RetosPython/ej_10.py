"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
# Versión 1
def reserva(palabra):
    word = []
    for i in palabra:
        word.append(i)

    #print(f"Palabra en lista: {word}")

    drow = []
    a = len(word)
    while a > 0:
        a -= 1
        drow.append(word[a])

    print("Respuesta: ","".join(drow))

reserva("Hola, mundo")


# Versión 2

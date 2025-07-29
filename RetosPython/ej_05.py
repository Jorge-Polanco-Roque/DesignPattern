"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 """
 # Ejemplos: "amor" y "roma" son anagramas.

def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    lista_p1 = []
    for p1 in palabra1:
        lista_p1.append(p1)

    print(f"Lista de palabra #1: {lista_p1}")

    lista_p2 = []
    for p2 in palabra2:
        lista_p2.append(p2)

    print(f"Lista de palabra #2: {lista_p2}")

    len_palabra1 = len(palabra1)
    lista_p1_2 = []
    while len_palabra1 > 0:
        len_palabra1 -= 1
        lista_p1_2.append(lista_p1[len_palabra1])
    
    if lista_p1_2 == lista_p2:
        print(f"Las palabras '{palabra1}' y '{palabra2}' son anagramas.")
    else:
        print(f"Las palabras '{palabra1}' y '{palabra2}' no son anagramas.")

son_anagramas("amor", "roma")
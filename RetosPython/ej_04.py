"""
Validar si es un palíndromo
 """

# Es un palindromo si se lee igual al derecho que al revés.

palabra1 = "Anita lava la tina"

def son_anagramas(palabra1):
    palabra1 = palabra1.lower()
    palabra1 = palabra1.replace(" ", "")

    lista_p1 = []
    for p1 in palabra1:
        lista_p1.append(p1)
    
    print(lista_p1)

    lista_p2 = []
    a = len(lista_p1)
    while a > 0:
        a -= 1
        lista_p2.append(lista_p1[a])
    
    print(lista_p2)

    if lista_p1 == lista_p2:
        print(f"La palabra '{palabra1}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra1}' no es un palíndromo.")

son_anagramas(palabra1)
#son_anagramas("Jorge")
"""
Conteo de letras
"""

def cadenas(str1, str2):
    
    cadena_1 = []
    for x in str1:
        cadena_1.append(x)

    cadena_2 = []
    for y in str2:
        cadena_2.append(y)

    cadena_3 = cadena_1 + cadena_2

    conteo = {}
    for z in cadena_3:
        if z in conteo:
            conteo[z] += 1
        else:
            conteo[z] = 1

    filtrados = {k: v for k, v in conteo.items() if v >= 2}

    print(f"Las siguientes letras se repite: {filtrados}")

cadenas("Holaa", "mundo!")
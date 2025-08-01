"""
/*
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""

def ej_17(a1:list, a2:list, b1:bool) -> str:
    try:
        if not isinstance(a1,list) or not isinstance(a2,list) or not isinstance(b1,bool):
            raise ValueError("Los parámetros tienen que ser listas.")

        if b1 == True:
            
            comunes = []
            for x in a1:
                for y in a2:
                    print(x==y)
                    if x == y:
                        comunes.append(x)
            
            print(f"Los comunes son: {comunes}")

        elif b1 == False:
            
            diferentes = []
            for x in a1:
                if x not in a2 and x not in diferentes:
                    diferentes.append(x)

            for y in a2:
                if y not in a1 and y not in diferentes:
                    diferentes.append(y)

            print(f"Los diferentes son: {diferentes}")
        
    except ValueError as e:
        print(f"Error: {e}")

a1 = [22,313]
a2 = [22,3133]
b1 = False

ej_17(a1,a2,b1)
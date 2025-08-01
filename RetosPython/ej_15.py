"""
/*
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 */
"""

action = ["run", "jump","jump"]
track = ["_", "|","_"]

def carrera(action:list, track:list):
    
    results = []

    try:
        if len(action) != len(track):
            raise ValueError("Las listas no tienen el mismo número de elementos.")

        for i in range(0,len(track)):
            #print(action[i])
            #print(track[i])
            if action[i]=="run" and track[i]=="_":
                results.append(1)
            elif action[i]=="jump" and track[i]=="|":
                results.append(1)
            else:
                results.append(0)

        print(f"Los resultados fueron: {results}")

        if sum(results)==len(results):
            print("Se logró!")
        else:
            print("Fallaste!")
    
    except ValueError as e:
        print(f"Error: {e}")

carrera(action,track)
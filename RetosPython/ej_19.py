"""
/*
 * Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección
 * del producto.
 * - El programa retornará el nombre del producto y un array con el dinero
 *   de vuelta (con el menor número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe,
 *   deberá indicarse con un mensaje y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas
 *   de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
 */
"""

def machine(monedas:list,producto:str):
    productos = {
        "A1": 10,
        "B2": 5,
        "C3": 15
        }

    total = sum(monedas)
    print(f"Se ingesaron: ${total} pesos.")
    print(f"Se seleccionó el siguiente producto: {producto}.")

    try: 
        if not isinstance(monedas,list) or producto not in productos:
            raise ValueError("Fallo de input.")

        #print(f"Producto disponibles: {productos}")
        #print(f"Precio: {productos[producto]}")
        #print(f"Monedas: {total}")

        if producto in productos:
            if productos[producto]<=total:
                total = total-productos[producto]
                return f"Transacción completada correctamente de {producto}, te regreso {total} como cambio."
            elif productos[producto]>total:
                return f"No tienes saldo suficiente, te faltan {productos[producto]-total}"
            
    except ValueError as e:
        return f"Error: {e}"


monedas = [1]
producto = "A1"

print(machine(monedas,producto))




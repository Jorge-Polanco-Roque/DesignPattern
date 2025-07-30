"""
🧱 Ejemplo de uso del Patrón de Diseño Builder en Python

Este script implementa el patrón de diseño **Builder**, el cual pertenece a los patrones **creacionales**.
Su objetivo es separar la construcción de un objeto complejo de su representación, permitiendo crear
diferentes versiones del mismo objeto paso a paso.

En este caso, modelamos la construcción de una casa (`House`) de forma controlada usando un `HouseBuilder`.
Este patrón es útil cuando el objeto tiene múltiples configuraciones posibles o cuando su construcción
requiere varios pasos que deben ser controlados de forma explícita.

"""

# Definimos la clase House que representará una casa
class House:
    # Constructor por defecto: inicializa la casa sin valores
    def __init__(self):
        self.floor = None        # Número de pisos (por defecto None)
        self.wall = None         # Número de paredes
        self.roof = None         # Número de techos
        self.furniture = {}  # Diccionario para almacenar muebles

    # Método especial que define cómo se mostrará el objeto al imprimirlo
    def __str__(self):  
        return (
            f"Floor: {self.floor}\n"       # Muestra el número de pisos
            f"Wall: {self.wall}\n"         # Muestra el número de paredes
            f"Roof: {self.roof}\n"         # Muestra el número de techos
            f"Furniture: {self.furniture}" # Muestra los muebles añadidos
        )

# Definimos el constructor (Builder) de casas
class HouseBuilder:
    def __init__(self):
        # Crea una nueva instancia de House que se irá construyendo paso a paso
        self.house = House()

    # Establece el número de pisos
    def set_floor(self, amount):
        self.house.floor = amount
        return self  # Retorna el builder para permitir encadenamiento (fluent interface)

    # Establece el número de paredes
    def set_wall(self, amount):
        self.house.wall = amount
        return self

    # Establece el número de techos
    def set_roof(self, amount):
        self.house.roof = amount
        return self
    
    # Establece el número de muebles
    def set_furniture(self, name, amount):
        if not self.house.furniture.get(name):
            self.house.furniture[name] = 0
        self.house.furniture[name] += amount  # Suma la cantidad de muebles del tipo especificado
        
        return self

    # Devuelve el objeto House ya construido
    def get_house(self):
        return self.house

# Punto de entrada principal del script, lo cual indica el inicio del bloque que debe ejecutarse solo cuando el archivo es el script principal
if __name__ == "__main__":
    print("***Building a house with the Builder pattern***")
    small_house_builder = HouseBuilder()
    small_house_builder.set_floor(1) \
        .set_wall(4) \
        .set_roof(1) \
        .set_furniture("Chair", 2) \
        .set_furniture("Table", 1)
    
    small_house = small_house_builder.get_house()
    print(small_house)


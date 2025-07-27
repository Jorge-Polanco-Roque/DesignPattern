"""
🧱 Ejemplo completo del Patrón de Diseño Builder en Python

Este script implementa el **patrón de diseño Builder**, uno de los patrones **creacionales**.
Su propósito es separar la construcción de un objeto complejo de su representación, permitiendo
crear distintas configuraciones del mismo tipo de objeto paso a paso.

Este ejemplo modela la construcción de una casa (`House`) usando:
- Un **builder** (`SmallHouseBuilder`) que define los pasos de construcción.
- Un **director** (`Contractor`) que orquesta el proceso sin conocer los detalles internos.

🧭 Concepto Clave: Director
El **Director** encapsula el proceso de construcción (orden, pasos, consistencia),
delegando los detalles específicos al builder. Esto permite reutilizar la lógica de armado
con distintos tipos de casas (builders).
"""

# Clase principal que representa una Casa
class House:
    def __init__(self):
        self.floor = None             # Número o tipo de piso
        self.wall = None              # Número o tipo de pared
        self.roof = None              # Número o tipo de techo
        self.furniture = {}           # Diccionario para guardar muebles (nombre: cantidad)

    def __str__(self):
        # Devuelve una representación legible del objeto
        return (
            f"Floor: {self.floor}\n"
            f"Wall: {self.wall}\n"
            f"Roof: {self.roof}\n"
            f"Furniture: {self.furniture}"
        )

# Clase base Builder: define cómo construir paso a paso los elementos de una casa
class HouseBuilder:
    def __init__(self):
        self.house = House()  # Se instancia una casa vacía

    def set_floor(self, amount):
        self.house.floor = amount
        return self  # Permite encadenamiento de métodos

    def set_wall(self, amount):
        self.house.wall = amount
        return self

    def set_roof(self, amount):
        self.house.roof = amount
        return self

    def set_furniture(self, name, amount):
        # Si el mueble no existe aún, se inicializa
        if not self.house.furniture.get(name):
            self.house.furniture[name] = 0
        self.house.furniture[name] += amount  # Se suma la cantidad indicada
        return self

    def get_house(self):
        return self.house  # Devuelve la casa ya construida

# Builder especializado: define una versión particular de casa "pequeña"
class SmallHouseBuilder(HouseBuilder):
    def build_floor(self):
        return self.set_floor("Small Floor")  # Podría ser un objeto o string más descriptivo

    def build_wall(self):
        return self.set_wall("Small Wall")

    def build_roof(self):
        return self.set_roof("Small Roof")

    def build_furnitures(self):
        return self.set_furniture("Chair", 2) \
                   .set_furniture("Table", 1)

# Director: orquesta el proceso de construcción, conoce el orden pero no los detalles internos
class Contractor:
    def __init__(self, builder):
        self.builder = builder  # Se le pasa un builder (puede ser cualquier implementación)

    def construct_house(self):
        # Define el proceso de construcción paso a paso
        self.builder.build_floor() \
                    .build_wall() \
                    .build_roof() \
                    .build_furnitures()

# Uso del patrón
if __name__ == "__main__":
    # Se crea un builder concreto para casas pequeñas
    small_builder = SmallHouseBuilder()

    # Se crea el director que usará el builder para construir la casa
    contractor = Contractor(small_builder)

    # Se construye la casa siguiendo el proceso definido en Contractor
    contractor.construct_house()

    # Se obtiene el objeto final construido
    small_house = small_builder.get_house()

    # Se imprime la descripción de la casa
    print(small_house)


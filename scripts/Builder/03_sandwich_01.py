"""
🥪 Ejemplo del Patrón de Diseño Builder con Sándwiches

Este script implementa el patrón de diseño Builder, uno de los patrones creacionales.
Permite construir diferentes configuraciones de un objeto complejo (Sandwich) paso a paso.

Componentes:
- Producto: `Sandwich`
- Builder base: `SandwichBuilder`
- Builders concretos: `ClubSandwichBuilder`, `VeggieSandwichBuilder`
- Director: `Waiter`
"""

# Producto final: el sándwich que se construirá
class Sandwich:
    def __init__(self):
        self._bread = None           # Tipo de pan
        self._meat = None            # Tipo de carne
        self._cheese = None          # Tipo de queso
        self._vegetables = []        # Lista de vegetales
        self._sauce = []             # Lista de salsas

    def __str__(self):
        # Formatea los ingredientes del sándwich para imprimirlos
        ingredients = "Bread: " + self._bread + " | Meat: " + self._meat
        if self._cheese:
            ingredients += " | Cheese: " + self._cheese
        ingredients += " | Vegetables: " + ", ".join(self._vegetables)
        ingredients += " | Sauce: " + ", ".join(self._sauce)
        return ingredients

# Builder base: define la interfaz común
class SandwichBuilder:
    def __init__(self):
        self.sandwich = Sandwich()

    def add_bread(self):
        pass

    def add_meat(self):
        pass

    def add_cheese(self):
        pass

    def add_vegetables(self):
        pass

    def add_sauce(self):
        pass

    def get_sandwich(self):
        return self.sandwich

# Builder concreto: Club Sandwich
class ClubSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich._bread = "White Bread"
        return self

    def add_meat(self):
        self.sandwich._meat = "Turkey"
        return self

    def add_cheese(self):
        self.sandwich._cheese = "Swiss Cheese"
        return self

    def add_vegetables(self):
        self.sandwich._vegetables += ["Tomato", "Lettuce", "Onion"]
        return self

    def add_sauce(self):
        self.sandwich._sauce += ["Mayonnaise", "Chipotle"]
        return self

# Builder concreto: Veggie Sandwich
class VeggieSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich._bread = "Whole Wheat Bread"
        return self

    def add_meat(self):
        self.sandwich._meat = "None"
        return self

    def add_cheese(self):
        self.sandwich._cheese = "Cheddar Cheese"
        return self

    def add_vegetables(self):
        self.sandwich._vegetables += ["Cucumber", "Bell Pepper", "Spinach"]
        return self

    def add_sauce(self):
        self.sandwich._sauce.append("Hummus")
        return self

# Director: orquesta la construcción del sándwich
class Waiter:
    def __init__(self):
        self.sandwich_builder = None

    def get_builder(self, builder):
        self.sandwich_builder = builder

    def create_sandwich(self):
        self.sandwich_builder.add_bread() \
                             .add_meat() \
                             .add_cheese() \
                             .add_vegetables() \
                             .add_sauce()
        return self.sandwich_builder.get_sandwich()

    def serve_sandwich(self):
        return self.sandwich_builder.get_sandwich()

# Uso del patrón
if __name__ == "__main__":
    # Creamos un Waiter que actuará como director
    waiter = Waiter()

    # Seleccionamos un builder concreto (Club Sandwich)
    waiter.get_builder(ClubSandwichBuilder())

    # Se construye el sándwich paso a paso
    waiter.create_sandwich()

    # Servimos el sándwich
    print("***Club Sandwich***")
    sandwich1 = waiter.serve_sandwich()
    print(sandwich1)

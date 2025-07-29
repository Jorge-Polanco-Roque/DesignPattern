# Importamos herramientas para definir clases abstractas
from abc import ABC, abstractmethod  # ABC = Abstract Base Class, abstractmethod = decorador para métodos abstractos

# ----------- PRODUCTO 1: Furniture (Muebles) -----------
class Furniture(ABC):  # Clase abstracta base para todos los muebles
    def __init__(self, quantity: int):
        self.quantity = quantity  # Cada mueble tendrá una cantidad asociada

    @abstractmethod
    def display(self):
        """Método obligatorio que debe ser implementado en cada subclase"""
        pass

class Sofa(Furniture):  # Implementación concreta de un mueble: Sofá
    def display(self):
        return f"Sofa: {self.quantity} units"

class chair(Furniture):  # Implementación concreta de un mueble: Silla
    def display(self):
        return f"Chair: {self.quantity} units"


# ----------- PRODUCTO 2: Electronics (Electrónicos) -----------
class Electronics(ABC):  # Clase abstracta base para todos los productos electrónicos
    def __init__(self, quantity: int):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        """Método obligatorio para mostrar los detalles"""
        pass

class Radio(Electronics):  # Implementación concreta: Radio
    def display(self):
        return f"Radio: {self.quantity} units"

class Television(Electronics):  # Implementación concreta: Televisión
    def display(self):
        return f"Television: {self.quantity} units"


# ----------- PRODUCTO 3: Decoration (Decoración) -----------
class Decoration(ABC):  # Clase abstracta base para todos los objetos decorativos
    def __init__(self, quantity: int):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        """Método obligatorio"""
        pass

class Painting(Decoration):  # Implementación concreta: Cuadro
    def display(self):
        return f"Painting: {self.quantity} units"

class Vase(Decoration):  # Implementación concreta: Florero
    def display(self):
        return f"Vase: {self.quantity} units"


# ----------- ABSTRACT FACTORY: HouseFactory -----------
class HouseFactory(ABC):  # Fábrica abstracta para crear elementos de una casa
    @abstractmethod
    def furniture(self):
        """Debe retornar un objeto tipo Furniture"""
        pass

    @abstractmethod
    def electronics(self):
        """Debe retornar un objeto tipo Electronics"""
        pass

    @abstractmethod
    def decoration(self):
        """Debe retornar un objeto tipo Decoration"""
        pass


# ----------- CONCRETE FACTORY: SmallHouse -----------
class SmallHouse(HouseFactory):  # Fábrica concreta para casas pequeñas
    def furniture(self):
        return Sofa(2)  # 2 sofás

    def electronics(self):
        return Radio(1)  # 1 radio

    def decoration(self):
        return Painting(1)  # 1 cuadro


# ----------- CONCRETE FACTORY: LargeHouse -----------
class LargeHouse(HouseFactory):  # Fábrica concreta para casas grandes
    def furniture(self):
        return chair(4)  # 4 sillas

    def electronics(self):
        return Television(2)  # 2 televisores

    def decoration(self):
        return Vase(3)  # 3 floreros


# ----------- CLIENTE -----------
def client(factory: HouseFactory):  # El cliente recibe una fábrica, pero no sabe cuál es
    furniture = factory.furniture()       # Crea mueble
    electronics = factory.electronics()   # Crea electrónico
    decoration = factory.decoration()     # Crea decoración

    # Mostrar los resultados (polimorfismo: sin importar el tipo, todos tienen display)
    print(furniture.display())
    print(electronics.display())
    print(decoration.display())


# ----------- EJECUCIÓN -----------
print("Small House Items:".center(50, "-"))  # Título centrado
client(SmallHouse())  # Ejecuta el cliente con la fábrica de casa pequeña

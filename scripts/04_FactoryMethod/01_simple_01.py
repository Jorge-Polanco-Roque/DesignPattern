# Importamos módulos necesarios para trabajar con clases abstractas
from abc import ABC, abstractmethod

# En patrones como Factory Method o Template Method, se usa @abstractmethod para definir comportamientos que deben ser definidos por cada clase concreta, permitiendo flexibilidad y extensibilidad sin modificar la clase base.

# ===============================
# INTERFAZ DEL PRODUCTO
# ===============================

# Definimos una clase abstracta que actuará como interfaz del producto
class Product(ABC):
    @abstractmethod
    def operation(self):
        """Método que cada producto concreto debe implementar"""
        pass

# ===============================
# PRODUCTOS CONCRETOS
# ===============================

# Producto concreto A que implementa la interfaz Product
class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA operation executed"  # Devuelve comportamiento específico

# Producto concreto B que también implementa la interfaz Product
class ConcreteProductB(Product):
    def operation(self):
        return "ConcreteProductB operation executed"  # Otro comportamiento específico

# ===============================
# CREATOR ABSTRACTO (FACTORÍA)
# ===============================

# Definimos la clase base abstracta para los creadores
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        """Método de fábrica que deben implementar las subclases"""
        pass

# ===============================
# CREADORES CONCRETOS
# ===============================

# Creador concreto A que devuelve una instancia de ConcreteProductA
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

# Creador concreto B que devuelve una instancia de ConcreteProductB
class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# ===============================
# CÓDIGO DEL CLIENTE
# ===============================

# El cliente utiliza el creador concreto A sin saber el tipo de producto
creator_a = ConcreteCreatorA()
product_a = creator_a.factory_method()  # Se crea un producto A
print(product_a.operation())           # Se ejecuta el método específico del producto A

# Lo mismo con el creador concreto B
creator_b = ConcreteCreatorB()
product_b = creator_b.factory_method()  # Se crea un producto B
print(product_b.operation())            # Se ejecuta el método específico del producto B
    
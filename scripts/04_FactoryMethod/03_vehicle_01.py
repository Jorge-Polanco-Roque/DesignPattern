# Importamos los módulos necesarios para definir clases abstractas
from abc import ABC, abstractmethod

# =========================
# Interfaz del Producto
# =========================

# Clase abstracta que representa un vehículo genérico
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        """Método que debe ser implementado por todos los tipos concretos de vehículos"""
        pass

# =========================
# Productos Concretos
# =========================

# Clase concreta que representa un coche
class Car(Vehicle):
    def start(self):
        return "Car is starting"

# Clase concreta que representa una bicicleta
class Bike(Vehicle):
    def start(self):
        return "Bike is starting"

# Clase concreta que representa un camión
class Truck(Vehicle):
    def start(self):
        return "Truck is starting"

# =========================
# Fábrica de Vehículos
# =========================

# Clase que encapsula la lógica de creación de vehículos
class VehicleFactory:
    def __init__(self):
        # Diccionario que actúa como "registro de clases" para los tipos de vehículos disponibles
        self.factory = dict(car=Car, bike=Bike, truck=Truck)

    def create_vehicle(self, vehicle_type: str) -> Vehicle:
        # Verifica si el tipo solicitado existe en el diccionario
        if vehicle_type in self.factory:
            vehicle = self.factory.get(vehicle_type)  # Obtiene la clase correspondiente
            return vehicle()  # Instancia y devuelve el objeto correspondiente

# =========================
# Código Cliente
# =========================

# Se instancia la fábrica
factory = VehicleFactory()

# Se crea un coche
car = factory.create_vehicle("car")
print(car.start())  # Salida: Car is starting

# Se crea una bicicleta
bike = factory.create_vehicle("bike")
print(bike.start())  # Salida: Bike is starting

# Se crea un camión
truck = factory.create_vehicle("truck")
print(truck.start())  # Salida: Truck is starting

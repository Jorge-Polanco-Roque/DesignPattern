# Definimos una clase llamada Vehicle que sirve para representar diferentes tipos de vehículos
class Vehicle:
    def __init__(self, vehicle_type: str):
        # Guardamos el tipo de vehículo (por ejemplo, 'car', 'bike', 'truck')
        self.vehicle_type = vehicle_type

    def start(self):
        # Dependiendo del tipo de vehículo, se retorna un mensaje diferente
        if self.vehicle_type == "car":
            return "Car is starting"
        elif self.vehicle_type == "bike":
            return "Bike is starting"
        elif self.vehicle_type == "truck":
            return "Truck is starting"
        else:
            return "Unknown vehicle type"  # Si no se reconoce el tipo, se devuelve un mensaje por defecto
            
# Código cliente para demostrar un enfoque sin Factory Method
car = Vehicle("car")           # Creamos una instancia de Vehicle con el tipo 'car'
print(car.start())             # Imprimimos el resultado de ejecutar el método start
# Resultado: "Car is starting"

"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""

from abc import ABC, abstractmethod

# Interfaz base para polígonos
class Polygon(ABC):
    
    @abstractmethod
    def area(self) -> float:
        pass

    def print_area(self):
        print(f"El área del {self.__class__.__name__.lower()} es {self.area()}")

# Clases concretas
class Triangle(Polygon):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return (self.base * self.height) / 2

class Rectangle(Polygon):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

class Square(Polygon):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side * self.side

# Única función para imprimir y retornar área
def area(polygon: Polygon) -> float:
    polygon.print_area()
    return polygon.area()

# Ejecución principal
if __name__ == "__main__":
    area(Triangle(10.0, 5.0))
    area(Rectangle(5.0, 7.0))
    area(Square(4.0))

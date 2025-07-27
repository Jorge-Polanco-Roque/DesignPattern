# Definimos la clase House que representará una casa
class House:
    # Método constructor que recibe los valores de piso, pared y techo
    def __init__(self, floor, wall, roof):
        self.floor = floor  # Número de pisos
        self.wall = wall    # Número de paredes
        self.roof = roof    # Número de techos

    # Método especial que define cómo se mostrará el objeto al imprimirlo
    def __str__(self):
        return (
            f"Floor: {self.floor}\n"  # Muestra el número de pisos
            f"Wall: {self.wall}\n"    # Muestra el número de paredes
            f"Roof: {self.roof}"      # Muestra el número de techos
        )
    
# Creamos una instancia de la clase House con 4 pisos, 10 paredes y 3 techos
house = House(4, 10, 3)

# Imprimimos el objeto, lo que activará el método __str__
print(house)

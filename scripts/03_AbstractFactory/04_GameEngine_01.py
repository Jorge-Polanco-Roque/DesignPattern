from abc import ABC, abstractmethod

# ========== INTERFAZ BASE ==========
# Clase base abstracta que obliga a implementar el método display()
class GameObject(ABC):
    @abstractmethod
    def display(self):
        pass

# ========== CHARACTERS ==========
# Clase abstracta para personajes
class Character(GameObject):
    @abstractmethod
    def display(self):
        pass

# Implementaciones concretas de personajes
class Knight(Character):
    def display(self):
        print("Knight Character")

class Astranault(Character):
    def display(self):
        print("Astranault Character")

class Soldier(Character):
    def display(self):
        print("Soldier Character")

# ========== WEAPONS ==========
# Clase abstracta para armas
class Weapon(GameObject):
    @abstractmethod
    def display(self):
        pass

# Implementaciones concretas de armas
class Sword(Weapon):
    def display(self):
        print("I have a sword")

class LightSaber(Weapon):
    def display(self):
        print("I have a Lightsaber")

# ========== LEVELS ==========
# Clase abstracta para niveles
class Level(GameObject):
    @abstractmethod
    def display(self):
        pass

# Implementaciones concretas de niveles
class Garage(Level):
    def display(self):
        print("Level Garage")

class SpaceShip(Level):
    def display(self):
        print("Level SpaceShip")

# ========== GAME FACTORY (Abstract Factory) ==========
# Interfaz abstracta de la fábrica de juegos
class GameFactory(ABC):
    @abstractmethod
    def create_character(self):
        pass

    @abstractmethod
    def create_weapon(self):
        pass 

    @abstractmethod
    def create_level(self):
        pass 

# Fábrica concreta: Juego moderno
class ModernGameFactory(GameFactory):
    def create_character(self):
        return Astranault()
    
    def create_weapon(self):
        return LightSaber()
    
    def create_level(self):
        return SpaceShip()

# Fábrica concreta: Juego medieval
class MedievalGameFactory(GameFactory):
    def create_character(self):
        return Soldier()
    
    def create_weapon(self):
        return Sword()
    
    def create_level(self):
        return Garage()

# ========== CLIENTE ==========
def client():
    factories = dict(medieval=MedievalGameFactory, modern=ModernGameFactory)
    
    # Muestra las opciones disponibles
    factory_list = ", ".join(factories)
    
    # Bucle hasta que el usuario escriba un valor válido
    while True:
        factory_type = input(f"Enter the type of game ({factory_list}): ")
        if factory_type in factories:
            break
        print(f"Try again. This game type does not exist. Choose between {factory_list}")
    
    # Retorna una instancia de la fábrica seleccionada
    return factories.get(factory_type)()

# ========== EJECUCIÓN ==========
if __name__ == "__main__":
    factory = client()

    # Crear e imprimir personaje
    character = factory.create_character()
    character.display()

    # Crear e imprimir arma
    weapon = factory.create_weapon()
    weapon.display()

    # Crear e imprimir nivel
    level = factory.create_level()
    level.display()

"""
🎮 Ejemplo del Patrón de Diseño Builder en un entorno estilo motor de juego (Game Engine)

Este script implementa el patrón Builder para crear un objeto de juego (`GameObject`) que puede tener 
componentes como: `Transform`, `Renderer`, `Collider` y un script asociado. El uso de este patrón permite
la construcción paso a paso del objeto, con un diseño limpio y escalable.
"""

# Clase base que representa un objeto de juego compuesto por varios componentes
class GameObject:
    def __init__(self):
        self.transform: Transform = None  # Posición, rotación y escala
        self.renderer: Renderer = None    # Información visual: malla y material
        self.collider: Collider = None    # Colisión: forma y si actúa como trigger
        self.script: str = None           # Script asociado al objeto (comportamiento)

    def __str__(self):
        # Muestra los componentes actuales del GameObject como string legible
        return f"Transforms: {self.transform}\n" \
               f"Renderer: {self.renderer}\n" \
               f"Collider: {self.collider}\n" \
               f"Script: {self.script}\n"

# Componente de posición, rotación y escala
class Transform:
    def __init__(self, position: tuple, rotation: tuple, scale: tuple):
        self.position = position
        self.rotation = rotation
        self.scale = scale

    def __str__(self):
        return f"Position: {self.position}, Rotation: {self.rotation}, Scale: {self.scale}"

# Componente visual que representa una malla y un material
class Renderer:
    def __init__(self, mesh: str, material: str):
        self.mesh = mesh
        self.material = material

    def __str__(self):
        return f"Mesh: {self.mesh}, Material: {self.material}"

# Componente físico que determina colisiones
class Collider:
    def __init__(self, shape: str, is_trigger: bool):
        self.shape = shape
        self.is_trigger = is_trigger

    def __str__(self):
        return f"Shape: {self.shape}, Trigger: {self.is_trigger}"

# Builder que construye paso a paso un GameObject
class GameBuilder:
    def __init__(self):
        self._game = GameObject()  # Crea una instancia vacía

    def add_transform(self, position, rotation, scale):
        self._game.transform = Transform(position, rotation, scale)
        return self  # Retorna self para permitir encadenamiento de métodos

    def add_renderer(self, mesh, material):
        self._game.renderer = Renderer(mesh, material)
        return self

    def add_collider(self, shape, is_trigger):
        self._game.collider = Collider(shape, is_trigger)
        return self

    def add_script(self, script):
        self._game.script = script
        return self

    def get_game(self):
        return self._game  # Devuelve el GameObject construido

# Uso del patrón Builder
if __name__ == "__main__":
    print("***Building a game object with the Builder pattern***")

    # Se crea el builder
    game_builder = GameBuilder()

    # Se construye paso a paso el objeto de juego
    game_builder.add_transform((0, 0, 0), (0, 0, 0), (1, 1, 1)) \
                .add_renderer("CubeMesh", "DefaultMaterial") \
                .add_collider("Box", False) \
                .add_script("PlayerController")

    # Se obtiene el objeto final
    game_object = game_builder.get_game()

    # Se imprime su estado
    print(game_object)

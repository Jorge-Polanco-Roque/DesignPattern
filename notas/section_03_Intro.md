# 🧱 Patrón de Diseño Creacional: Factory Method - Introducción

El **método de fábrica (Factory Method)** es un patrón de diseño creacional que proporciona una interfaz para crear objetos, pero permite que las **subclases decidan qué clase instanciar**.

Es un tipo de patrón orientado a objetos que:
- **Promueve el bajo acoplamiento**.
- Aplica el **principio de abierto/cerrado**, que indica que las clases deben estar abiertas a la extensión pero cerradas a la modificación.

---

## 💡 Idea Principal

El patrón Factory Method es útil cuando se desea **delegar la responsabilidad de creación de objetos a subclases**, en lugar de que la clase base cree directamente las instancias.

> Esto ofrece **mayor flexibilidad y extensibilidad**, ya que se pueden agregar nuevas subclases sin modificar el código existente.

---

## ✅ Ventajas del patrón Factory Method

- Permite **encapsular la lógica de creación de objetos** dentro de las subclases.
- Proporciona una forma consistente de crear objetos, manteniendo **flexibilidad y personalización**.
- Muy utilizado en **frameworks y librerías**, donde el tipo exacto de objeto que se necesita se determina en tiempo de ejecución por el código cliente.

---

## 🛠️ Analogía del mundo real

> Es como una fábrica abstracta que sabe **cómo fabricar** algo,  
pero **delega el "qué fabricar"** a cada una de sus filiales especializadas.

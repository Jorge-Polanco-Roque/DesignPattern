# Design Patterns

Los **Design Patterns** o *patrones de diseño* son soluciones típicas a problemas comunes en el diseño de software. Se agrupan en tres categorías principales:

---

## 🔧 Creational Patterns (Patrones Creacionales)

Estos patrones se centran en el proceso de creación de objetos, ocultando la lógica de creación y haciendo el sistema más independiente del modo en que se crean, componen y representan los objetos.

- **Factory Method**: Define una interfaz para crear un objeto, pero permite a las subclases decidir qué clase instanciar.
- **Abstract Factory**: Proporciona una interfaz para crear familias de objetos relacionados sin especificar sus clases concretas.
- **Builder**: Separa la construcción de un objeto complejo de su representación para que el mismo proceso de construcción pueda crear diferentes representaciones.
- **Prototype**: Crea nuevos objetos copiando un objeto existente, conocido como prototipo.
- **Singleton**: Garantiza que una clase tenga una única instancia y proporciona un punto de acceso global a ella.

---

## 🧱 Structural Patterns (Patrones Estructurales)

Estos patrones se ocupan de cómo las clases y objetos se componen para formar estructuras más grandes.

- **Adapter**: Permite que interfaces incompatibles trabajen juntas.
- **Bridge**: Desacopla una abstracción de su implementación para que ambas puedan variar independientemente.
- **Composite**: Compone objetos en estructuras de árbol para representar jerarquías parte-todo.
- **Decorator**: Añade responsabilidades adicionales a un objeto dinámicamente.
- **Facade**: Proporciona una interfaz unificada a un conjunto de interfaces en un subsistema.
- **Flyweight**: Usa el compartimiento para soportar grandes cantidades de objetos de granularidad fina de manera eficiente.
- **Proxy**: Proporciona un sustituto o representante de otro objeto para controlar el acceso a él.

---

## 🔁 Behavioral Patterns (Patrones de Comportamiento)

Estos patrones se centran en la comunicación entre objetos, definiendo cómo interactúan y cómo se distribuyen las responsabilidades.

- **Chain of Responsibility**: Pasa la petición a lo largo de una cadena de manejadores hasta que uno la procesa.
- **Command**: Encapsula una solicitud como un objeto, permitiendo parametrizar clientes con diferentes solicitudes.
- **Interpreter**: Dado un lenguaje, define una representación para su gramática y un intérprete que usa la representación.
- **Iterator**: Proporciona una manera de acceder secuencialmente a los elementos de una colección sin exponer su representación subyacente.
- **Mediator**: Define un objeto que encapsula cómo interactúan un conjunto de objetos.
- **Observer**: Define una dependencia uno-a-muchos entre objetos para que cuando uno cambie de estado, sus dependientes sean notificados automáticamente.
- **State**: Permite a un objeto modificar su comportamiento cuando cambia su estado interno.
- **Strategy**: Define una familia de algoritmos, encapsula cada uno, y los hace intercambiables.
- **Visitor**: Permite definir una nueva operación sin cambiar las clases de los elementos sobre los que opera.
- **Template Method**: Define el esqueleto de un algoritmo en una operación, dejando algunos pasos a las subclases.

---



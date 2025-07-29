# 🏗️ Creational Design Pattern: Abstract Factory

## 🔸 ¿Qué es?

El patrón **Abstract Factory** es un patrón de diseño creacional que:

- Proporciona una **interfaz para crear familias de objetos relacionados o dependientes** sin especificar sus clases concretas.
- **Separa la lógica de creación** de los objetos de su implementación real, permitiendo mayor flexibilidad y facilidad de modificación.
- Se utiliza cuando un sistema debe ser **independiente de cómo se crean, componen o representan sus productos**.
- Es similar al patrón *Factory Method*, pero en lugar de crear un solo objeto, **crea grupos/familias de objetos** consistentes entre sí.

---

## 📚 Términos clave

| Término              | Descripción                                                                                                                                          |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Abstract Factory** | Interfaz o clase abstracta que declara los métodos para crear productos. Proporciona una interfaz común para crear objetos de una familia.          |
| **Concrete Factory** | Implementación concreta de la fábrica abstracta. Cada fábrica concreta genera una familia específica de productos relacionados.                      |
| **Abstract Product** | Interfaz o clase abstracta que declara los métodos comunes que deben implementar todos los productos de una familia. Define el contrato.             |
| **Concrete Product** | Implementación concreta del producto abstracto. Cada producto concreto corresponde a un tipo específico dentro de una familia.                        |
| **Product Family**   | Grupo de productos relacionados creados por una misma fábrica concreta. Comparten un tema o propósito común.                                         |
| **Factory Hierarchy**| Estructura jerárquica donde sub-fábricas especializadas heredan de una fábrica abstracta y personalizan su comportamiento para diferentes productos. |
| **Client**           | Código o componente que utiliza la Abstract Factory. Interactúa solo con interfaces abstractas, sin conocer clases concretas.                        |

---

## ✅ ¿Cuándo usar Abstract Factory?

- Cuando los productos deben ser **consistentes entre sí**.
- Cuando se necesita **independencia** entre el sistema y la creación de objetos.
- Cuando se desea **encapsular la lógica de creación** de múltiples familias de objetos.


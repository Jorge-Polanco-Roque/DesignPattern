# 🏗️ Creational Design Pattern  
## ✳️ Factory Method vs Abstract Factory

### 🎯 Propósito
- **Factory Method**: Crea objetos dentro de una jerarquía de clases específica, permitiendo que las subclases decidan qué clase concreta instanciar.
- **Abstract Factory**: Crea familias de objetos relacionados o dependientes sin especificar sus clases concretas.

### ⚙️ Creación de objetos
- **Factory Method**: Define un método que las subclases implementan para crear una instancia específica.
- **Abstract Factory**: Define un conjunto de métodos abstractos que devuelven objetos de una familia relacionada.

### 🔗 Relación entre objetos
- **Factory Method**: Produce objetos individuales con una interfaz común.
- **Abstract Factory**: Produce grupos de objetos relacionados con relaciones específicas y consistencia entre ellos.

### 🔁 Alcance de la variación
- **Factory Method**: Maneja la variación dentro de una sola jerarquía.
- **Abstract Factory**: Maneja la variación entre múltiples jerarquías o familias de productos.

### 🧪 Granularidad
- **Factory Method**: Opera a nivel de **un solo objeto**.
- **Abstract Factory**: Opera a nivel de **familias de objetos** relacionadas.

---

## ✅ Abstract Factory - Ventajas

- **🔗 Bajo acoplamiento**: El cliente interactúa solo con interfaces abstractas.
- **🧩 Consistencia en familias de productos**: Evita combinaciones incompatibles.
- **🧱 Interfaz consistente**: Simplifica el código cliente.
- **🔄 Sustitución fácil**: Permite cambiar implementaciones fácilmente si siguen la misma interfaz.
- **📦 Extensibilidad**: Permite agregar nuevas familias sin modificar el código existente.

---

## ❌ Abstract Factory - Desventajas

- **📈 Complejidad**: Más clases e interfaces pueden dificultar mantenimiento.
- **📦 Limitada flexibilidad para nuevos productos**: Agregar tipos nuevos requiere modificar varias clases.
- **🧬 Duplicación de código**: Si la lógica de creación es similar, se repite en distintas fábricas.
- **🔒 Acoplamiento fuerte entre fábrica y producto**: Cambiar un producto implica modificar múltiples fábricas.
- **🕐 Flexibilidad limitada en tiempo de ejecución**: Elección de fábrica suele hacerse en tiempo de compilación o inicialización.

---

## 📌 Recomendaciones para Abstract Factory

- **🔧 Define interfaces abstractas** para productos y fábricas (usa ABCs en Python).
- **🏭 Implementa clases concretas** que cumplan las interfaces.
- **📥 Usa inyección de dependencias o configuración** para instanciar fábricas.
- **✅ Aplica el principio de sustitución de Liskov (LSP)**: Las implementaciones concretas deben poder sustituirse sin afectar al cliente.
- **🗂 Usa registros o archivos de configuración** si tienes muchas fábricas/productos.
- **🔗 Alta cohesión y bajo acoplamiento**: Cada fábrica concreta debe crear una familia específica.
- **📛 Convenciones de nombres claras** para interfaces y productos.
- **📝 Documenta responsabilidades** de cada clase/método.
- **🧪 Escribe tests unitarios** para validar que los productos creados funcionan correctamente.

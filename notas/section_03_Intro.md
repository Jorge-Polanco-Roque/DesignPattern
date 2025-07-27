# 🏭 Patrón de Diseño Creacional: Factory Method

El **Factory Method** es un patrón de diseño creacional que define una interfaz para la creación de objetos, pero delega a las **subclases la decisión de qué clase concreta instanciar**. Este enfoque permite diseñar sistemas flexibles, extensibles y de bajo acoplamiento.

---

## 🎯 Objetivo del Patrón

- Desacoplar el código cliente de las clases concretas que necesita instanciar.
- Promover la **extensibilidad** sin necesidad de modificar el código existente (Principio Abierto/Cerrado).
- **Encapsular la lógica de creación** de objetos dentro de una jerarquía de clases.

---

## 💡 Idea Central

El patrón Factory Method se aplica cuando se desea **trasladar la responsabilidad de creación de objetos** a subclases, permitiendo que cada una determine qué tipo de objeto concreto debe generarse.

> Esto proporciona **flexibilidad, reutilización de código y facilidad de mantenimiento**, al permitir la incorporación de nuevos tipos de objetos sin alterar el código base.

---

## ✅ Beneficios Clave

- 🔄 **Extensibilidad**: nuevas clases pueden integrarse sin modificar las existentes.
- 🔒 **Desacoplamiento**: el cliente no necesita conocer las clases concretas.
- 🧱 **Reutilización**: reutiliza lógica de creación común en la clase base.
- ⚙️ **Versatilidad**: ideal para bibliotecas o frameworks que permiten a los usuarios extender comportamientos.

---

## 🧠 Analogía del Mundo Real

> Imagina una empresa matriz (la clase base) que define el proceso general de producción,  
pero permite a cada fábrica regional (subclase) decidir **qué producto específico** fabricar.  
Así se garantiza una producción estandarizada, pero con productos personalizados según la región.

---

## 🗂️ Terminología del Patrón Factory Method

| Término              | Definición |
|----------------------|------------|
| **Product**          | Clase base abstracta o interfaz que define los métodos comunes que implementarán todos los productos. |
| **Concrete Product** | Clases concretas que implementan la interfaz del producto. Representan variaciones específicas. |
| **Creator**          | Clase abstracta que declara el método de fábrica. Puede incluir lógica general para productos. |
| **Concrete Creator** | Subclases que implementan el método de fábrica y devuelven instancias de productos concretos. |

---

## 🔧 Método de Fábrica y el Rol del Cliente

### 🏗️ **Factory Method**
Es el método abstracto que se declara en el `Creator` y define el contrato para la creación de objetos. Las subclases (`Concrete Creators`) implementan este método para decidir qué producto concreto instanciar.

### 👤 **Client**
Es el código que **utiliza el método de fábrica** para crear objetos. Interactúa con el `Creator` sin conocer los detalles de implementación de las clases concretas que serán instanciadas.

---

## 📌 Conclusión

El patrón **Factory Method** permite construir sistemas extensibles y fácilmente modificables, al separar la lógica de creación de objetos de su uso. Es ideal para aplicaciones donde el tipo exacto de los objetos a crear puede variar según el contexto o configuración del cliente.

# 🧱 Relación entre Clases en el Patrón de Diseño Builder

Este diseño sigue el patrón **Builder**, separando la construcción de un objeto complejo (una casa) de su representación. A continuación se explica la relación entre las clases involucradas:

---

## 🏠 `House`: El Producto Final

- Representa la **casa construida**.
- Contiene atributos como:
  - `floor` (piso)
  - `wall` (paredes)
  - `roof` (techo)
  - `furniture` (muebles)
- No tiene lógica de construcción. Solo almacena el resultado.

---

## 🧰 `HouseBuilder`: El Constructor Genérico

- Clase que **sabe cómo construir** una casa paso a paso.
- Define métodos como:
  - `set_floor(amount)`
  - `set_wall(amount)`
  - `set_roof(amount)`
  - `set_furniture(name, amount)`
- Tiene un atributo `self.house` donde guarda el objeto que va construyendo.
- Actúa como **clase base reutilizable** para otros builders.

---

## 🏡 `SmallHouseBuilder`: Constructor Especializado

- **Hereda** de `HouseBuilder`.
- Define pasos concretos con valores predefinidos:
  - `build_floor()` → `"Small Floor"`
  - `build_wall()` → `"Small Wall"`
  - `build_roof()` → `"Small Roof"`
  - `build_furnitures()` → `"Chair": 2`, `"Table": 1`
- Reutiliza los métodos de `HouseBuilder`, pero encapsula una **versión específica** del producto.

---

## 👷‍♂️ `Contractor`: El Director

- Recibe un builder como parámetro.
- Orquesta la construcción paso a paso mediante:
  - `builder.build_floor()`
  - `builder.build_wall()`
  - `builder.build_roof()`
  - `builder.build_furnitures()`
- **No conoce** los detalles de implementación de `HouseBuilder` ni de `House`.
- Puede trabajar con cualquier builder compatible (`SmallHouseBuilder`, `LuxuryHouseBuilder`, etc.).

---

## 🔗 Relación entre Clases

| Clase              | Relación                                                                 |
|-------------------|--------------------------------------------------------------------------|
| `HouseBuilder`     | Construye el objeto `House` paso a paso                                 |
| `SmallHouseBuilder` | Hereda de `HouseBuilder` y define una casa preconfigurada              |
| `Contractor`       | Usa un builder para orquestar la construcción (actúa como Director)     |
| `House`            | Es el resultado final construido por el builder                         |

---

## 🎯 Beneficios de esta Arquitectura

- **Desacoplamiento:** el director no necesita saber cómo se implementa cada parte.
- **Flexibilidad:** se pueden crear múltiples tipos de casas con distintos builders.
- **Reutilización:** lógica común centralizada en `HouseBuilder`.

---

## 📌 Conclusión

El patrón Builder permite construir objetos complejos de forma estructurada, desacoplando el **qué se construye** (producto) del **cómo se construye** (proceso).


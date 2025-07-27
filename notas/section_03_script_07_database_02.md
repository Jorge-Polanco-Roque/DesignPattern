# 🏭 Creational Design Patterns: Factory Method vs Factory Pattern

## 🧩 Introducción

Dentro de los patrones creacionales, **Factory Pattern** y **Factory Method** son soluciones populares para la creación de objetos. Aunque similares en propósito (centralizar la creación de instancias), **difieren en estructura, escalabilidad y adherencia a principios SOLID**.

---

## 🏗️ ¿Qué es Factory Pattern (Patrón de Fábrica Simple)?

- Es una **clase concreta** que contiene un método para decidir qué objeto crear.
- Suele tener **condicionales** (`if`, `switch`) para decidir qué instancia devolver.
- El cliente llama directamente a la fábrica.

### 📌 Características
- ✅ Fácil de implementar.
- ❌ Menos flexible (rompe el Principio Abierto/Cerrado).
- 🔧 No requiere herencia.

### 📦 Ejemplo:

```python
class SimpleVehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError("Tipo de vehículo no soportado.")
```

---

## 🧠 ¿Qué es Factory Method?

- Define una **interfaz abstracta** para crear objetos, pero permite que las subclases decidan qué clase instanciar.
- Utiliza herencia para permitir la creación de objetos por clases concretas.

### 📌 Características
- ✅ Alto desacoplamiento y extensibilidad.
- ✅ Aplica el Principio Abierto/Cerrado.
- 🔧 Usa herencia y polimorfismo.

### 📦 Ejemplo:

```python
from abc import ABC, abstractmethod

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()
```

---

## 🔍 Diferencias Clave

| Característica                   | Factory Pattern (Simple Factory) | Factory Method                   |
|----------------------------------|----------------------------------|----------------------------------|
| Nivel de abstracción             | Bajo (clase concreta)            | Alto (clase abstracta + herencia)|
| Cumple con Open/Closed Principle| ❌ No                            | ✅ Sí                            |
| Extensibilidad                   | Limitada                         | Alta                             |
| Complejidad                      | Baja                             | Media                            |
| Uso de condicionales             | Sí                               | No (usa polimorfismo)            |
| Uso de herencia                  | No                               | Sí                               |
| Escenario ideal                  | Proyectos simples                | Arquitecturas escalables         |

---

## ✅ ¿Cuándo usar cada uno?

- Usa **Factory Pattern**:
  - Cuando quieres una forma rápida de encapsular la creación de objetos.
  - Cuando el número de tipos de objetos es limitado y estable.

- Usa **Factory Method**:
  - Cuando esperas que se agreguen nuevos tipos de objetos en el futuro.
  - Cuando deseas cumplir con los principios SOLID y mantener bajo acoplamiento.

---

## 🧩 Conclusión

> Ambos patrones ayudan a separar la lógica de creación de objetos del código cliente.  
> El **Factory Pattern** es simple y directo.  
> El **Factory Method** es más flexible y orientado a sistemas extensibles y mantenibles.

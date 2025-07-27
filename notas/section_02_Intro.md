# 🧱 Patrón de Diseño Creacional: Builder - Introducción

El **patrón de diseño Builder** es un patrón creacional que se utiliza para crear objetos complejos paso a paso. Permite producir diferentes tipos y representaciones de un objeto utilizando el **mismo código de construcción**.

---

## 💡 Idea Principal

La idea principal del patrón Builder es **separar la construcción** de un objeto complejo de su representación.

> Esto permite que **el mismo proceso de construcción** pueda generar **diferentes representaciones** del objeto.

---

## ✅ ¿Por qué usar el patrón Builder?

- Es útil cuando se necesita construir objetos con **muchos parámetros opcionales**.
- Permite **especificar qué parámetros usar y en qué orden**.
- Evita la necesidad de crear múltiples constructores sobrecargados con largas listas de parámetros.

---

## 🛠️ Analogía del mundo real

> Como pedir un sándwich personalizado:  
Tú decides **qué ingredientes** incluir y en **qué orden**, pero el cocinero sigue **el mismo proceso de preparación** para todos los sándwiches.


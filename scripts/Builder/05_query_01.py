from typing import List  # Para tipado de listas (List[str])

# 🧱 Clase QueryBuilder: Aplica el patrón Builder para construir consultas SQL de forma encadenada
class QueryBuilder:
    def __init__(self):
        self._query = ""  # Inicializa la consulta como cadena vacía

    # Agrega cláusula SELECT con columnas separadas por coma
    def select(self, columns: List):
        self._query += f"SELECT {', '.join(columns)} "
        return self  # Retorna self para permitir el encadenamiento

    # Agrega cláusula FROM con el nombre de la tabla
    def from_(self, table):
        self._query += f"FROM {table} "
        return self

    # Agrega cláusula WHERE con condiciones unidas por AND
    def where(self, conditions: List):
        self._query += f"WHERE {' AND '.join(conditions)} "
        return self

    # Agrega cláusula ORDER BY con columnas separadas por coma
    def order_by(self, columns: List):
        self._query += f"ORDER BY {', '.join(columns)} "
        return self

    # Agrega cláusula LIMIT con un valor numérico
    def limit(self, limit: int):
        self._query += f"LIMIT {limit} "
        return self

    # Devuelve la consulta construida
    def get_query(self):
        return self._query.strip()  # .strip() elimina espacios al final

# 🧪 Ejemplo de uso del builder
if __name__ == "__main__":
    builder = QueryBuilder()
    
    # Construcción encadenada de una consulta SQL
    query = builder.select(['name', 'age']) \
                   .from_('users') \
                   .where(['age > 18', 'active = true']) \
                   .order_by(['age DESC']) \
                   .limit(10) \
                   .get_query()

    # Imprime la consulta final generada
    print(query)

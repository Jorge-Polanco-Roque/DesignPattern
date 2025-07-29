from abc import ABC, abstractmethod

# 1. Interfaz abstracta para conexión a base de datos
class DataConnection(ABC):
    @abstractmethod
    def connect(self):
        """Método obligatorio para establecer una conexión"""
        pass

# 2. Implementaciones concretas para MySQL y Postgres
class MySQLConnection(DataConnection):
    def connect(self):
        print("Connecting to MySQL database...")

class PostgresConnection(DataConnection):
    def connect(self):
        print("Connecting to Postgres database...")

# 3. Interfaz abstracta para el cursor (ejecución de queries)
class Cursor(ABC):
    @abstractmethod
    def execute(self, query: str):
        """Método obligatorio para ejecutar una consulta"""
        pass

# 4. Implementaciones concretas del cursor
class MySQLCursor(Cursor):
    def execute(self, query: str):
        print(f"Executing MySQL query: {query}")

class PostgresCursor(Cursor):
    def execute(self, query: str):
        print(f"Executing Postgres query: {query}")

# 5. Fábrica abstracta: define qué métodos deben implementarse
class AbstractFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DataConnection:
        """Debe retornar un objeto tipo DataConnection"""
        pass

    @abstractmethod
    def create_cursor(self) -> Cursor:
        """Debe retornar un objeto tipo Cursor"""
        pass

# 6. Fábricas concretas para MySQL y Postgres
class MySQLFactory(AbstractFactory):
    def create_connection(self) -> DataConnection:
        return MySQLConnection()

    def create_cursor(self) -> Cursor:
        return MySQLCursor()

class PostgresFactory(AbstractFactory):
    def create_connection(self) -> DataConnection:
        return PostgresConnection()

    def create_cursor(self) -> Cursor:
        return PostgresCursor()

# 7. Cliente que selecciona una fábrica según el input del usuario
def client():
    factories = dict(mysql=MySQLFactory(), postgres=PostgresFactory())
    fact_list = ", ".join(factories)

    while True:
        db = input(f"Select a database ({fact_list}): ").strip().lower()

        if db in factories:
            break
        else:
            print(f"Invalid database selection. Please choose from: {fact_list}")

    print("="*30)
    return factories.get(db)

# 8. Main: uso real de la fábrica seleccionada
if __name__ == "__main__":
    db_factory = client()  # Se elige la fábrica (MySQL o Postgres)
    db_connect = db_factory.create_connection()  # Se obtiene la conexión correspondiente
    db_cursor = db_factory.create_cursor()       # Se obtiene el cursor correspondiente

    db_connect.connect()                         # Se establece la conexión
    db_cursor.execute("SELECT * FROM Student")   # Se ejecuta una consulta

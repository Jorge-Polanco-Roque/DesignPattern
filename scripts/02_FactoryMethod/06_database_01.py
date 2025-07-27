from abc import ABC, abstractmethod

############ FACTORY METHOD DP ############

# 1. Producto abstracto
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        """Define una operación que todos los productos concretos deben implementar"""
        pass

# 2. Productos concretos
class MySQLConnection(DatabaseConnection):
    def connect(self):
        return "Connectiong to MySQL Database"

class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to PostgreSQL Database"

# 3. Creador abstracto (Factory)
class DatabaseConnectionFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DatabaseConnection:
        """Define el contrato de creación, pero no especifica la clase concreta"""
        pass

# 4. Creadores concretos (Factory)
class MYSQLConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return MySQLConnection()

class PostgreSQLConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return PostgreSQLConnection()

# 5. Código del cliente
if __name__ == "__main__":
    """
    El cliente utiliza las fábricas concretas para crear conexiones a bases de datos
    sin conocer los detalles de implementación de cada tipo de conexión.
    """
    def connect_to_database(factory: DatabaseConnectionFactory):
        connection = factory.create_connection()
        print(f"Cliente: estoy trabajando con -> {connection.connect()}")

    mysql_factory = MYSQLConnectionFactory()
    connect_to_database(mysql_factory)

    postgreql_factory = PostgreSQLConnectionFactory()
    connect_to_database(postgreql_factory)


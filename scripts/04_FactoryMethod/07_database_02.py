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

class DatabaseFactory(ABC):
    def __init__(self):
        self.factory = dict(mysql=MySQLConnection, postgresql=PostgreSQLConnection)

    def create_connection(self, db_type: str) -> DatabaseConnection:
        """Crea una conexión a la base de datos según el tipo especificado"""
        if db_type in self.factory:
            connection_class = self.factory.get(db_type)
            return connection_class()

# 3. Código del cliente
if __name__ == "__main__":
    db_factory = DatabaseFactory()
    
    mysql_connection = db_factory.create_connection("mysql")
    print(mysql_connection.connect())  # Salida: Connectiong to MySQL Database

    postgresql_connection = db_factory.create_connection("postgresql")
    print(postgresql_connection.connect())  # Salida: Connecting to PostgreSQL Database
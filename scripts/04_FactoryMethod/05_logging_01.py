# Importamos herramientas para clases abstractas
from abc import ABC, abstractmethod

# ========================================
# INTERFAZ ABSTRACTA DEL PRODUCTO: LOGGER
# ========================================

class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        """Método que cada logger concreto debe implementar para registrar mensajes"""
        pass

# ========================================
# PRODUCTOS CONCRETOS: IMPLEMENTAN LOGGER
# ========================================

# Logger que imprime mensajes en consola
class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"[ConsoleLogger] {message}")

# Logger que escribe mensajes en un archivo
class FileLogger(Logger):
    def log(self, message: str):
        with open("log.txt", "a") as file:
            file.write(f"[FileLogger] {message}\n")

# Logger que simula guardar el mensaje en una base de datos
class DatabaseLogger(Logger):
    def log(self, message: str):
        # Simulación de registro en una base de datos
        print(f"[DatabaseLogger] {message}")

# ========================================
# INTERFAZ ABSTRACTA DEL CREATOR: FACTORY
# ========================================

class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        """Método de fábrica que deben implementar las factorías concretas"""
        pass

# ========================================
# FACTORÍAS CONCRETAS: CREAN LOGGERS
# ========================================

class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()

class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()

class DatabaseLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return DatabaseLogger()

# ========================================
# CÓDIGO DEL CLIENTE
# ========================================

def perform_logging(factory: LoggerFactory, message: str):
    """
    Función cliente que recibe una fábrica de loggers,
    crea el logger y registra un mensaje.
    """
    logger = factory.create_logger()
    logger.log(message)

# ========================================
# USO DEL PATRÓN FACTORY METHOD
# ========================================

print("***Logging with Factory Method Pattern***")
console_logger_factory = ConsoleLoggerFactory()
perform_logging(console_logger_factory, "This is a message to the console.")

print("\n***Logging with File Logger***")
file_logger_factory = FileLoggerFactory()
perform_logging(file_logger_factory, "This is a message to the file.")

print("\n***Logging with Database Logger***")
database_logger_factory = DatabaseLoggerFactory()
perform_logging(database_logger_factory, "This is a message to the database.")

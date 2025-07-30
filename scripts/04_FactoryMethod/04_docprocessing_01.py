# Importamos herramientas para clases abstractas
from abc import ABC, abstractmethod

# ============================
# INTERFAZ DEL PRODUCTO
# ============================

# Clase abstracta base para cualquier tipo de documento
class Document(ABC):
    @abstractmethod
    def open(self):
        """Método que debe implementar cada documento concreto"""
        pass

# ============================
# PRODUCTOS CONCRETOS
# ============================

# Documento tipo Word que implementa la interfaz Document
class WordDocument(Document):
    def open(self):
        return "Opening Word Document"

# Documento tipo PDF que implementa la interfaz Document
class PDFDocument(Document):
    def open(self):
        return "Opening PDF Document"

# Documento tipo CSV que implementa la interfaz Document
class CSVDocument(Document):
    def open(self):
        return "Opening CSV Document"

# ============================
# CREATOR (FACTORY)
# ============================

# Clase abstracta que define el método de fábrica
class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        """Método de fábrica que debe ser implementado por las fábricas concretas"""
        pass

# ============================
# FACTORÍAS CONCRETAS
# ============================

# Fábrica para crear documentos Word
class WordDocumentFactory(DocumentFactory):    
    def create_document(self) -> Document:
        return WordDocument()

# Fábrica para crear documentos PDF
class PDFDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PDFDocument()

# Fábrica para crear documentos CSV
class CSVDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return CSVDocument()

# ============================
# CÓDIGO DEL CLIENTE
# ============================

# Función que recibe una fábrica, crea un documento y lo procesa
def process_document(factory: DocumentFactory):
    document = factory.create_document()  # Crea el documento sin saber su tipo exacto
    print(document.open())                # Llama al método open del producto

# Uso del patrón: el cliente no sabe qué tipo de documento se está creando internamente
word_factory = WordDocumentFactory()
process_document(word_factory)  # Salida esperada: Opening Word Document

pdf_factory = PDFDocumentFactory()
process_document(pdf_factory)   # Salida esperada: Opening PDF Document

csv_factory = CSVDocumentFactory()
process_document(csv_factory)   # Salida esperada: Opening CSV Document

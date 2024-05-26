
Crea una clase ArchivoSeguro con un método leer_archivo que intente leer un archivo de texto. Si el archivo no existe, maneja la excepción e informa al usuario.

class ArchivoNoEncontradoError(Exception):
    def __init__(self, mensaje="El archivo no fue encontrado"):
        super().__init__(mensaje)

class ArchivoSeguro:
    def leer_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                return archivo.read()
        except FileNotFoundError:
            print("Error: El archivo no fue encontrado")

# Ejemplo de uso
archivo_seguro = ArchivoSeguro()
contenido = archivo_seguro.leer_archivo("archivo.txt")  # Salida esperada: Error: El archivo no fue encontrado si el archivo no existe
print(contenido)

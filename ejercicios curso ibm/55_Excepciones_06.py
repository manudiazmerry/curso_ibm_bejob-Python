


# Crea una clase Persona con un método set_edad que valide que la edad no sea negativa. 
# Si se proporciona una edad negativa, lanza una excepción personalizada.

class EdadNegativaError(Exception):
    def __init__(self, mensaje="La edad no puede ser negativa"):
        super().__init__(mensaje)

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edad = None

    def set_edad(self, edad):
        try:
            if edad < 0:
                raise EdadNegativaError()
            self.edad = edad
        except EdadNegativaError as e:
            print(f"Error: {e}")

# Ejemplo de uso
persona = Persona("Juan")
persona.set_edad(25)  # Salida esperada: Ningún error
print(persona.edad)  # Salida esperada: 25
persona.set_edad(-5)  # Salida esperada: Error: La edad no puede ser negativa

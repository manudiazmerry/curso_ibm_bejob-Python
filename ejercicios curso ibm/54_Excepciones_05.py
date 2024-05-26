

Crea una clase DivisorSeguro con un método divide que realice una división entre dos números y maneje la excepción de división por cero.

class DivisionPorCeroError(Exception):
    def __init__(self, mensaje="No se puede dividir entre cero"):
        super().__init__(mensaje)

class DivisorSeguro:
    def divide(self, num1, num2):
        try:
            if num2 == 0:
                raise DivisionPorCeroError()
            return num1 / num2
        except DivisionPorCeroError as e:
            print(f"Error: {e}")

# Ejemplo de uso
divisor = DivisorSeguro()
print(divisor.divide(10, 2))  # Salida esperada: 5.0
print(divisor.divide(10, 0))  # Salida esperada: Error: No se puede dividir entre cero

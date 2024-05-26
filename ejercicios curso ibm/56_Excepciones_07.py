Crea una clase Calculadora con un método calcula_raiz que calcule la raíz cuadrada de un número. Si el número es negativo, lanza una excepción personalizada.

import math

class NumeroNegativoError(Exception):
    def __init__(self, mensaje="No se puede calcular la raíz cuadrada de un número negativo"):
        super().__init__(mensaje)

class Calculadora:
    def calcula_raiz(self, num):
        try:
            if num < 0:
                raise NumeroNegativoError()
            return math.sqrt(num)
        except NumeroNegativoError as e:
            print(f"Error: {e}")

# Ejemplo de uso
calc = Calculadora()
print(calc.calcula_raiz(16))  # Salida esperada: 4.0
print(calc.calcula_raiz(-4))  # Salida esperada: Error: No se puede calcular la raíz cuadrada de un número negativo

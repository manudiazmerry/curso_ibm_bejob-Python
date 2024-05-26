
Crea una clase IngresoSeguro con un método solicitar_numero que solicite al usuario ingresar un número entero. Si el usuario ingresa un valor no numérico, maneja la excepción y vuelve a solicitar el número.

class IngresoSeguro:
    def solicitar_numero(self):
        while True:
            try:
                num = int(input("Introduce un número entero: "))
                return num
            except ValueError:
                print("Error: Debes ingresar un número entero válido")

# Ejemplo de uso
ingreso = IngresoSeguro()
numero = ingreso.solicitar_numero()  # Salida esperada: Sigue solicitando hasta que se ingrese un número entero
print(f"Número ingresado: {numero}")

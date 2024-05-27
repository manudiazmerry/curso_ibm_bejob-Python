import os

def clear_screen():
    # Detecta el sistema operativo y ejecuta el comando adecuado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix (Linux y macOS)
        os.system('clear')

# Limpiar la pantalla al iniciar el programa
clear_screen()

# Resto del programa
print("Pantalla limpia. Bienvenido al programa.")
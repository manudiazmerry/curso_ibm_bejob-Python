
#------------------------------------------------------------------------------------------------------------

import os

def clear_screen():
    # Detecta el sistema operativo y ejecuta el comando adecuado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix (Linux y macOS)
        os.system('clear')


#------------------------------------------------------------------------------------------------------------

def mostrar_menu():
    clear_screen()
    print('----------------- Menú de Opciones -----------------')
    print('1. Añadir tarea nueva')
    print('2. Marcar tarea como completada')
    print('3. Mostrar lista de tareas')
    print('4. Eliminar tarea')
    print('5. Salir')
    print('----------------------------------------------------')

#------------------------------------------------------------------------------------------------------------

def obtener_opcion():
    rango = (1,5)
    while True:
        entrada = input('Introduzca número de opción del menú y pulse enter: ')
        try:
            opcion = int(entrada)
            if rango[0] <= opcion <= rango[1]:
                break
            else:
                mostrar_menu()
                print(f'"{opcion}" no es una opción del menú (núm. entero fuera de rango)')
        except ValueError:
            mostrar_menu()
            print(f'"{entrada}" no es una opción del menú (núm. entero no válido)')

    return opcion

#------------------------------------


mostrar_menu()
opcion = obtener_opcion()

if opcion == 1:
    
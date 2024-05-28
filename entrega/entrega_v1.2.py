
'''
Requisitos:
Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione 
una lista de tareas pendientes.

El programa deberá permitir al usuario realizar las siguientes operaciones:

ok  • Agregar una nueva tarea: El programa deberá permitir al usuario agregar una nueva tarea a
    la lista de tareas pendientes.

ok  • Marcar una tarea como completada: El programa deberá permitir al usuario marcar una tarea 
    como completada, dada su posición en la lista.

ok  • Mostrar todas las tareas: El programa deberá imprimir en pantalla todas las tareas
    pendientes, numeradas y mostrando su estado (completada o pendiente).

    • Eliminar una tarea: El programa deberá permitir al usuario eliminar una tarea de la lista,
    dada su posición.

El programa deberá incluir las siguientes características:

ok  • Manejo de excepciones: El programa deberá manejar excepciones en caso de que el
    usuario ingrese una opción no válida o una posición que no exista en la lista.

    • Comentarios explicativos: El código deberá estar comentado para explicar su
    funcionamiento en cada parte relevante.

'''

# a partir de las indicaciones del enunciado concluimos que necesitaremos, al menos,
# objetos de la clase tarea y de la clase lista
# de todos los los atributos y métodos que los objetos de cada clase pueden tener, 
# en el proceso de abstracción delimitamos los que serán necesarios y creamos las clases

# BORRAR no haremos método constructor con parámetros para que el usuario no meta valores no válidos 
# BORRAR meter método str para print objeto


#------------------------------------------------------------------------------------------------------------

import os

def clear_screen():
    # Detecta el sistema operativo y ejecuta el comando adecuado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix (Linux y macOS)
        os.system('clear')

    print('----------------- Área de mesajes -----------------\n')

#------------------------------------------------------------------------------------------------------------

def mostrar_menu():
    print('\n')
    print('----------------- Menú de Opciones -----------------')
    print('1. Añadir tarea nueva')
    print('2. Marcar tarea como completada')
    print('3. Eliminar tarea')
    print('4. Mostrar lista de tareas')
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
                clear_screen()
                print(f'"{opcion}" no es una opción del menú (núm. entero fuera de rango)')
                mostrar_menu()
        except ValueError:
            clear_screen()
            print(f'"{entrada}" no es una opción del menú (núm. entero no válido)')
            mostrar_menu()

    return opcion

'''

def obtener_opcion():
    opciones = ('1','2','3','4','5')
    while True:
        entrada = input('Introduzca número de opción del menú y pulse enter: ')
        if entrada in opciones:
            break
        else:
            clear_screen()
            print(f'"{entrada}" no es una opción del menú')
            mostrar_menu()
        
    return int(entrada)
    
'''


#------------------------------------------------------------------------------------------------------------

def obtener_indice(min,max):
    rango = (min,max)
    while True:
        entrada = input('Introduzca número de posición de la tarea y pulse enter: ')
        try:
            indice = int(entrada)
            if rango[0] <= indice <= rango[1]:
                break
            else:
                clear_screen()
                print(f'"{indice}" posición no válida (núm. entero fuera de rango)')
                mostrar_menu()
        except ValueError:
            clear_screen()
            print(f'"{entrada}" posición no válida (núm. entero no válido)')
            mostrar_menu()

    return indice


#------------------------------------------------------------------------------------------------------------


class Tarea():

    contador = 1
    
    def __init__(self, s_contenido):
        self.s_contenido = s_contenido
        self.is_completada = False
        self.n_id = Tarea.contador
        Tarea.contador += 1

        
    def __str__(self):        
        estado = 'Pendiente'
        if self.is_completada:
            estado = 'Completada'     
        str_salida = ("{:>8}    {:<10}   {}".format(self.n_id, estado, self.s_contenido[:100]))
        return str_salida





#------------------------------------------------------------------------------------------------------------

clear_screen()
print('Bienvenido a su gestor de tareas!')

lista_tareas = []

tarea = Tarea('ir a la compra')
lista_tareas.append(tarea)
tarea = Tarea('lavar car')
lista_tareas.append(tarea)
tarea = Tarea('paseo en bici')
lista_tareas.append(tarea)





while True:

    mostrar_menu()
    opcion = obtener_opcion()

    if opcion == 1:
        contenido = input('Contenido de la tarea: ')
        tarea = Tarea(contenido)
        lista_tareas.append(tarea)
        clear_screen()
        print('Tarea "' + contenido + '" añadida')
    elif opcion == 2:
        indice = obtener_indice(1,len(lista_tareas))
        lista_tareas[indice-1].is_completada = True
        clear_screen()
        print('Completada tarea:', indice,  lista_tareas[indice-1].s_contenido[:25])
    elif opcion == 3:
        indice = obtener_indice(1,len(lista_tareas))
        eliminada = lista_tareas.pop(indice-1)
        clear_screen()
        print('Eliminada tarea:', indice,  eliminada.s_contenido[:25])
    elif opcion == 4:
        clear_screen()
        print("Posición    Id    Estado       Contenido\n")
        if len(lista_tareas) == 0:
            print('lista vacia')
        else:
            for i in range(len(lista_tareas)):
                print('{:>5}'.format(i+1), lista_tareas[i])        
    elif opcion == 5:
        break

#str_salida = ("{:<4}{:<10}{}".format(str(self.n_id), estado, self.s_contenido))


#------------------------------------------------------------------------------------------------------------


'''
Requisitos:
Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione una lista de 
tareas pendientes. El programa deberá permitir al usuario realizar las siguientes operaciones:
    • Agregar una nueva tarea: El programa deberá permitir al usuario agregar una nueva tarea a
    la lista de tareas pendientes.
    • Marcar una tarea como completada: El programa deberá permitir al usuario marcar una tarea 
    como completada, dada su posición en la lista.
    • Mostrar todas las tareas: El programa deberá imprimir en pantalla todas las tareas
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

gn_id_tarea = 1

class Tarea:
    
    def __init__(self, s_contenido, gn_id_tarea):
        self.s_contenido = s_contenido
        self.is_completada = False
        self.n_posicion = gn_id_tarea
        gn_id_tarea += 1

        
    def __str__(self):
        return str(self.n_posicion) + 'Contenido: ' + self.s_contenido[:21] + '\nCompletada: ' + str(self.is_completada)
    

tarea_01 = Tarea('hacer la comida',gn_id_tarea)
print(tarea_01)

tarea_02 = Tarea('poner lavadora',gn_id_tarea)
tarea_02.is_completada = True
print(tarea_02)

#-----------------------------------------------------------------------------------Menu
def menu():

    while True:
        print('\n')
        print('___Menú____________________ introduzca número de opción y pulse enter:')
        print('1. Añadir tarea nueva')
        print('2. Modificar tarea')
        print('3. Marcar tarea como completada')
        print('4. Mostrar lista de tareas')
        print('5. Eliminar tarea')
        print('6. Salir')

        try:
            opcion = int(input('Seleccione una opción: '))

            if opcion == 1:
                descripcion = input('Ingrese la descripción de la nueva tarea: ')
                lista_de_tareas.agregar_tarea(descripcion)
            elif opcion == 2:
                posicion = int(input('Ingrese el número de la tarea a marcar como completada: '))
                lista_de_tareas.marcar_tarea_como_completada(posicion)
            elif opcion == 3:
                lista_de_tareas.mostrar_tareas()
            elif opcion == 4:
                posicion = int(input('Ingrese el número de la tarea a eliminar: '))
                lista_de_tareas.eliminar_tarea(posicion)
            elif opcion == 5:
                print('Saliendo del programa...')
                break
            else:
                print('Opción no válida. Por favor, intente nuevamente.')
        except ValueError:
            print('Error: Debe ingresar un número.')
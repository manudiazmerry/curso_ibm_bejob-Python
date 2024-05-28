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


class Tarea:
    def __init__(self, descripcion):
        """
        Inicializa una nueva tarea con una descripción y un estado de no completada.
        
        :param descripcion: Descripción de la tarea.
        """
        self.descripcion = descripcion
        self.completada = False

    def marcar_como_completada(self):
        """
        Marca la tarea como completada.
        """
        self.completada = True

    def __str__(self):
        """
        Devuelve una representación en cadena de la tarea, mostrando su estado.
        """
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"
class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, contenido):
        self.tareas.append(contenido)

    def __str__(self):
        return str(self.tareas)

# Crear una instancia de la clase ListaTareas
lista_01 = ListaTareas()
lista_01.agregar_tarea('contenido tarea 1')
lista_01.agregar_tarea('contenido tarea 2')

print(lista_01)

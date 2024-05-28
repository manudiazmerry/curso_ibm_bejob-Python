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



#-----------------------------------------------------------------------

class ListaDeTareas:
    def __init__(self):
        """
        Inicializa una nueva lista de tareas vacía.
        """
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """
        Agrega una nueva tarea a la lista de tareas.
        
        :param descripcion: Descripción de la nueva tarea.
        """
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        print(f"Tarea '{descripcion}' agregada.")

    def marcar_tarea_como_completada(self, posicion):
        """
        Marca una tarea como completada dada su posición en la lista.
        
        :param posicion: Posición de la tarea en la lista (1-indexada).
        """
        try:
            self.tareas[posicion - 1].marcar_como_completada()
            print(f"Tarea {posicion} marcada como completada.")
        except IndexError:
            print("Error: La posición ingresada no existe en la lista.")

    def mostrar_tareas(self):
        """
        Muestra todas las tareas numeradas y su estado.
        """
        if not self.tareas:
            print("La lista de tareas está vacía.")
        else:
            for i, tarea in enumerate(self.tareas, start=1):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self, posicion):
        """
        Elimina una tarea de la lista dada su posición.
        
        :param posicion: Posición de la tarea en la lista (1-indexada).
        """
        try:
            tarea_eliminada = self.tareas.pop(posicion - 1)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
        except IndexError:
            print("Error: La posición ingresada no existe en la lista.")


#-------------------------------------------------------------------------

def menu():
    """
    Muestra el menú de opciones y gestiona la interacción con el usuario.
    """
    lista_de_tareas = ListaDeTareas()

    while True:
        print("\n--- Menú de Tareas Pendientes ---")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                descripcion = input("Ingrese la descripción de la nueva tarea: ")
                lista_de_tareas.agregar_tarea(descripcion)
            elif opcion == 2:
                posicion = int(input("Ingrese el número de la tarea a marcar como completada: "))
                lista_de_tareas.marcar_tarea_como_completada(posicion)
            elif opcion == 3:
                lista_de_tareas.mostrar_tareas()
            elif opcion == 4:
                posicion = int(input("Ingrese el número de la tarea a eliminar: "))
                lista_de_tareas.eliminar_tarea(posicion)
            elif opcion == 5:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número.")

# if __name__ == "__main__":

menu()


# --------------------------------------



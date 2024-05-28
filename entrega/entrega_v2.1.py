
'''
Requisitos:
Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione 
una lista de tareas pendientes.

El programa deberá permitir al usuario realizar las siguientes operaciones:

  • Agregar una nueva tarea: El programa deberá permitir al usuario agregar una nueva tarea a
    la lista de tareas pendientes.

  • Marcar una tarea como completada: El programa deberá permitir al usuario marcar una tarea 
    como completada, dada su posición en la lista.

  • Mostrar todas las tareas: El programa deberá imprimir en pantalla todas las tareas
    pendientes, numeradas y mostrando su estado (completada o pendiente).

  • Eliminar una tarea: El programa deberá permitir al usuario eliminar una tarea de la lista,
    dada su posición.

El programa deberá incluir las siguientes características:

  • Manejo de excepciones: El programa deberá manejar excepciones en caso de que el
    usuario ingrese una opción no válida o una posición que no exista en la lista.

  • Comentarios explicativos: El código deberá estar comentado para explicar su
    funcionamiento en cada parte relevante.

'''

# a partir de las indicaciones del enunciado concluimos que necesitaremos, al menos,
# objetos de la clase tarea
# de todos los los atributos y métodos que los objetos de cada clase pueden tener, 
# en el proceso de abstracción delimitamos los que serán necesarios
# en este caso los objetos tarea deberían tener un contenido o descripción y un estado (completada/pendiente)
# por otro lado necesitaremos una lista de tareas en la que los objetos tarea se almacenaran ordenados 


# Primero haremos algunas funciones (procedimientos si no devuelven return) que nos facilitaran el trabajo más adelante
# ya que son pequeños bloques o módulos de código que se repetirían varias veces

#------------------------------------------------------------------------------------------------------------

# sacado de internet, lo usaremos cada vez que nos interese borrar la pantalla de la consola durante la ejecución
import os
def preparar_pantalla():
    # Detecta el sistema operativo y ejecuta el comando adecuado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix (Linux y macOS)
        os.system('clear')


#------------------------------------------------------------------------------------------------------------

# procedimiento para mostrar el menú de opciones
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

# función para obtener introducido por el usuario, un número entero que se corresponda con alguna opción del menú
def obtener_opcion():
    rango = (1,5)    #rango de opciones del menú
    while True:    #bucle infinito, se repite hasta que haya un break       
        entrada = input('Introduzca número de opción del menú y pulse enter: ') 
        try:
            opcion = int(entrada) #si el string del input no se puede parsear a numero entero porque no son dígitos da error y va al except
            if rango[0] <= opcion <= rango[1]:# si no da error sigue y comprueba que el número esta en el rango de opciones del menú
                break #si es una opción del menú correcta, sale del ciclo while true
            else: #si no es un número del menú avisa y se repite el while
                preparar_pantalla() #esto es para que no baje la linea del input con cada entrada no válida
                print(f'"{opcion}" no es una opción del menú (núm. entero fuera de rango)')
                mostrar_menu()
        except ValueError: #si dio error el parseo del string del input a entero avisa y se repite el while
            preparar_pantalla()
            print(f'"{entrada}" no es una opción del menú (núm. entero no válido)')
            mostrar_menu()

    return opcion #cuando sale del while con el break llega a qui y devuelve la opción que introdujo el usuario


'''
Así sería más simplificado, pero no se usa el manejo de excepcioones que nos pide el enunciado del ejercicio:

def obtener_opcion():
    opciones = ('1','2','3','4','5')
    while True:
        entrada = input('Introduzca número de opción del menú y pulse enter: ')
        if entrada in opciones:
            break
        else:
            preparar_pantalla()
            print(f'"{entrada}" no es una opción del menú')
            mostrar_menu()
        
    return int(entrada)    
'''


#------------------------------------------------------------------------------------------------------------

# función similar al anterior preo más genérica, para obtener un número introducido por el usuario
# pero en este caso no sería para un número del menú dentro de un rango cerrado sino para seleccionar 
# el número o posición de una tarea en la lista de tareas (índice). Al cambiar la cantidad de tareas es un rango variable
def obtener_indice(min,max):
    rango = (min,max)
    while True:
        entrada = input('Introduzca número de posición de la tarea y pulse enter: ')
        try:
            indice = int(entrada)
            if rango[0] <= indice <= rango[1]:
                break
            else:
                preparar_pantalla()
                print(f'"{indice}" posición no válida (núm. entero fuera de rango)')
                mostrar_menu()
        except ValueError:
            preparar_pantalla()
            print(f'"{entrada}" posición no válida (núm. entero no válido)')
            mostrar_menu()

    return indice


#------------------------------------------------------------------------------------------------------------

#las tareas de la lista serán objetos de la clase Tarea

class Tarea():

    contador = 1 #hacemos un contador con una variable de clase para que cada objeto tarea tenga un id único
    
    #método constructor
    def __init__(self, s_contenido): #necesita que le pasemos el contenido de la tarea
        self.s_contenido = s_contenido #un atibuto será el contenido, es un string, se recibe por parámetro
        self.is_completada = False #otro atributo es si está completada (booleano), por defecto al instanciar está en false
        self.n_id = Tarea.contador #le asignamos un id único
        Tarea.contador += 1 #aumenta cada vez que se cra un objeto de la clase Tarea

        
    def __str__(self):  # cuando hagamos un print de un objeto de la clase Tarea imprimirá el return de esté método        
        estado = 'Pendiente' #por defecto el estado de las tareas es pendiente
        if self.is_completada: #a no ser que se haya modificado a True el atributo is_completada
            estado = 'Completada'     
        str_salida = ("{:>8}    {:<10}   {}".format(self.n_id, estado, self.s_contenido[:100]))
        #hacemos un string formateado a nuestra conveniencia con el id, el estado y el contenido de la tarea
        return str_salida


    def obtener_estado(self):
        return self.is_completada

    def cambiar_estado(self, estado):
        self.is_completada = estado

#------------------------------------------------------------------------------------------------------------

# haremos unas funciones para manejar la 'Lista de tareas' para estructurar y modular el programa con las funciones del menú
# añadir tarea, modificar tarea, eliminar tarea, mostrar lista de tareas


# función añadir tarea
def añadir_tarea():
    preparar_pantalla()
    contenido = input('Contenido de la tarea: ')
    tarea = Tarea(contenido)
    lista_tareas.append(tarea)
    preparar_pantalla()
    print('----------------- Área de mesajes -----------------\n')
    print('Tarea "' + contenido + '" añadida')



# función marcar tarea como completada
def marcar_completada():

    preparar_pantalla()
    if len(lista_tareas) == 0:
        print('----------------- Área de mesajes -----------------\n')
        print('No hay tareas para marcar, la lista de tareas está vacía')
    else:
        print('Marcar tarea como completada')
        indice = obtener_indice(1,len(lista_tareas))
        lista_tareas[indice-1].cambiar_estado(True)
        preparar_pantalla()
        print('----------------- Área de mesajes -----------------\n')
        print('Completada tarea:', indice,  lista_tareas[indice-1].s_contenido[:25])





# función eliminar tarea
def eliminar_tarea():
    preparar_pantalla()
    if len(lista_tareas) == 0:
        print('----------------- Área de mesajes -----------------\n')
        print('No hay tareas para eliminar, la lista de tareas está vacía')
    else:
        print('Eliminar tarea de la lista')
        indice = obtener_indice(1,len(lista_tareas))
        eliminada = lista_tareas.pop(indice-1)
        preparar_pantalla()
        print('----------------- Área de mesajes -----------------\n')
        print('Eliminada tarea:', indice,  eliminada.s_contenido[:25])
        



# función mostrar lista de tareas
def mostrar_lista():
    preparar_pantalla()
    if len(lista_tareas) == 0:
        print('----------------- Área de mesajes -----------------\n')
        print('La lista de tareas está vacía')
    else:
        print("----------------- Lista de Tareas -----------------\n")
        print("Posición    Id    Estado       Contenido")
        for i in range(len(lista_tareas)):
            print('{:>5}'.format(i+1), lista_tareas[i])
        print('\n\n')
        input('Presione enter para continuar....')
        preparar_pantalla()       
        print('----------------- Área de mesajes -----------------\n')



# función salir de la ejecución
def salir():
    pass


#------------------------------------------------------------------------------------------------------------
# Comienza la ejecución del programa

lista_tareas = [] #creamos una lista de tareas vacía

# comentar/descomentar por si se quiere arrancar con algunas tareas de prueba en la lista:
tarea = Tarea('ir a la compra')
lista_tareas.append(tarea)
tarea = Tarea('lavar car')
lista_tareas.append(tarea)
tarea = Tarea('paseo en bici')
#lista_tareas.append(tarea)
tarea = Tarea('hacer ejercicios de Python')
#lista_tareas.append(tarea)
tarea = Tarea('preparar la comida')
#lista_tareas.append(tarea)



preparar_pantalla()
print('----------------- Área de mesajes -----------------\n')
print('  ¡ Bienvenido al gestor de tareas !')


while True: #ejecución en bucle hasta que se introduzca opción 5 y se sale del bucle por el break

    mostrar_menu()
    opcion = obtener_opcion() 

    if opcion == 1:
        añadir_tarea()
    elif opcion == 2:
        marcar_completada()
    elif opcion == 3:
        eliminar_tarea()
    elif opcion == 4:
        mostrar_lista()
    elif opcion == 5:
        break




#------------------------------------------------------------------------------------------------------------


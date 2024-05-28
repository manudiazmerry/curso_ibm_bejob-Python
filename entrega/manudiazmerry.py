
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
def limpiar_pantalla():
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
    while True:    #bucle infinito, se repite hasta que haya un break (cuando sea un entero y dentro del rango)      
        entrada = input('Introduzca número de opción del menú y pulse enter: ') 
        try:
            opcion = int(entrada) #si el string del input no se puede parsear a numero entero porque no son dígitos da error y va al except
            if rango[0] <= opcion <= rango[1]:# si no da error sigue y comprueba que el número esta en el rango de opciones del menú
                break #si es una opción del menú correcta, sale del ciclo while true
            else: #si no es un número del menú avisa y se repite el while
                limpiar_pantalla() #esto es para que no baje la linea del input con cada entrada no válida
                print('----------------- Área de mesajes -----------------\n')
                print(f'"{opcion}" no es una opción del menú (núm. entero fuera de rango)')
                mostrar_menu()
        except ValueError: #si dio error el parseo del string del input a entero avisa y se repite el while
            limpiar_pantalla()
            print('----------------- Área de mesajes -----------------\n')
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
            limpiar_pantalla()
            print(f'"{entrada}" no es una opción del menú')
            mostrar_menu()
        
    return int(entrada)    
'''


#------------------------------------------------------------------------------------------------------------

# función similar al anterior preo más genérica, para obtener un número introducido por el usuario
# pero en este caso no sería para un número del menú dentro de un rango cerrado sino para seleccionar 
# el número o posición de una tarea en la lista de tareas (índice). Al cambiar la cantidad de tareas es un rango variable
def obtener_indice(min,max,titulo):
    rango = (min,max) #rango variable en función de lo larga que se ala lista de tareas
    limpiar_pantalla()
    print(titulo, '\n') #se recibe por parámetro según se este marcando completada o eliminando tarea
    generar_tabla_tareas() #para que el usuario pueda ver la tabla de tareas y saber que índice de tarea quiere introducir
    while True:
        entrada = input('Introduzca número de posición de la tarea y pulse enter: ')
        try:
            indice = int(entrada)
            if rango[0] <= indice <= rango[1]:
                break
            else:
                limpiar_pantalla()
                print(titulo, '\n')
                generar_tabla_tareas()
                print(f'"{indice}" posición no válida (núm. entero fuera de rango)')
        except ValueError:
            limpiar_pantalla()
            print(titulo, '\n')
            generar_tabla_tareas()
            print(f'"{entrada}" posición no válida (núm. entero no válido)')

    return indice


#------------------------------------------------------------------------------------------------------------

#las tareas de la lista serán objetos de la clase Tarea

class Tarea():

    contador = 1 #hacemos un contador con una variable de clase para que cada objeto tarea tenga un id único
    
    #método constructor
    def __init__(self, s_contenido): #necesita que le pasemos el contenido de la tarea
        self.s_contenido = s_contenido #un atibuto será el contenido, es un string, se recibe por parámetro
        self.__is_completada = False #otro atributo es si está completada (booleano), por defecto al instanciar está en false
                                    #lo ponemos como privado para que desde fuera solo se pueda acceder a él con métodos de la clase
        self.n_id = Tarea.contador #le asignamos un id único
        Tarea.contador += 1 #aumenta cada vez que se cra un objeto de la clase Tarea


    def cambiar_estado(self, estado): #método set para el único atributo del objeto que es modificable
        self.__is_completada = estado

    #métodos get de todos los atributos
    def obtener_estado(self): 
        return self.__is_completada
    
    def obtener_contenido(self): 
        return self.s_contenido
    
    def obtener_id(self): 
        return self.n_id
    

    def __str__(self):  # cuando hagamos un print de un objeto de la clase Tarea imprimirá el return de esté método        
        estado = 'Pendiente' #por defecto el estado de las tareas es pendiente
        if self.__is_completada: #a no ser que se haya modificado a True el atributo is_completada
            estado = 'Completada' 
        if self.s_contenido == '': self.s_contenido = '(vacía)'    
        str_salida = ("{:>8}    {:<10}   {}".format(self.n_id, estado, self.s_contenido[:100]))
        #hacemos un string formateado a nuestra conveniencia con el id, el estado y el contenido de la tarea
        return str_salida


#------------------------------------------------------------------------------------------------------------

# haremos unas funciones para manejar la 'Lista de tareas' para estructurar y modular el programa con las funciones del menú
# añadir tarea, modificar tarea, eliminar tarea, mostrar lista de tareas


# función añadir tarea
def añadir_tarea():
    limpiar_pantalla()
    print('-------------- Añadiendo nueva tarea --------------\n')
    contenido = input('Contenido de la nueva tarea: ')
    tarea = Tarea(contenido)
    lista_tareas.append(tarea)
    global mensaje
    mensaje = str('Tarea añadida: ' + lista_tareas[-1].obtener_contenido())



# función marcar tarea como completada
def marcar_completada():
    global mensaje
    if len(lista_tareas) == 0:
        mensaje = 'No hay tareas para marcar, la lista de tareas está vacía'
    else:
        indice = obtener_indice(1,len(lista_tareas),'---------- Marcar tarea como completada -----------')
        lista_tareas[indice-1].cambiar_estado(True)
        mensaje = str('Tarea marcada como completada: ' + lista_tareas[indice-1].obtener_contenido()[:25])



# función eliminar tarea
def eliminar_tarea():
    global mensaje
    if len(lista_tareas) == 0:
        mensaje = 'No hay tareas para eliminar, la lista de tareas está vacía'
    else:
        indice = obtener_indice(1,len(lista_tareas),'------------ Eliminar tarea de la lista ------------')
        eliminada = lista_tareas.pop(indice-1)
        mensaje = str('Eliminada tarea: ' + eliminada.obtener_contenido()[:25])



# función mostrar lista de tareas
def mostrar_lista():
    global mensaje
    if len(lista_tareas) == 0:
        mensaje = 'No hay lista que mostrar, la lista de tareas está vacía'
    else:
        generar_tabla_tareas()
        input('Presione enter para volver al menú....')
        mensaje = ''

# separamos esta parte en una función aparte para poder usarla cuando nos interese
def generar_tabla_tareas():
    print('Posición    Id    Estado       Contenido')
    print('¨¨¨¨¨¨¨¨    ¨¨    ¨¨¨¨¨¨       ¨¨¨¨¨¨¨¨¨')
    for i in range(len(lista_tareas)):
        print('{:>5}'.format(i+1), lista_tareas[i])
    print('\n---------------------------------------------------')
    



# función para confirmar que se quiere salir de la ejecución
def confirmar_salir():
    limpiar_pantalla()
    print('----------------- Área de mesajes -----------------\n')
    print('Confirmar')
    mostrar_menu()
    
    print('La lista de tareas solo persiste durante la ejecución del programa.\n'
          'Si sale, la lista de tareas actual se perderá.')
    confirmar = input('Escriba "salir" y presione enter para confirmar que quiere salir: ')

    if confirmar.lower() == 'salir': return (True)




#------------------------------------------------------------------------------------------------------------

#función que usaremos al arrancar el programa para opcionalmente rellenar una lista con tareas de ejemplo 

tareas_ejemplo = ['ir a la compra', 'lavar car', 'hacer ejercicios Python', 'paseo en bici', 'preparar la comida', 
                'encontrar trabajo', 'estudiar power BI', 'leer libro', 'jugar con los nenos', 'probar telescopio']

def rellenar_lista():
    limpiar_pantalla()
    print('Paso previo opcional')
    while True:
        cuantas = input('Cuántas tareas de ejemplo quiere en la lista inicialmente (0-10): ')
        try:
            cuantas = int(cuantas)
            if 0 <= cuantas <= 10:
                break
            else:
                limpiar_pantalla()
                print(f'"{cuantas}" es núm. entero fuera de rango')
        except ValueError:
            limpiar_pantalla()
            print(f'"{cuantas}" no es núm. entero válido')

    for i in range (0,cuantas):
        tarea_nueva = Tarea(tareas_ejemplo[i])
        lista_tareas.append(tarea_nueva)



#------------------------------------------------------------------------------------------------------------

# Aquí Comienza la ejecución del programa

lista_tareas = [] #creamos una lista de tareas vacía

rellenar_lista() #comentar/descomentar en función de si se quiere arrancar con algunas tareas de prueba en la lista

mensaje = '       ¡ Bienvenido al gestor de tareas !'



while True: #ejecución en bucle hasta que se introduzca opción 5 y se sale del bucle por el break

    limpiar_pantalla()
    print('----------------- Área de mesajes -----------------\n')
    print(mensaje)
    mostrar_menu()

    opcion = obtener_opcion() 

    if opcion == 1:
        añadir_tarea()
    elif opcion == 2:
        marcar_completada()
    elif opcion == 3:
        eliminar_tarea()
    elif opcion == 4:
        limpiar_pantalla()
        print('----------------- Lista de Tareas -----------------\n')
        mostrar_lista()
    elif opcion == 5:
        if confirmar_salir():
            limpiar_pantalla()
            print('\n\n   ¡ Hasta la próxima !   \n\n')
            break
        mensaje='No se ha confirmado la opción de salir'




#------------------------------------------------------------------------------------------------------------


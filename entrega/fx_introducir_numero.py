

#para los inputs, acepta números entre un máx. y un mín. indicados

#------------------------------------

def obtenerOpcion():
    rango = (1,5)
    while True:
        entrada = input('Introduzca número de opción del menú y pulse enter: ')
        try:
            opcion = int(entrada)
            if rango[0] <= opcion <= rango[1]:
                break
            else:
                print(f'"{opcion}" no es una opción del menú (fuera de rango)')
        except ValueError:
            print(f'"{entrada}" no es una opción del menú (núm. entero no válido)')

    return opcion

# Ejemplo de uso:
opcion = obtenerOpcion()
print(f"La opción del menú elegida es: {opcion}")





# Pone el cursor al inicio de la línea, la sobrescribe con espacios en blanco para borrarla y pone el cursor al ppio de nuevo
def borrar_linea():
    print('\r', ' '*100, '\r', end='')

   
    

print('linea primera', end='')
borrar_linea()
print('linea 2')


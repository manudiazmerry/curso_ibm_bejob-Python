

n_numero1 = 34
s_texto1 = "34"
print(n_numero1 == s_texto1)



miNumero = 65
miNumero2 = miNumero
print(miNumero)
print("La dirección de memoria es" , id(miNumero))
print(miNumero2)
print("La dirección de memoria es" , id(miNumero2))


miNumero+=2
print(miNumero)
print("La dirección de memoria es" , id(miNumero))
print(miNumero2)
print("La dirección de memoria es" , id(miNumero2))


a = (1, 2, 3, 4, 5)
print("La dirección de memoria es" ,
id(a))

a = {'a': 1, 'b': 2}
print(a)
print("La dirección de memoria es" ,
id(a))
a["c"] = 3
print(a)
print("La dirección de memoria es" ,
id(a))



a = 5
while a: # Utilizamos la propia variable como condición

 print (a, end=' ')
 if a == 2: break
 a -= 1

print ('\nFuera del Bucle.')
print('Valor de "a": {}'.format(a))

for i in range(2):
    print(f"Valor de la variable {i}")

for i in range(5,10):
    print(f"Valor de la variable {i}")

color = ["verde", "amarilla", "roja"]
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    for y in color:
        print(x, y)




a, b, c = map(int, input("Introduzca los números: ").split())

print("Los números son: ", end = " ")

print(a, b, c)

# Solicitar al usuario que introduzca tres números separados por espacios
a, b, c = map(int, input("Introduzca los números: ").split())

# Imprimir los números introducidos
print("Los números son: ", end=" ")
print(a, b, c)




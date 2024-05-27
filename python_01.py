import random
import math

random.random ()

lista = [1, 2, 3, 4]
random.choice(lista)

random.shuffle(lista)
lista

# recursividad
def factorial(x):
    if x>1:
     return x*factorial(x-1)
    else:
      return 1
print(factorial(4))


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
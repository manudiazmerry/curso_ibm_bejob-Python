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
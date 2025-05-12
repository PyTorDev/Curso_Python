# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.
my_tuple = (10, 20, 30, 40, 50)

print(my_tuple)
print(type(my_tuple))

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
second_tuple = (100, 200, 300, 400, 500)
print(second_tuple[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
# second_tuple.insert(0, 50) #No se puede modificar una tupla

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
third_tuple = (1, 2, 3, 3, 4, 5, 3)
print(third_tuple.count(3))

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
forth_tuple = ("Java", "Python", "JavaScript", "Python")
print(forth_tuple.index("Python"))

# 6. Concatena dos tuplas de las anteriores e imprime la tupla resultante.
sumed_tuples = my_tuple + second_tuple
print(sumed_tuples)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
fifth_tuple = (10, 20, 30, 40, 50)
print(fifth_tuple[2:4])

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
colors_tuple = ("rojo", "verde", "azul")
colors_tuple = list(colors_tuple)
colors_tuple[1] = "Amarillo"
colors_tuple = tuple(colors_tuple)
print(type(colors_tuple))
print(colors_tuple)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
del my_tuple
# print(my_tuple) #Esto da error porque my_tuple ha sido eliminado

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
alone_tuple = (1,)
print(type(alone_tuple))

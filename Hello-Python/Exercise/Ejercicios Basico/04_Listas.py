# 1. Crea una lista con los números del 1 al 5 e imprímela.
my_list = [1, 2, 3, 4, 5]
print(my_list)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
second_list = [10, 20, 30, 40, 50]
print(second_list[2])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.
third_list = [1, 2, 3, 4, 5]
third_list.append(6)
print(third_list)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
second_list.insert(1, 15)
print(second_list)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
forth_list = [10, 20, 30, 30, 40, 50]
forth_list.remove(30)
print(forth_list)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.
num_poped = my_list.pop()
print(num_poped)
print(my_list)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.
fifth_list = [100, 200, 300, 400, 500]
fifth_list.reverse()
print(fifth_list)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
sixth_list = [3, 1, 4, 2, 5]
sixth_list.sort()
print(sixth_list)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
seventh_list = [1, 2, 3]
eighth_list = [4, 5, 6]
ninth_list = seventh_list + eighth_list
print(ninth_list)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
tenth_list = [10, 20, 30, 40, 50]
last_list = tenth_list[0:3]
print(last_list)

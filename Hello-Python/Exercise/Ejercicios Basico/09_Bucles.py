# 1. Usa un bucle while para imprimir los números del 1 al 10.
n = 1
while n <= 10:
    print(n)
    n += 1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.
my_list = [10, 20, 30, 40, 50]
for i in my_list:
    print(i)

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.
n = 1
r = 0
while n <= 100:
    r += n
    n += 1
else:
    print(r)

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
w = "Python"
for i in w:
    print(i)

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
n = 0
while n <= 50:
    n += 1
    if n % 7 == 0:
        print(f"{n} es el primer numero dividible entre 7 en el rango 1-50")
        break

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
my_dict = {"name": "Brais", "age": 37, "country": "Galicia"}
for i in my_dict:
    print(i)

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.
n = 0
while n < 20:
    n += 1
    if n % 2 == 0:
        print(n)

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.
i = 1
for i in range(10, 0, -1):
    print(i)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].
new_list = [30, 10, 30, 20, 30, 40]
counter = 0
for i in new_list:
    if i == 30:
        counter += 1
else:
    print(f"30 aparece {counter} veces en la lista")

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
name_list = ["Aitor", "Pedro", "Brais", "Manolo", "Albaro"]
for i in name_list:
    if i == "Brais":
        print("Ya encontre Brais")
        break
    print(f"Voy por el nombre {i}")

# 1. Genera una lista utilizando comprensión con los números del 0 al 10.

my_range_list = [i for i in range(0, 11)]
print(my_range_list)

# 2. Crea una lista utilizando comprensión con los cuadrados de los números del 1 al 10.

my_square_list = [i**2 for i in range(1, 11)]
print(my_square_list)

# 3. Genera una lista utilizando comprensión con los números pares del 0 al 20.

my_even_list = [i for i in range(0, 21) if i % 2 == 0]
print(my_even_list)

# 4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprensión.

celsius_list = [15, 25, 50, 100]

fahrenheit_list = [i * 1.8 + 32 for i in celsius_list]
print(fahrenheit_list)

# 5. Crea una lista utilizando comprensión con los caracteres de una cadena.

my_str = "Python"

str_list = [i for i in my_str]
print(str_list)

# 6. Filtra una lista de palabras y deja solo las que tienen más de 4 letras utilizando comprensión.

words_list = ["aitor", "moneda", "zapato", "oso", "mal"]

words_filtred = [i for i in words_list if len(i) > 4]
print(words_filtred)

# 7. Aumenta en 5 cada número de una lista con comprensión usando una función externa.


def sum_five(list):
    list = [i + 5 for i in list]
    return list


print(sum_five(my_range_list))

# 8. Crea una lista de booleanos que indique si cada número es mayor que 10 utilizando comprensión.

n = [i for i in range(5, 16)]
my_boolean_list = [i > 10 for i in n]
print(my_boolean_list)

# 9. Multiplica solo los números impares por 3 en una lista utilizando comprensión.

new_n = [i for i in range(0, 11)]
my_new_even_list = [i * 3 for i in new_n if i % 2 != 0]
print(my_new_even_list)

# 10. Usa comprensión de listas anidada para generar una matriz 3x3 con números del 1 al 9.

matrix = [[row * 3 + col + 1 for col in range(3)] for row in range(3)]
print(matrix)

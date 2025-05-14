# 1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting(name="Desconocido"):
    print(f"Hola, {name}")


# personalized_greeting()


# 2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.
def multiply(n1, n2):
    result = n1 * n2
    return result


# 3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# 4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.
def convert_to_uppercase(text):
    return text.upper()


# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos.
def arbitrary_sum(*n):
    result = 0
    for num in n:
        result += num
    return result


# 6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
def generate_full_greeting(name, surname):
    return f"Hola, {name} {surname}."


print(generate_full_greeting(name="Aitor", surname="López"))


# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.
def power(base, exponent):
    result = base**exponent
    return result


# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.
def calculate_average(n1, n2, n3):
    avergae = (n1 + n2 + n3) / 3
    return avergae


# 9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.
def count_characters(text):
    count = len(text)
    return count


# 10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*texts):
    for text in texts:
        print(text)


display_messages("pedro", "come", "patatas")

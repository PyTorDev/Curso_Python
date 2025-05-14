# 1. Crea una lambda que sume dos números.

sum2 = lambda a, b: a + b  # noqa: E731
print(sum2(3,5))

# 2. Crea una lambda que calcule el cuadrado de un número.

square = lambda x: x**2  # noqa: E731
print(square(40))

# 3. Crea una lambda que devuelva el mayor de dos números.

bigger_num = lambda x, y: max(x, y)  # noqa: E731
print(bigger_num(56,98))

# 4. Crea una lambda que sume 10 a un número dado.

plus_ten = lambda n: n + 10  # noqa: E731
print(plus_ten(2))

# 5. Crea una lambda que devuelva el último carácter de una cadena.

last_caracter = lambda text: text[-1]  # noqa: E731
print(last_caracter('hola'))

# 6. Crea una lambda que indique si una palabra tiene más de 6 letras.

more_six_caratcers = lambda word: len(word) > 6 # Devuelve true si word tiene mas de 6 letras  # noqa: E731
print(more_six_caratcers('hola'))

# 7. Crea una lambda que convierta una cadena a minúsculas.

str_lower = lambda text: text.lower()  # noqa: E731
print(str_lower('HOLA'))

# 8. Crea una lambda que devuelva True si un número es positivo.

is_positive = lambda n: n > 0 # Devuelve true si n es mayor que cero  # noqa: E731
print(is_positive(-23))

# 9. Crea una lambda que devuelva "Cadena vacía" si el string está vacío.

empty_str = lambda text: 'Cadena vacía' if len(text) == 0 else False  # noqa: E731
print(empty_str('Hola'))

# 10. Crea una lambda que calcule el precio final con un impuesto añadido del 21%.

final_price = lambda price: (1 + 0.21) * price  # noqa: E731
print(final_price(35))
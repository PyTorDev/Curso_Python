# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"

print(len(text))

# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.
cad_1 = "Hola"
cad_2 = "Python"

print(cad_1, cad_2)

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
cad_salto = "Esta cadena tiene aqui \nun salto de linea"

print(cad_salto)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name = "Aitor"
surname = "Lopez"
age = "27"

print(f"Soy {name} {surname}, y tengo {age} años.")

# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.
word = "Python"
w1, w2, w3, w4, w5, w6 = word

print(w1)
print(w2)
print(w3)
print(w4)
print(w5)
print(w6)

# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
word2 = "Programacion"
print(word2[3:8])

# 7. Invierte la cadena “Python” usando slicing y muestra el resultado.
print(word[::-1])

# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
print("Aprendiendo Python".upper())

# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
cadena = "Programacion en Python"
print(cadena.count("n"))

# 10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
print("12345".isnumeric())

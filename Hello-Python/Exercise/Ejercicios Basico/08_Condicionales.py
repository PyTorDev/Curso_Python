# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
def positivo_negativo(n):
    if n == 0:
        print(f"{n} es igual a 0")
    elif n < 0:
        print(f"{n} es negatvio")
    else:
        print(f"{n} es positivo")


# positivo_negativo(-2)


# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.
def mayor_edad():
    age = int(input("Indicame tu edad: "))
    if age >= 18:
        print(f"Si tienes {age} ya eres mayor de edad")
    else:
        print(f"Vaya, con {age} todavia eres menor de edad")


# mayor_edad()


# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.
def cadena_vacia():
    cadena = input("Introduce o no una cadena de texto: ")
    if cadena:
        print("Es una cadena de texto normal")
    else:
        print("Es una cadena de texto, pero esta vacia")


# cadena_vacia()


# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
def compara_neros():
    n1 = int(input("Introduce el primer nero: "))
    n2 = int(input("Introduce el segundo nero: "))
    if n1 < n2:
        print(f"{n1} es menor que {n2}")
    elif n1 > n2:
        print(f"{n1} es mayor que {n2}")
    else:
        (print(f"{n1} y {n2} son iguales"))


# compara_neros()


# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
def divisible():
    n = int(input("Introduce un nero: "))
    if n % 3 == 0 and n % 5 == 0:
        print(f"{n} es divisible entre 3 y entre 5")
    else:
        print(f"{n} no es divisible entre 3 y 5 a la vez")


# divisible()


# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
def par_impar():
    n = int(input("Introduce un numero: "))
    if n % 2 == 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")


# par_impar()


# 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
def votar():
    age = int(input("Indicame tu edad: "))
    if age >= 18:
        print(f"Si tienes {age} puedes votar sin problema en las proximas elecciones")
    elif age == 16 or age == 17:
        print(
            f"Buno, con {age} años, puedes vota pero necesitas un permiso especial de tu tutor legal"
        )
    else:
        print(f"Vaya, con {age} todavia no puedes votar")


# votar()
# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
def passw():
    right_pass = "1234"
    user_pass = input("Introduce la contraseña: ")
    if user_pass == right_pass:
        print("Contraseña aceptada")
    else:
        print("Error. La contraseña no coincide")


# passw()


# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
def in_range(min=10, max=20):
    n = int(input("Introduce un numero: "))
    if n >= min and n <= max:
        print(f"{n} esta entre {min} y {max}")
    else:
        print(f"{n} no esta entre {min} y {max}")


# in_range()


# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
def semaforo():
    color = input("Introduce el color del semaforo (rojo, amarillo o verde): ")
    if color == "rojo":
        print("Hay que detenerse")
    elif color == "amarillo":
        print("Hay que mantenerse alerta para pasar")
    elif color == "verde":
        print("Adelnate, pasa sin problema")
    else:
        print(f"{color} no es un color correcto")


# semaforo()

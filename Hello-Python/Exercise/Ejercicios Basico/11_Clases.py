import math


# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un método "make_sound" que imprima un sonido genérico.
# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacénala en una propiedad pública. Añade el método "make_sound" que imprima un sonido dependiendo de la especie.
class Animal:
    def __init__(self, species):
        self.specie = species

    def make_sound(self):
        if self.specie == "dog":
            print("guau, guau")
        elif self.specie == "cat":
            print("miauuu")
        elif self.specie == "ape":
            print("hu hu hu")
        else:
            print("grrrr")


monkey = Animal("ape")
dog = Animal("dog")
cat = Animal("cat")
lion = Animal("lion")

monkey.make_sound()
dog.make_sound()
cat.make_sound()
lion.make_sound()


# 3. Crea una clase llamada "Car" con las propiedades públicas "brand" y "model". Además, debe tener una propiedad privada "_speed" que inicialmente será 0.
# 4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad en 10 unidades. Añade también un método "brake" que reduzca la velocidad en 10 unidades. Asegúrate de que la velocidad no sea negativa.
class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def accelerate(self):
        self.__speed += 10

    def brake(self):
        if self.get_speed() >= 0:
            self.__speed -= 10


my_car = Car("Ferrari", "LaFerrari")

my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
my_car.brake()
print(my_car.get_speed())


# 5. Crea una clase "Book" que tenga propiedades como "title" (público) y "author" (privado). Añade un método para obtener el autor y otro para cambiar el título del libro.
class Book:
    def __init__(self, title, author):
        self.title = title
        self._author = author

    def get_author(self):
        return self._author

    def set_title(self):
        self.title = input("Introduce el nuevo titulo: ")
        print(f"El nuevo titulo es: {self.title}")


my_book = Book("El señor de los anillos", "Tolkkien")
print(my_book.title)
my_book.set_title()


# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un método para calcular y devolver la nota media del estudiante.
class Estudiante:
    def __init__(self, name, surname, califications=[]):
        self.name = name
        self.surname = surname
        self.califications = califications

    def califications_auverage(self):
        sum = 0
        for i in self.califications:
            sum += i
        auverage = sum / len(self.califications)
        return auverage


aitor = Estudiante("Aitor", "López", [5, 5, 5])
print(aitor.califications_auverage())


# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit_money(self, money):
        self.balance += money

    def whithdrow_money(self, money):
        if money <= self.balance:
            self.balance -= money
        else:
            print(f"No hay suficiente dinero. Sus fondos actuales son {self.balance}")


my_account = BankAccount("Aitor", 1200)
my_account.whithdrow_money(2000)
print(my_account.balance)
my_account.deposit_money(1000)
print(my_account.balance)


# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un método que calcule la distancia entre dos puntos.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = x, y

    def distance(self):
        distance = math.sqrt((self.x**2) + (self.y**2))
        return distance


# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora.
class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def salary(self):
        salary = self.hours_worked * self.hourly_wage
        return salary


# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un método para agregar un producto al inventario y otro para mostrar todos los productos disponibles.
class Store:
    def __init__(self, invetory=None):
        self.inventory = (
            invetory if invetory is not None else []
        )  # Si se da una lista, self.inventory sera esa lista, sino, se crea una lista nueva vacia

    def add_product(self, product):
        self.inventory.append(product)

    def get_inventory(self):
        print(self.inventory)

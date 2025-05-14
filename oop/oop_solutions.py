# EASY
# 1. Basic class design --
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 2. Class methods --
class Counter:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1
    def decrement(self):
        self.value -= 1
    def reset(self):
        self.value = 0

# MEDIUM
# 1. Inheritance --
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, no_of_doors, fuel_type):
        super().__init__(make, model, year)
        self.doors = no_of_doors
        self.fuel_type = fuel_type

# 2. Encapsulation --
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

# HARD
# 1. Polymorphism and Abstract class --
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# 2. Complex class relationships --
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

class Library:
    def __init__(self):
        self.books = []         
        self.members = []     
        self.checked_out = {} 
    def add_book(self, book):
        self.books.append(book)
    def register_member(self, member):
        self.members.append(member)
    def checkout_book(self, book, member):
        if book in self.books and book not in self.checked_out:
            self.checked_out[book] = member
        else:
            print("Book not available")
    def return_book(self, book, member):
        if self.checked_out.get(book) == member:
            del self.checked_out[book]
    def is_book_available(self, book):
        return book in self.books and book not in self.checked_out

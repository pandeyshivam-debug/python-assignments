from oop_solutions import *

# EASY
# 1. Basic class design --
rect = Rectangle(5, 10)
print("Rectangle area:", rect.area())
print("Rectangle perimeter:", rect.perimeter())
circle = Circle(7)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

# 2. Class methods --
counter = Counter()
counter.increment()
counter.increment()
print(counter.value)  
counter.decrement()
print(counter.value) 
counter.reset()
print(counter.value)

# MEDIUM
# 1. Inheritance --
car = Car("BMW", "M3GTR", 2020, 4, "Diesel")
print(car.make)      
print(car.model)     
print(car.year)       
print(car.doors)      
print(car.fuel_type)  

# 2. Encapsulation --
account = BankAccount("123456", 15000)
print(account.get_balance())  
account.deposit(500)
print(account.get_balance())  
account.withdraw(200)
print(account.get_balance())  
print(account.get_account_number()) 

# HARD
# 1. Polymorphism and Abstract class --
circle = Circle(5)         
rectangle = Rectangle(4, 6)  
triangle = Triangle(3, 4, 5)  
shapes = [circle, rectangle, triangle]
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")


# 2. Complex class relationships --
library = Library()
book1 = Book("Book1", "Shivam")
book2 = Book("DSA book #3", "Pandey")

library.add_book(book1)
library.add_book(book2)

member = Member("ShivamPandey", "SKP2025")
library.register_member(member)

library.checkout_book(book1, member)
print(library.is_book_available(book1))  
print(library.is_book_available(book2))   

library.return_book(book1, member)
print(library.is_book_available(book1))   

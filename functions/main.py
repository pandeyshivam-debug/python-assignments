from functions_solutions import *
# average
numbers = [3,5,65,7,34,9]
print(f"Average of {numbers} is: {calculate_average(numbers)}")
print(".....")

# default parameters
print(greet_user("Sai", "Hi"))
print(greet_user("Shivam"))

# variable arguments
print(f"Total price of 150, 175, 35, 220, 68 after discount of 10% is: {calculate_total(150, 175, 35, 220, 68, rate=10)}")

# closures
double = create_multiplier(2)
triple = create_multiplier(3)
print("Using closure...")
print(f"Double of 7 is: {double(5)}")
print(f"Triple of 18 is: {triple(5)}")
print(".....")

# recursion
print("2^6 is: ", power(2, 6))

# higher-order functions
def add_one(x): return x + 1
def double(x): return x * 2
def square(x): return x * x
f = compose(square, double, add_one)
# print(f"After using compose- answer: {f(3)}")
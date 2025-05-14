# EASY
# 1. Function basics --
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# 2. Default parameters --
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# MEDIUM
# 1. Varibale arguments --
def calculate_total(*prices, rate = 0):
    total = sum(prices)
    total -= (total * rate/100)
    return total

# 2. Closures --
def create_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier

# HARD
# 1. Recursion --
def power(num, pow):
    if pow == 0:
        return 1
    else:
        return num * power(num, pow - 1)
    
# 2. Higher-Order Functions --
def compose(*functions):
    def composed_function(x):
        for function in reversed(functions):
            x = function(x)
        return x
    return composed_function


# EASY
# 1. Tuple basics --
def swap_pairs(t):
    swapped = []
    i = 0
    while i < len(t) - 1:
        swapped.append(t[i + 1])
        swapped.append(t[i])
        i += 2
    if i < len(t):
        swapped.append(t[i])
    return tuple(swapped)

# 2. Tuple unpacking --
def get_stats(numbers):
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]
    for num in numbers:
        total += num
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    average = total / len(numbers)
    return (minimum, maximum, total, average)

# MEDIUM
# 1. Named tuples --
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'grades'])
def top_student(students):
    top = students[0]
    for student in students:
        if sum(student.grades) / len(student.grades) > sum(top.grades) / len(top.grades):
            top = student
    
    return top

# 2. Tuple as keys --
def count_coordinate_occurrences(coords):
    count_dict = {}
    for coord in coords:
        if coord in count_dict:
            count_dict[coord] += 1
        else:
            count_dict[coord] = 1
    return count_dict

# HARD
# 1. Complex data structure --
def group_by_department(employees):
    department_dict = {}
    for emp in employees:
        name, department, salary = emp
        if department not in department_dict:
            department_dict[department] = (0, [], 0) 
        total_salary, names_list, count = department_dict[department]
        department_dict[department] = (total_salary + salary, names_list + [name], count + 1)
    for department in department_dict:
        total_salary, names_list, count = department_dict[department]
        department_dict[department] = (total_salary / count, names_list)
    return department_dict

# 2. Recursive tuple processing --
def flatten_tuple(my_tuple):
    flat_list = []
    for item in my_tuple:
        if type(item) == tuple:
            flat_list.extend(flatten_tuple(item))  
        else:
            flat_list.append(item)
    return tuple(flat_list) 

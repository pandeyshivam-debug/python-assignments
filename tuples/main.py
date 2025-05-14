from tuple_solutions import *

my_tuple = (1, 2, 3, 4, 5)
swapped = swap_pairs(my_tuple)
print(f"Original tuple: {my_tuple}")
print(f"Swapped tuple: {swapped}")

numbers_tuple = (5, 1, 9, 3, 7)
stats = get_stats(numbers_tuple)
print("Input:", numbers_tuple)
print("Output:", stats)

students = [
        Student(name="Shivam", age=23, grades=(90, 85, 92)),
        Student(name="Pandey", age=22, grades=(78, 81, 85))
    ]
top = top_student(students)
print(f"Top Student: {top.name}, Age: {top.age}, Grades: {top.grades}")

coordinates = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
occurrences = count_coordinate_occurrences(coordinates)
print("Coordinate Occurrences:", occurrences)

employees = [
        ("Shivam", "HR", 50000),
        ("Pandey", "Engineering", 75000)
    ]
department_stats = group_by_department(employees)
print("Department statistics:", department_stats)

nested_tuple = ((1, 2), (3, (4, 5)), (6, (7, (8, 9))))
flattened = flatten_tuple(nested_tuple)
print("Flattened Tuple:", flattened)
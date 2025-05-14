from list_solutions import *

# EASY
# 1. List operations --
list = [1,4,56,32,84,5,12]
print(f"filtered {list} for even numbers: {list}")

# 2. List manipulation --
list1 = [3,5,8, 47]
list2 = [1, 29, 35]
print(f"merged {list1} and {list2}: {list1}")

# MEDIUM
# 1. List comprehension --
new_matrix = generate_matrix(3, 4)
print(f"generated matrix: {new_matrix}")

# 2. Transpose matrix --
transposed = transpose_matrix(new_matrix)
print(f"transposed matrix: {transposed}")

# HARD
# 1. Advanced list operations --
numbers = [1, 3, 7, 1, 2, 6, 3, 2]
peaks = find_peaks(numbers)
print(f"peaks in {numbers}: {peaks}")

# 2. List algorithms --
list = [2,4,8,9,10]
rotated = rotate_list(list, 3)
print(f"rotated {list} by 3: {rotated}")


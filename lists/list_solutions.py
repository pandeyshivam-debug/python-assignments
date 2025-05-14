# EASY
# 1. List operations --
def filter_even_numbers(numbers): return [num for num in numbers if num % 2 == 0]

# 2. List manipulation --
def merge_sorted_lists(list1, list2): return sorted(list1 + list2)

# MEDIUM
# 1. List comprehension --
def generate_matrix(rows, cols): 
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(i * j)
        matrix.append(row)
    return matrix

# 2. Transpose matrix --
def transpose_matrix(matrix):
    transposed = []
    rows = len(matrix)
    cols = len(matrix[0])
    
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    return transposed

# HARD
# 1. Advanced list operations --
def find_peaks(numbers):
    peaks = []
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            peaks.append(numbers[i])
    return peaks

# 2. List algorithms --
def rotate_list(list, k):
    n = len(list)
    k = k % n 
    rotated = []
    for i in range(n - k, n):
        rotated.append(list[i]) 
    for i in range(n - k):
        rotated.append(list[i])

    return rotated


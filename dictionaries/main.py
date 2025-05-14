from dictionary_solutions import *

original_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
inverted = invert_dictionary(original_dict)
print("Inverted Dictionary:", inverted)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5}
merged = merge_dictionaries(dict1, dict2)
print("Merged Dictionary:", merged)

text = "the quick brown fox jumps over the lazy dog"
frequencies = word_frequencies(text)
print("Word Frequencies:", frequencies)

contact_book = {}
contact_book = add_contact(contact_book, 'ShivamKP', '95286--88', 'email@gmail.comm', 'Kondapur')
contact_book = add_contact(contact_book, 'SKP', '736--74--5', 'gmail.email.com', 'Hyderabad')
print("Contact Book:", contact_book)

student_grades = {
    'Shivam': [85, 90, 78, 92],
    'Pandey': [88, 79, 85, 91]
}
transformed = transform_grades(student_grades)
print("Transformed Grades:", transformed)


file_paths = [
    "folder1/file1.txt", 
    "folder1/folder2/file2.txt", 
    "folder3/file3.txt"
]
tree = generate_tree(file_paths)
print("Generated File Structure Tree:", tree)
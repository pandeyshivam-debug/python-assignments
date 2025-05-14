# EASY
# 1. Dictionary basics --
def invert_dictionary(d):
    inverted_dict = {}
    for key, value in d.items():
        inverted_dict[value] = key
    return inverted_dict

# 2. Dictionary operations --
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy() 
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] = value
        else:
            merged_dict[key] = value
    return merged_dict

# MEDIUM
# 1. Dictionary comprehension --
def word_frequencies(text):
    words = text.split()
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    
    return freq_dict

# 2. Nested dictionaries --
def add_contact(contact_book, name, phone=None, email=None, address=None):
    if name in contact_book:
        contact_book[name]['phone'] = phone if phone else contact_book[name].get('phone')
        contact_book[name]['email'] = email if email else contact_book[name].get('email')
        contact_book[name]['address'] = address if address else contact_book[name].get('address')
    else:
        contact_book[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
    return contact_book

# HARD
# 1. Dictionary transformation --
def transform_grades(grades):
    transformed = {}
    for student, grade_list in grades.items():
        average = sum(grade_list) / len(grade_list)
        highest = max(grade_list)
        lowest = min(grade_list)
        transformed[student] = {
            'average': average,
            'highest': highest,
            'lowest': lowest
        }
    return transformed

# 2. Advanced dictionary operations --
def generate_tree(file_paths):
    tree = {}
    for path in file_paths:
        parts = path.split('/') 
        current = tree
        for i in range(len(parts)):
            part = parts[i]
            if i == len(parts) - 1:
                current[part] = {}
            else:
                if part not in current:
                    current[part] = {}
                current = current[part]
    return tree
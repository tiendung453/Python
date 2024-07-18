# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Miumiu'
dog['color'] = 'black_brown'
dog['breed'] = 'VietNam'
dog['legs'] = 4
dog['age'] = 9
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status
#    skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Tien',
    'last_name':'Dung',
    'gender':'Male',
    'age':21,
    'marital status':True,
    'skills':['C','C++','STM32','ESP32','PYTHON'],
    'country':'Viet Nam',
    'city':'Ha Noi',
    'address':'Cau Giay'
}

# 4. Get the length of the student dictionary
print('Length of the student:', len(student))

# 5. Get the value of skills and check the data type, it shuold be list
value_of_skill = student.get('skills')
print('Skill:', value_of_skill)
print('Type:', type(value_of_skill))

# 6. Modify the skills values by adding one or two skill
student['skills'].append('DSA')
print('Skill:', value_of_skill)

# 7. Get the dictionary keys as a list
keys = student.keys()
print(keys)

# 8. Get the dictionary value as a list
values = student.values()
print(values)

# 9. Change the dictionary to a list of tuples uing items() method
list_tuple_of_dict = student.items()
print(list_tuple_of_dict)

# 10. Delete one of the items in the dictionary
del student['address']
print(keys)

# 11. Delete one of the dictionaries
del student

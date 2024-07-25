names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [first_name+' '+last_name for sublist in names for first_name, last_name in sublist]
print(output)
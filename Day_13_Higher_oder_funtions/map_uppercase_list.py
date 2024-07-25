countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def uppercase_list(name):
    return name.upper()
names_upper_cased = map(uppercase_list,countries)
print(list(names_upper_cased))
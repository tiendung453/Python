# 1. Create an empty tuple
empty_tuple = tuple()

# 2. Create a tuple containing names of your sisters and your brothers
tuple_name_sis = ('Tham','Tien')
tuple_name_bro = ('Dung',)

# 3. Join brothers and sisters tuples and assign it to siblings
tuple_siblings = tuple_name_sis + tuple_name_bro
print(tuple_siblings)

# 4. How many siblings do you have
print("Number of siblings: ", len(tuple_siblings))

# 5. Modify the siblings tuple and add the name of your father and mother ans assign it to family_members
parents_tuple = ('Thang','The')
family_members = parents_tuple + tuple_siblings
print(family_members)

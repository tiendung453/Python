# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    for i in range(0, len(lst), 1):
        lst[i] = lst[i].upper()
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
capitalize_list_items(food_staff)
print(food_staff)

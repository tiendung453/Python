lst = [1,'e',3,5,'g','gh']
def get_string_lists(lst):
    return[i for i in lst if type(i) == str]
print(get_string_lists(lst))
    
        

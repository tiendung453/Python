import random
from random import randint
def seven_elements_array():
    lst = []
    for i in range(7):
        lst.append(randint(0,9))
    return lst
print(seven_elements_array())
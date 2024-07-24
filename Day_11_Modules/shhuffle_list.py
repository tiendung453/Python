import random 
def shuffle_list(lst):
    shuffle_lst = []
    for i in range(len(lst)):
        random_values = random.choice(lst)
        shuffle_lst.append(random_values)
        lst.remove(random_values)
    print(shuffle_lst)
lst = [1,2,3,4,5]
shuffle_list(lst)


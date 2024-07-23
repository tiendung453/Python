# 10. reserve_list
def reserve_list(lst):
    reserved_list = []
    for i in range(len(lst)-1, -1, -1):
        reserved_list.append(lst[i])
    print(reserved_list)
numbers = [1,2,3,4]
reserve_list(numbers)
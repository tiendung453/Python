list_of_lists = [[[1, 2, 4]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
print(flattened_list)

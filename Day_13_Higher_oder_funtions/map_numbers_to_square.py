numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def num_to_square(num):
    return num**2
numbers_square = map(num_to_square,numbers)
print(list(numbers_square))

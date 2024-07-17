# 1. Declare an empty list
empty_list = []
print (empty_list)

# 2. Declare a list with more than 5 items
lst = [ '1', '2', '3', '4', '5', '6' ]

# 3. Find the length of list
print(len(lst))

# 4. Get the first item, the middle item and the last item of the list
index_middle = ( len(lst) -1 )//2
middle_list = lst[index_middle]
index_last =  len(lst) -1 
last_list = lst[index_last]
print( 'Middle item:', middle_list )
print( 'Last item:', last_list )

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Dung', 21, 170, 'No', 'Ha Noi']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print('First:',it_companies[0])
print('Middle:',it_companies[(len(it_companies)-1)//2])
print('Last:',it_companies[(len(it_companies)-1)])

# Exercises : LEVEL 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print('Min age:', min_age)
print('Max age:', max_age)

# 2. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

# 3. find the median age( one middle item ỏ tưo middle items divides by two)
lenght_ages = len(ages)
if lenght_ages % 2 != 0:
    print('Median age:',ages[(lenght_ages-1) // 2])
else:
    sum_1 = (ages[lenght_ages//2] + ages[(lenght_ages//2) -1]) /2
    print('Median age:', sum_1)

# 4. Find the average age 
print('Average age:', "{:.2f}".format(sum(ages)/lenght_ages))

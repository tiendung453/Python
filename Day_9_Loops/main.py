# 3. Print triangle
for i in range(8):
    print('#'*i)
# 4. print retangle
for i in range(9):
    print('# '*8)
# 5. print the following pattern
for i in range(11):
    print(i, 'x' ,i,'=',i*i)
# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
lenght = len(lst)
for i in lst:
    print(i)
# 7. Use for loop to iterate from 0 to 100 print the sum of all numbers
tong = 0
for i in range(101):
    tong = tong + i 
print('The sum of the all numbers is: ', tong)
# 8. Use for loop to iterate from 0 - 100 and print the sum of all evens and the sum of all odds
sum_odd = 0
sum_even = 0
for i in range(101):
    if( i %2 == 0):
        sum_even += i
    else:
        sum_odd += i
print(sum_even, '\t', sum_odd)

# 9. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from data.countries import countries
# Lặp qua danh sách và trích xuất các quốc gia có chứa từ "land"
land_countries = [country for country in countries if 'land' in country]

# In kết quả
print(land_countries)

# 10. Đảo ngược list
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

# Sử dụng vòng lặp for để đảo ngược thứ tự của danh sách
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)

# 11. go to the data folder and use the countries_data.py 
from data.countries_data import countries_data
unique_languages = set()
total_languages = 0
for key in countries_data:
    if 'languages' in key:
        unique_languages.update(key['languages'])
print(len(unique_languages))

# 10 languages most used
languges_list = list()
number_languages = {}
for key in countries_data:
    if 'languages' in key:
        languges_list.extend(key['languages'])
for language in languges_list:
    if language in number_languages:
        number_languages[language] += 1
    else:
        number_languages[language] = 1
sorted_languages = sorted(number_languages.items(), key=lambda item: item[1], reverse=True)
print(sorted_languages[:10])

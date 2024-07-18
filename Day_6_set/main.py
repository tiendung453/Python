# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
print('Length of the set it_companies:',len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Viettel','Vina'])
print(it_companies)

# 4, Remove one of the conpanies from the set it_companies
it_companies.pop()
removed_item = it_companies.pop()
print(removed_item)

# 5. Convert the ages to a set and compare the length of the list and the set, which one is the biggest
age_to_set = set(age)
age_length = len(age)
a_length = len(A)
b_length = len(B)
print('The biggest length: ', max(age_length, a_length, b_length))

# 6. I am a teacher and I love to inspire and teach people.
#    How many unique words have been used in the sentence?
#    Use the split methods and set to get the unique words.
sentence = " I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print('Number: ', len(unique_words))
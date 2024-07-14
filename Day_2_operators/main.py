import math
# 1. Declare your age as integer variable
age = 25
# 2. Declare your height as a float variable
height = 1.7
# 3. Declare a variable that store a complex number
complex_number = 1 + 1j

#-------------============----------------------------------------------------
"""
4. Write a script that prompts the user to enter base and height of
the triangle and calculate an area of this triangle (area = 0.5 x b x h).
"""
base_of_triangle = float(input('Nhap chieu rong:'))
height_of_triangle = float(input('Nhap chieu cao tam giac:'))
area_of_triangle = 0.5*base_of_triangle*height_of_triangle
print('Dien tich cua tam giac la:', area_of_triangle)
#-------------============----------------------------------------------------

"""
5. Write a script that prompts the user to enter side a, side b, and side c of 
the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
"""
side_a = float(input('Nhap canh a:'))
side_b = float(input('Nhap canh b:'))
side_c = float(input('Nhap canh c:'))
C = side_a + side_b + side_c
print('Chu vi tam giac:', C)
#-------------============----------------------------------------------------'''

"""
6. Get length and width of a rectangle using prompt.
Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
"""
length = float(input('Nhap chieu dai hcn:'))
width  = float(input('Nhap chieu rong hcn: '))
S_hcn  = length * width
C_hcn  = 2*(length + width)
print('Dien tich hcn:', S_hcn)
print('Chu vi hcn:', C_hcn)
#-------------============----------------------------------------------------'''
"""
7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r)
and circumference (c = 2 x pi x r) where pi = 3.14.
"""
pi = 3.14
radius = float(input('Nhap ban kinh:'))
S_circle = pi * radius *radius
C_circle = 2 * pi * radius
print('Dien tich hinh tron:', S_circle)
print('Chu vi hinh tron:', C_circle)
#-------------============----------------------------------------------------'''
"""
8.Calculate the slope, 
x-intercept and y-intercept of y = 2x -2
"""
#tính slope
m_8 = 2
print('m_8 =', m_8)
#tính tọa độ giao điểm hoành y=0
y1 =0
x1 = (y1+2)/2
print('x1 =', x1)
# tính tọa độ giao điểm tung độ x =0
x2 = 0
y2 = 2 * x2 +2
print('y2 =', y2)

#-------------============----------------------------------------------------'''
"""
9.Slope is (m = y2-y1/x2-x1). Find the slope and 
Euclidean distance between point (2, 2) and point (6,10)
"""
x1 , y1, x2, y2 = 2, 2, 6, 10
# tính slope m
m_9 = (y2-y1)/(x2-x1)
print('m_9 =', m_9)
# tính khoảng cách 
E_distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print('E_distance =', "{:.2f}".format (E_distance))
#-------------============----------------------------------------------------'''
"""
10.Compare the slopes in tasks 8 and 9.
"""
if  m_8 < m_9:
    print('Slope 8 < slope 9')
elif m_8 > m_9:
    print('Slope 8 > slope 9')
else:
    print('Slope 8 = slope 9')
#________________________________________________#
"""
11. Calculate the value of y (y = x^2 + 6x + 9). 
Try to use different x values and figure out at what x value y is going to be 0.
"""
x = -6/2
print('x =', x)
#_________________________________________________#
# 12.Find the length of 'python' and 'dragon' and make a falsy comparison statement.
a = len('python')
b = len('dragon')
if a > b:
    print('Do dai python lon hon do dai dragon')
elif a < b:
    print('Do dai python nho hon do dai dragon')
else:
    print('Do dai python bang do dai dragon')
#________________________________________________#
# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'

string1 = 'python'
string2 = 'dragon'

if 'on' in string1 and 'on' in string2:
    print("'on' is found in both 'python' and 'dragon'")
else:
    print("'on' is not found in both 'python' and 'dragon'")
#_______________________________________________#
# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
string3 = 'I hope this course is not full of jargon'
if 'jargon' in string3:
    print('jargon in the sentence')
else:
    print('jargon not in the sentence')
#_______________________________________________#
# 16.Find the length of the text python and convert the value to float and convert it to string
lenght_float = float(a)
lenght_string = str(lenght_float)
#_______________________________________________#
# 17. Even numbers are divisible by 2 and the remainder is zero. 
#     How do you check if a number is even or not using python?
number = int(input('Nhap number: '))
if number % 2 == 0:
    print('Number is even')
else:
    print('Number is not even')
#_______________________________________________#
# 18.Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
if (7//3) == (int(2.7)):
    print('equal')
else:
    print('not equal')
#_______________________________________________#
# 21.Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('Nhap hour: '))
rate_per_hour = int(input('Nhap luong 1 gio: '))
week_earning = hours * rate_per_hour
print('weekly earning is:', week_earning)

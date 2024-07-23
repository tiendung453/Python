import math
# 1. Declare a funtion add_two_numbers. Its takes two parameters and it return a sum
def add_two_numbers(num1, num2):
    summ = num1 + num2
    return summ
print(add_two_numbers(1,2))

# 2.Write a function that calculates area_of_circle.
def area_circle(radius):
    area = 3.14 * radius * radius
    return area
print(area_circle(2))

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
check = True
sum_1 = 0
def add_all_nums(*nums):
    global check
    global sum_1
    for num in nums:
        if(isinstance(num,int) or isinstance(num,float)):
            sum_1 += num
        else:
            check = False
            break
    if(check):
        return sum_1
    else:
        return "This number is not a number type!"
print(add_all_nums(1,2.1,3,4))
print(add_all_nums(1,'a',3,4))

# 4. Convert C to F
def convert_celsius_to_fahrenheit(temp_c):
    F = 0
    F = (temp_c *9/5)+32
    return F
print(convert_celsius_to_fahrenheit(23))

# 5. slope of linear equation
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return "Đường thẳng thẳng đứng, không có độ dốc (vô hạn)"
    else:
        slope = (y2 - y1) / (x2 - x1)
        return slope

# Ví dụ sử dụng:
print(calculate_slope(1, 2, 3, 4))  # Output: 1.0
print(calculate_slope(1, 2, 1, 5))  # Output: Đường thẳng thẳng đứng, không có độ dốc (vô hạn)

# 6. Quadratic equation is caculated
def solve_quadratic_eqn(a, b, c):
    i = 1j
    set_of_solution = set()
    delta = b**2 - 4*a*c
    if(delta > 0):
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b - math.sqrt(delta))/2*a
        set_of_solution.update([x1,x2])
    elif(delta == 0):
        x1 = -b/2
        x2 = -b/2
        set_of_solution.update([x1,x2])
    else:
        x1 = (-b + math.sqrt(-delta)*i)/2*a
        x2 = (-b - math.sqrt(-delta)*i)/2*a
        set_of_solution.update([x1, x2])
    return set_of_solution
print(solve_quadratic_eqn(1,1,1))


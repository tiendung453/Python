#Day2: 30 days of python programming 
first_name = 'Tien'
last_name = 'Dung'
full_name = first_name +' '+ last_name
country = 'VietNam'
city = 'HaNoi'
age = 21
is_married = False
is_true = True
is_light_on = True

#khai bao nhieu bien tren 1 dong
first_name, last_name, full_name, country, city, age, is_married, is_true, is_light_on = 'Tien', 'Dung', 'Tien Dung', 'VietNam', 'HaNoi', 21, False, True, True

#in ra giá trị và kiểu dữ liệu của biến 
print(first_name, type(first_name))
print(last_name, type(last_name))
print(full_name, type(full_name))
print(country, type(country))
print(city, type(city))
print(age, type(age))
print(is_married, type(is_married))
print(is_true, type(is_true))
print(is_light_on, type(is_light_on))

# sử dụng hàm len() hiển thị chiều dài chuỗi
print(len(first_name))
print(type(zip([1,2],[3,4])))

# so sánh độ dài 2 chuỗi first_name và last_name
lenght_first_name = len(first_name)
lenght_last_name = len(last_name)

if lenght_first_name < lenght_last_name:
    print('Chuoi 1 co do dai ngan hoi chuoi 2')
elif lenght_last_name > lenght_last_name:
    print('Chuoi 1 co do dai lon hon chuoi 2')
else:
    print("2 chuoi co do dai bang nhau")

#declare num_one va num_two
num_one = 5
num_two = 4

# tính tổng 
total = num_one + num_two
print('total:',total)

# tính hiệu
diff = num_one - num_two
print('diff:',diff)

#tính nhân
product = num_one * num_two
print('product:', product)

#tính chia 
division = num_one / num_two
print('division:',division)

#tính dư
remainder = num_two % num_one
print('remainder:', remainder)

# tính lũy thừa 
exp = pow(num_one, num_two)
print('exp:',exp)

#tìm phép chia lấy nguyên 
floor_division = num_one // num_one
print('floor_division:', floor_division)

#the radius of a cỉcle ís 30m
pi = 3.14 #khai báo số pi
r = 30 #khai báo bán kính

#tính diện tích hình tròn 
S = pi*r*r
print("Area:", S)

#tính chu vi hình tròn
C = 2*pi*r
print("Circum:", C)

#nhập đầu vào của bán kinh r
r2 = input('Nhap r2:')

#chuyển đổi chuỗi từ bàn phím thành kiểu float
r2 = float(r2)

#tính diện tích hình tròn 
S2 = pi*r2*r2
print("Area:", S2)

#tính chu vi hình tròn
C2 = 2*pi*r2
print("Circum:", C2)








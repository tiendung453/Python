# 1.Nối chuỗi 'Thirty', 'Days', 'Of', 'Python' thành một chuỗi duy nhất, 'Thirty Days Of Python'.
chuoi_duy_nhat = 'Thirty' +' '+'Days'+' '+'Of'+' '+'Python'
print(chuoi_duy_nhat)

# 2. Nối chuỗi 'Coding', 'For', 'All' thành một chuỗi duy nhất, 'Coding For All'.
chuoi_duy_nhat_v2 = 'Coding'+' '+'For'+' '+'All'
print(chuoi_duy_nhat_v2)

# 3.Khai báo một biến có tên company và gán nó cho một giá trị ban đầu "Coding For All".
company = 'Coding For All'

# 4.In công ty biến bằng print().
print(company)

# 5.In độ dài của chuỗi công ty bằng phương thức len() và print().
print(len(company))

# 6. Thay đổi tất cả các ký tự thành chữ hoa bằng phương thức upper().
print(company.upper())

# 7. Thay đổi tất cả các ký tự thành chữ thường bằng phương thức lower().
print(company.lower())

# 8. Sử dụng các phương thức capitalize(), title(), swapcase() để định dạng giá trị của chuỗi Coding For All.
print(company.capitalize())

# 9. Cắt (cắt) từ đầu tiên của chuỗi Coding For All.
print(company.split()[0])

# 10.Kiểm tra xem chuỗi Coding For All có chứa một từ Coding bằng cách sử dụng
# phương thức index(), find() hoặc các phương thức khác hay không
company_coding = company.find('Coding') != -1
print(company_coding)

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
PfE = 'Python for Everyone'
print(PfE.replace(PfE, 'Python for All'))

# 13.Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
M_X_H = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(M_X_H.split(','))

# 15. What is the character at index 0 in the string Coding For All.
print(company[0])

# 16. What is the last index of the string Coding For All.
print(company[len(company)-1])

# 17. What character is at index 10 in "Coding For All" string.
print(company[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
import random

def generate_hexa_color():
    # Tạo ra một màu hexadecimal
    hex_chars = '0123456789abcdef'
    color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
    return color

def list_of_hexa_colors(n):
    # Tạo ra danh sách các màu hexadecimal
    print([generate_hexa_color() for _ in range(n)])

# Ví dụ sử dụng
#print(list_of_hexa_colors(5))

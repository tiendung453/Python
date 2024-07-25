countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Sử dụng list comprehension để tạo danh sách mới theo định dạng yêu cầu
flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for country, capital in sublist]

print(flattened_countries)

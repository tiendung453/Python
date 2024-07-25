countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_to_dict = [{'country':country.upper(),'city':capital.upper()} for sublist in countries for country, capital in sublist]
print(list_to_dict)
from data.countries_data import countries_data
# sort by name of country
def sort_countries_by_name(lst):
    countries_name_list = []
    for country in countries_data:
        if 'name' in country:
            countries_name_list.append(country['name'])
    countries_name_list = sorted(countries_name_list)
    return countries_name_list
print(sort_countries_by_name(countries_data))

# sort by name of capital

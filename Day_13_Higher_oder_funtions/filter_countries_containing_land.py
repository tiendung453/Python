countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def filter_out_countries_contain_land(country):
    if 'land' in country:
        return True
    else:
        return False
countries_containing_land = filter(filter_out_countries_contain_land, countries)
print(list(countries_containing_land))
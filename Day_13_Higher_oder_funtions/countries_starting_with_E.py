countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def check_country_starts_with_E(country):
    if country.startswith('E'):
        return True
    else:
        return False
countries_starting_with_E = filter(check_country_starts_with_E,countries)
print(list(countries_starting_with_E))
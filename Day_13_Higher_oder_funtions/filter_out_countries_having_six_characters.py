countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def filter_out_countries_having_six_characters(country):
    if len(country) == 6:
        return True
    else:
        return False
six_characters_in_coutry = filter(filter_out_countries_having_six_characters, countries)
print(list(six_characters_in_coutry))
from data.countries import countries
def categorize_countries(countries_list,pattern_list):
    categorized_countries = {pattern: [] for pattern in pattern_list}
    for country in countries_list:
        for pattern in pattern_list:
            if pattern in country:
                categorized_countries[pattern].append(country)
    return categorized_countries

patterns_list = ['land', 'ia', 'island', 'stan']
categorized_countries = categorize_countries(countries,patterns_list)
for pattern, country_list in categorized_countries.items():
    print(f"Countries containing '{pattern}': {country_list}")


from data.countries_data import countries_data
def most_populated_countries():
    countries_population_dict = {}
    for country in countries_data:
        if 'name'in country and 'population'in country:
            countries_population_dict[country['name']] = country['population']
    
    sorted_population = sorted(countries_population_dict.items(), key=lambda item: item[1], reverse=True)
    print(sorted_population[:10])
most_populated_countries()

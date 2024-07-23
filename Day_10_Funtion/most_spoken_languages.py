from data.countries_data import countries_data
def most_spoken_languages():
    languges_list = list()
    number_languages = {}
    for key in countries_data:
        if 'languages' in key:
            languges_list.extend(key['languages'])
    for language in languges_list:
        if language in number_languages:
            number_languages[language] += 1
        else:
            number_languages[language] = 1
    sorted_languages = sorted(number_languages.items(), key=lambda item: item[1], reverse=True)
    print(sorted_languages[:10])
most_spoken_languages()

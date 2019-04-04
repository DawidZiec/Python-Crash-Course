import json

from country_codes import get_country_code

# Wczytanie danych i umiesczenie ich na liście.

filename = 'Data Mining/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Wyświetlenie populacji poszczególnych państw w 2010 roku.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ": " + str(population))
        else:
            print('BŁĄD - ' + country_name)

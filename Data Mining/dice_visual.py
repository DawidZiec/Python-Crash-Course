import pygal

from die import Die

# Utworzenie dwóch kości typu D6.
die_1 = Die()
die_2 = Die()

# Wykonanie pewnej liczby rzutuów i umieszczenie danych na liście.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analiza wyników.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Wizualizacja wyników.
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wynik rzucania dwiema kośćmi D6 tysiąc razy"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 12]
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('2x D6', frequencies)
hist.render_to_file('dice_visual.svg')

import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Pobranie najwyższych temperatur z pliku, a także dat ich wystąpienia.
filename = 'Data Mining/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

    print(highs)

# Dane wykresu.
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, highs, c='red')

# Formatowanie wykresu.
plt.title("Najwyższa temperatura dnia, lipiec 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

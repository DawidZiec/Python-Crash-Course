import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Pobranie najniższych i najwyższych temperatur z pliku, a także dat ich wystąpienia.
filename = 'Data Mining/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'Brak danych.')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Dane wykresu.
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formatowanie wykresu.
plt.title("Najwyższa i najniższa temperatura dnia - 2014\nDolina Śmierci, Kalifornia", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

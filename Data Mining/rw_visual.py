from random import choice

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Mapy kolorów do losowego wybrania przy każdym rysowaniu.
color_palette = [plt.cm.seismic, plt.cm.inferno, plt.cm.summer, plt.cm.plasma]

# Tworzenie nowego błądzenia losowego, dopóki program pozostaje aktywny.
while True:
    # Przygotowanie danych błądzenia losowego i wyświetlenie punktów.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Określenie wielkości okna wykresu.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,
                c=point_numbers, cmap=choice(color_palette), edgecolor='none', s=1)

    # Podkreślenie pierwszego i ostatniego punktu błądzenia losowego.
    plt.scatter(0, 0, c='red', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='blue', edgecolor='none', s=100)

    # Ukrycie osi.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Utworzyć kolejne błądzenia losowe? (t/n): ")
    if keep_running == 'n':
        break

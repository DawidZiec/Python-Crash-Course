class Settings():
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja danych statystycznych gry."""
        # Ustawienia ekranu.
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (54, 5, 132)

        # Ustawienia dotyczące statku.
        self.ship_limit = 3

        # Ustawienia dotyczące pocisku.
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (249, 126, 2)
        self.bullets_allowed = 3

        # Ustawienia dotyczące obcego.
        self.fleet_drop_speed = 10

        # Łatwa zmiana szybkośi gry.
        self.speedup_scale = 1.4

        # łatwa zmiana liczby punktów przyznawanych za zestrzelenie obcego.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawień, które ulegają zmianie w trakcie gry."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = .2

        # Wartość fleet_direction wynosząca 1 oznacza ruch w prawi, natomiast -1 w lewo.
        self.fleet_direction = 1

        # Punktacja.
        self.alien_points = 50

    def increase_speed(self):
        """Zmiana ustawie” dotyczących szybkości gry oraz przyznawanych punktów."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

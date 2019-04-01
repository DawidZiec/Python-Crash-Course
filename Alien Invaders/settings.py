class Settings():
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustawiń gry."""
        # Ustawienia ekranu.
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (54, 5, 132)

        # Ustawienia dotyczące statku.
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Ustawiania dotyczące pocisku.
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (249, 126, 2)
        self.bullets_allowed = 3

        # Ustawienia dotyczące obcego.
        self.alien_speed_factor = .2
        self.fleet_drop_speed = 10
        # Wartość fleet_direction wynosząca 1 oznacza ruch w prawi, natomiast -1 w lewo.
        self.fleet_direction = 1

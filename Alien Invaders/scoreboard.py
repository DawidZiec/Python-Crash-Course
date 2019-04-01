import pygame.font
from pygame.sprite import Group

from ship import LittleShip


class Scoreboard():
    """Klasa przeznaczona do przedstawiania informacji o punktacji."""

    def __init__(self, ai_settings, screen, stats):
        """Inicjalizacja atrybutów dotyczących punktacji."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Ustawienia czcionki dla informacji dotyczących punktacji.
        self.text_color = (80, 80, 80)
        self.font = pygame.font.SysFont(None, 48)

        # Przygotowanie początkowych obrazów z punktacją.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.ai_settings.bg_color)

        # Wyświetlenie punktacji w prawym górnym roku ekranu.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 5

    def prep_high_score(self):
        """Konwersja najlepszego wyniku w grze na wygenerowany obraz."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Wyświetlenie punktacji w prawym górnym roku ekranu.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.centerx
        self.high_score_rect.top = 5

    def prep_level(self):
        """Konwersja numeru poziomu na wygenerowany obraz."""
        self.level_image = self.font.render(
            str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        # Numer poziomu jest wyświetlany pod aktualną punktacją.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 5

    def prep_ships(self):
        """Wyświetla liczbę statków, jakie pozostały graczowi."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = LittleShip(self.ai_settings, self.screen)
            ship.rect.x = 5 + ship_number * ship.rect.width
            ship.rect.y = 3
            self.ships.add(ship)

    def show_score(self):
        """Wyświetlenie na ekranie punktacji oraz statków."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # Wyświetlenie statków.
        self.ships.draw(self.screen)

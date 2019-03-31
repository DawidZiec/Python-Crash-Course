import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf

def run_game():
    # Inicjalizacja gry, ustawień i utworzenie obiektu ekranu.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Utworzenie egzemplarza przeznaczonego do przechowywania danych statystycznych dotyczących gry.
    stats = GameStats(ai_settings)

    # Utworzenie statku kosmicznego.
    ship = Ship(ai_settings, screen)

    # Utworzenie gupy przeznaczonej do przechowywania pocisku oraz floty obcych.
    bullets = Group()
    aliens = Group()

    # Utworzenie floty obcych.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Zdefiniowanie koloru tła.
    bg_color = (ai_settings.bg_color)

    # Rozpoczęcie pętli głównej gry.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
                gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
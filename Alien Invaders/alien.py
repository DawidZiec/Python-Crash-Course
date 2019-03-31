import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przedstawiająca pojedynczego obcego we flocie."""
    def __init__(self, ai_settings, screen):
        """Inicjalizacja obcego i zdefiniowanie jego położenia początkowego."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Wczytanie obrazu obcego i zdefiniowanie jego atrybutu rect.
        self.image = pygame.image.load("Source/images/thug.png")
        self.rect = self.image.get_rect()

        # Umieszczenie nowego obcego w poliżu lewego górnego rogu ekranu.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Przechowanie dokładnego położenia obcego.
        self.x = float(self.rect.x)

    def blitme(self):
        """Wyświetlenie obcego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Zwraca wartość True, jeśli obcy zajduje się przy krawędzi ekranu."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True

    def update(self):
        """Przesunięcie obcego w prawo."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
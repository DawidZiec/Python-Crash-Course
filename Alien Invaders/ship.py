import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """Inicjalizacja statku kosmicznego i jego położenie początkowe."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Wczytanie obrazu statku kosmicznego i wczytanie jego prostokąta.
        self.image = pygame.image.load('Alien Invaders/images/Ship_0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Każdy nowy statek kosmiczny pojaweia się na dole ekranu.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Punkt środkowy statku jest przechowywany w postaci liczby zmiennoprzecinkowej.
        self.center = float(self.rect.centerx)

        # Opcje wskazująca na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Uaktualnienie położenia statku na podstawie opcji wskazującej na jego ruch."""
        # Uaktualnienie wartości punktu środkowego statku, a nie jego prostokąta.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        # Uaktualnienie obiektu rect na podstawie wartosci self.center.
        self.rect.centerx = self.center  # 5.

    def blitme(self):
        """Wyświetlanie statku kosmicznego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Umieszczenie statku na środku przy dolnej krawędzi ekranu."""
        self.center = self.screen_rect.centerx

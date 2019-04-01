import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg):
        """Inicjalizacja atrybutów przycisku."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Zdefiniowanie wymiarów i właściwości przycisku.
        self.width, self.height = 200, 50
        self.button_color = (100, 200, 100)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Utworzenie prostokąta prxycisku i wyśrodkowanie go.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Komunikat wyświetlany przez przycisk trzeba przygotować jednkrotnie.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """
        Umieszczenie komunikatu w wygenerowanym obrazie i wyśrodkowanie
        tekstu na przysciku
        """
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Wyświetlenie pustego przysicku, a następnie komunikat na nim.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

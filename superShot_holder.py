import pygame
from pygame.color import THECOLORS
from screen import Screen

pygame.init()


class SuperShot_holder:

    def __init__(self):
        self.shot = 0
        self.is_superShot = False
        self.colors = [(221, 160, 221), (255, 0, 255), (139, 0, 139), (75, 0, 130)]

    def add_chance(self):
        self.shot += 24

    def check_100_p(self):
        return self.shot >= 100

    def get_text(self):
        color = self.colors[(self.shot - 1) // 25]
        text = pygame.font.SysFont('couriernew', 50).render(str(self.shot) + "%", True, color)
        return text

    def update(self, screen):
        if self.check_100_p():
            self.shot = 100
        if self.check_100_p():
            self.is_superShot = True
            self.shot = 100
            text_press = pygame.font.SysFont('couriernew', 40).render("PRESS SPACE", True, THECOLORS["red"])
            screen.blit(text_press, (Screen.WIDTH // 2 - 130, 50))

        screen.blit(self.get_text(), (Screen.WIDTH // 2 - 50, 10))

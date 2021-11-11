import pygame
from pygame.color import THECOLORS
from screen import Screen

pygame.init()


class SuperShot_holder:
    shot = 0
    is_superShot = False
    colors = [(221, 160, 221), (255, 0, 255), (139, 0, 139), (75, 0, 130)]

    @classmethod
    def add_chance(cls):
        cls.shot += 24

    @classmethod
    def set_100_p(cls):
        if cls.shot >= 100:
            return True
        return False

    @classmethod
    def get_text(cls):
        color = cls.colors[(cls.shot - 1) // 25]
        text = pygame.font.SysFont('couriernew', 50).render(str(cls.shot) + "%", True, color)
        return text

    @classmethod
    def update(cls, screen):
        if cls.set_100_p():
            cls.shot = 100
        if cls.set_100_p():
            cls.is_superShot = True
            cls.shot = 100
            text_press = pygame.font.SysFont('couriernew', 40).render("PRESS SPACE", True, THECOLORS["red"])
            screen.blit(text_press, (Screen.WIDTH // 2 - 130, 50))

        screen.blit(cls.get_text(), (Screen.WIDTH // 2 - 50, 10))
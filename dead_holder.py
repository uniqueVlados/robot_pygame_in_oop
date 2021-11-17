import pygame
from pygame.color import THECOLORS
from screen import Screen


class DeadHolder:
    def __init__(self, robot):
        self.font = pygame.font.SysFont('couriernew', 50)
        self.robot_link = robot

    @property
    def robot(self):
        return self.robot_link

    def update(self, screen):
        text = self.font.render(str(self.robot_link.get_hit()), True, THECOLORS["white"])
        screen.blit(text, ( Screen.WIDTH - 60, 10))

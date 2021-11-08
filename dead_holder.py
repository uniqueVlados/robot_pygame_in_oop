import pygame
from pygame.color import THECOLORS


class DeadHolder:
    def __init__(self, robot):
        self.font = pygame.font.SysFont('couriernew', 50)
        self.robot_link = robot

    @property
    def robot(self):
        return self.robot_link

    def update(self, screen):
        text = self.font.render(str(self.robot_link.get_hit()), True, THECOLORS["white"])
        WIDTH, HEIGHT = screen.get_size()
        screen.blit(text, (WIDTH - 60, 10))
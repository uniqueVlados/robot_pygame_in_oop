import pygame
from pygame.color import THECOLORS


class HealthHolder:
    def __init__(self, robot):
        self.font = pygame.font.SysFont('couriernew', 60)
        self.robot_link = robot

    @property
    def robot(self):
        return self.robot_link

    def update(self, screen):
        if self.robot_link.get_health() > 85:
            text = self.font.render(str(self.robot_link.get_health()), True, THECOLORS["green"])
        elif 60 < self.robot_link.get_health() <= 85:
            text = self.font.render(str(self.robot_link.get_health()), True, THECOLORS["yellow"])
        elif 25 <= self.robot_link.get_health() <= 60:
            text = self.font.render(str(self.robot_link.get_health()), True, THECOLORS["orange"])
        elif 0 <= self.robot_link.get_health() < 25:
            text = self.font.render(str(self.robot_link.get_health()), True, THECOLORS["red"])
        screen.blit(text, (10, 10))


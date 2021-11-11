import pygame
from pygame.color import THECOLORS


class HealthHolder:
    def __init__(self, robot):
        self.font = pygame.font.SysFont('couriernew', 50)
        self.robot_link = robot

    @property
    def robot(self):
        return self.robot_link

    def update(self, screen):
        color = ["red", "orange", "yellow", "green"]
        text = self.font.render(str(self.robot_link.get_health()), True, THECOLORS[color[(self.robot_link.get_health()
                                                                                          - 1) // 25]])
        screen.blit(text, (10, 10))
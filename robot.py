from screen import Screen
from superShot_holder import SuperShot_holder
import pygame

class Robot:
    SIZE = 72
    IS_DEAD = False

    def __init__(self, pos, robot_img, count_robotAttack, health=100):
        self.pos_x, self.pos_y = pos[0], pos[1]
        self.health = health
        self.image = robot_img
        self.hit = 0
        self.count_robotAttack = count_robotAttack
        Robot.SIZE = self.image.get_size()[0]

    def __repr__(self):
        return f"({self.pos_x}, {self.pos_y})"

    @property
    def pos(self):
        return self.pos_x, self.pos_y

    def update(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))

    def get_health(self):
        return self.health

    def get_hit(self):
        return self.hit

    def move_a(self):
        if self.pos_x > 0:
            self.pos_x -= Robot.SIZE

    def move_w(self):
        if self.pos_y > 0:
            self.pos_y -= Robot.SIZE

    def move_d(self):
        if self.pos_x < Screen.WIDTH - Robot.SIZE:
            self.pos_x += Robot.SIZE

    def move_s(self):
        if self.pos_y < Screen.HEIGHT - Robot.SIZE:
            self.pos_y += Robot.SIZE

    def move(self, key):
        directions = {"a": self.move_a,
                      "w": self.move_w,
                      "s": self.move_s,
                      "d": self.move_d}

        if self.health > 0:
            if move_in_direction := directions.get(key):
                move_in_direction()


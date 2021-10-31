from random import randint

from robot import Robot

SPEED = 40


class Shot:
    def __init__(self, robot, image):
        self.pos_x, self.pos_y = robot.pos[0] + 30, robot.pos[1] + 30
        self.actions = [self.move_w, self.move_d, self.move_s, self.move_a]
        self.image = image
        self.is_active = False
        self.counter = 0
        self.speed = 10
        self.side = None

    def do_active(self):
        self.is_active = True

    def get_active(self):
        return self.is_active

    def set_side(self, side):
        self.side = side

    def set_start_pos(self, robot):
        self.pos_x, self.pos_y = robot.pos[0] + 30, robot.pos[1] + 30

    def move_a(self, speed):
        self.pos_x -= speed

    def move_w(self, speed):
        self.pos_y -= speed

    def move_d(self, speed):
        self.pos_x += speed

    def move_s(self, speed):
        self.pos_y += speed

    def update(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))








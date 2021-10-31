import pygame


class Shot:
    SPEED = 10

    def __init__(self, robot, image, side, screen):
        self.pos_x, self.pos_y = robot.pos[0] + 30, robot.pos[1] + 30
        self.image = image
        self.is_active = True
        self.counter = 0
        self.side = side
        self.screen = screen

    def __repr__(self):
        return f"({self.pos_x}, {self.pos_y})"

    def set_start_pos(self, robot):
        self.pos_x, self.pos_y = robot.pos[0] + 30, robot.pos[1] + 30

    @property
    def screen_width(self):
        width, height = self.screen.get_size()
        return width

    @property
    def screen_height(self):
        width, height = self.screen.get_size()
        return height

    def _move_a(self):
        if self.pos_x > 0:
            self.pos_x -= Shot.SPEED
        else:
            self.is_active = False

    def _move_w(self):
        if self.pos_y > 0:
            self.pos_y -= Shot.SPEED
        else:
            self.is_active = False

    def _move_d(self):
        if self.pos_x < self.screen_width - self.image.get_size()[0]:
            self.pos_x += Shot.SPEED
        else:
            self.is_active = False

    def _move_s(self):
        if self.pos_y < self.screen_height -  self.image.get_size()[1]:
            self.pos_y += Shot.SPEED
        else:
            self.is_active = False

    def move(self, key):
        directions = {pygame.K_LEFT: self._move_a,
                      pygame.K_UP: self._move_w,
                      pygame.K_DOWN: self._move_s,
                      pygame.K_RIGHT: self._move_d}

        if move_in_direction := directions.get(key):
            move_in_direction()

    def update(self):
        self.move(self.side)
        self.screen.blit(self.image, (self.pos_x, self.pos_y))

    # def control_shot(self, screen):
    #     self.counter += 1
    #     if self.counter == self.speed:
    #         if self.side == "a":
    #             self.move_a(50)
    #         elif self.side == "w":
    #             self.move_w(50)
    #         elif self.side == "s":
    #             self.move_s(50)
    #         elif self.side == "d":
    #             self.move_d(50)
    #         self.counter = 0
    #     if self.get_active():
    #         self.update(screen)








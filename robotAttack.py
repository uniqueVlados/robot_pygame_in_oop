from random import randint, choice
import pygame
from robot import Robot
from screen import Screen

pygame.init()
# ------MUSIC---------------------
shot_to_robotAttack_mus = pygame.mixer.Sound("music/shot_to_robotAttack_mus.mp3")
robot_to_robotAttack_mus = pygame.mixer.Sound("music/robot_to_robotAttack.mp3")
# --------------------------------

class RobotAttack(Robot):
    SPEED_START = 50
    SPEED_END = 100
    COUNT_ROBOT = 0

    def __init__(self, pos, image, screen, health=100):
        super().__init__(pos, image, health)
        self.speed = randint(RobotAttack.SPEED_START, RobotAttack.SPEED_END)
        self.counter = 0
        count_robot = None

    def check_pos(self):
        if self.pos_y > Screen.HEIGHT:
            self.pos_y = 0
        if self.pos_x > Screen.WIDTH:
            self.pos_x = 0
        if self.pos_y < 0:
            self.pos_y = Screen.HEIGHT
        if self.pos_x < 0:
            self.pos_x = Screen.WIDTH

    def move(self):
        neg_pos = choice([1, -1])
        if neg_pos == 1:
            if neg_pos == 1:
                self.pos_x += Robot.SIZE
            else:
                self.pos_x -= Robot.SIZE
        else:
            if neg_pos == 1:
                self.pos_y += Robot.SIZE
            else:
                self.pos_y -= Robot.SIZE
        self.check_pos()


    @staticmethod
    def diff_move(robotAttack_list, screen):
        for r in robotAttack_list:
            r.update(screen)
            r.counter += 1
            if r.counter == r.speed:
                r.move()
                r.counter = 0

    @staticmethod
    def _count_coord(length):
        return Robot.SIZE * randint(1, length // Robot.SIZE)


    @staticmethod
    def create_robotAttack(robotAttack_list, image, screen, robot):
        for i in range(robot.count_robotAttack):
            robotAttack = RobotAttack((RobotAttack._count_coord(Screen.WIDTH),
                                       RobotAttack._count_coord(Screen.HEIGHT)), image, screen)
            robotAttack_list.append(robotAttack)

    @staticmethod
    def delete_robotAttack(robotAttack_list):
        robotAttack_list.clear()

    def get_col(self, ra, obj):
        return ra.pos_x <= obj.pos_x <= ra.pos_x + ra.image.get_size()[0] and ra.pos_y <= \
                obj.pos_y <= ra.pos_y + ra.image.get_size()[1]

    def collision_robot(self, robotAttack_list, ra, robot):
        if self.get_col(ra, robot):
            robotAttack_list.remove(ra)
            robot_to_robotAttack_mus.play()
            robot.health -= 30
            if robot.health < 0:
                robot.health = 0
            # shot.is_active = False

    def collision_shot(self, robotAttack_list, ra, superShot_holder, shoots, robot):
        for shot in shoots[::-1]:
            if self.get_col(ra, shot):
                shot_to_robotAttack_mus.play()
                if shot.is_active:
                    shoots.remove(shot)
                    robotAttack_list.remove(ra)
                    robot.hit += 1
                    superShot_holder.add_chance()

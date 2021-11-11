from random import randint, choice
from robot import Robot
from screen import Screen

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
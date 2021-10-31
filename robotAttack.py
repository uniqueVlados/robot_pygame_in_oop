from random import randint, choice
from robot import Robot

SPEED_START = 50
SPEED_END = 100
COUNT_ROBOT = 0


class RobotAttack(Robot):

    def __init__(self, pos, image, health=100):
        super().__init__(pos, image, health)
        self.speed = randint(SPEED_START, SPEED_END)
        self.counter = 0
        count_robot = None

    def check_pos(self, WIDTH, HEIGHT):
        if self.pos_y > HEIGHT:
            self.pos_y = 0
        if self.pos_x > WIDTH:
            self.pos_x = 0
        if self.pos_y < 0:
            self.pos_y = HEIGHT
        if self.pos_x < 0:
            self.pos_x = WIDTH

    def move(self, SIZE, WIDTH, HEIGHT):
        neg_pos = choice([1, -1])
        if neg_pos == 1:
            if neg_pos == 1:
                self.pos_x += SIZE
            else:
                self.pos_x -= SIZE
        else:
            if neg_pos == 1:
                self.pos_y += SIZE
            else:
                self.pos_y -= SIZE
        self.check_pos(WIDTH, HEIGHT)

    @staticmethod
    def create_robotAttack(robotAttack_list, image, screen, robot):
        WIDTH, HEIGHT = screen.get_size()
        for i in range(robot.count_robotAttack):
            robotAttack = RobotAttack((Robot.SIZE * randint(1, WIDTH // Robot.SIZE) - Robot.SIZE, Robot.SIZE *
                                       randint(1, HEIGHT // Robot.SIZE) - Robot.SIZE), image)
            robotAttack_list.append(robotAttack)

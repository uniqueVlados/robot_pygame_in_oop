import pygame
import sys
from pygame.color import THECOLORS
from dead_holder import DeadHolder
from robot import Robot
from robotAttack import RobotAttack
from health_holder import HealthHolder
from shot import Shot

# ------IMAGE---------------------
robot_img = pygame.image.load("img/robot.png")
robotAttack_img = pygame.image.load("img/robotAttack.png")
shot_img = pygame.image.load("img/shot.png")
shot_img = pygame.transform.scale(shot_img, (40, 40))
# --------------------------------


# ------CONST---------------------
WIDTH = 1200
HEIGHT = 800
SIZE = 80
# --------------------------------

# ------VAR-----------------------
robotAttack_list = []
# --------------------------------

count_robotAttack = int(input("Сколько врагов создать? "))


# ------PYGAME--------------------
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ROBOTS")
pygame.display.set_icon(robotAttack_img)
# --------------------------------

# ------CREATE OBJECTS-----------------------
robot = Robot((WIDTH // 2 - SIZE // 2, HEIGHT // 2 - SIZE // 2), robot_img, count_robotAttack)
RobotAttack.create_robotAttack(robotAttack_list, robotAttack_img, screen, robot)
health_holder = HealthHolder(robot)
dead_holder = DeadHolder(robot)
shot = Shot(robot, shot_img)
# -------------------------------------------


screen.blit(robot_img, (WIDTH // 2 - SIZE // 2, HEIGHT // 2 - SIZE // 2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                robot.move("a", SIZE)
            elif event.key == pygame.K_w:
                robot.move("w", SIZE)
            elif event.key == pygame.K_d:
                robot.move("d", SIZE)
            elif event.key == pygame.K_s:
                robot.move("s", SIZE)
            elif event.key == pygame.K_RIGHT:
                shot.do_active()
                shot.set_side("d")
                shot.set_start_pos(robot)
            elif event.key == pygame.K_LEFT:
                shot.do_active()
                shot.set_side("a")
                shot.set_start_pos(robot)
            elif event.key == pygame.K_UP:
                shot.do_active()
                shot.set_side("w")
                shot.set_start_pos(robot)
            elif event.key == pygame.K_DOWN:
                shot.do_active()
                shot.set_side("s")
                shot.set_start_pos(robot)
    screen.fill((0, 0, 0))

    robot.update(screen)
    health_holder.update(screen)
    dead_holder.update(screen)

    shot.counter += 1
    if shot.counter == shot.speed:
        if shot.side == "a":
            shot.move_a(50)
        elif shot.side == "w":
            shot.move_w(50)
        elif shot.side == "s":
            shot.move_s(50)
        elif shot.side == "d":
            shot.move_d(50)
        shot.counter = 0
    if shot.get_active():
        shot.update(screen)

    for r in robotAttack_list:
        r.update(screen)
        r.counter += 1
        if r.counter == r.speed:
            r.move(SIZE, WIDTH, HEIGHT)
            r.counter = 0

    # ---------DELETE ROBOTATTACK IF COLLISION SHOT------
    for ra in robotAttack_list:
        if ra.pos_x - 40 <= shot.pos_x <= ra.pos_x + 40 and ra.pos_y - 40 <= shot.pos_y <= ra.pos_y + 70:
            robotAttack_list.remove(ra)
            robot.hit += 1
        if ra.pos_x - 40 <= robot.pos_x <= ra.pos_x + 40 and ra.pos_y - 40 <= robot.pos_y <= ra.pos_y + 70:
            robotAttack_list.remove(ra)
            robot.health -= 100 // robot.count_robotAttack
    # ---------------------------------------------------

    # ---------FINAL GAME--------------------------------
    if robot.get_health() <= 0:
        font = pygame.font.SysFont('couriernew', 100)
        text = font.render(str('YOU DEAD'), True, THECOLORS['red'])
        screen.blit(text, (WIDTH // 2 - 250, 100))

    elif len(robotAttack_list) == 0 and robot.get_health() > 0:
        font = pygame.font.SysFont('couriernew', 100)
        text = font.render(str('YOU WIN'), True, THECOLORS['green'])
        screen.blit(text, (WIDTH // 2 - 250, 100))


    # ---------------------------------------------------
    clock.tick(60)
    pygame.display.update()

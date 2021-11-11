import pygame
import sys
from pygame.color import THECOLORS
from dead_holder import DeadHolder
from robot import Robot
from robotAttack import RobotAttack
from health_holder import HealthHolder
from shot import Shot
from screen import Screen
from superShot_holder import SuperShot_holder

# -----------FUNCTION------------------------
def check_final(robot, robotAttack_list):
    if robot.get_health() <= 0:
        Robot.IS_DEAD = True
        Screen.is_final_scene = True
        screen.blit(lose_img, (0, 0))
        font = pygame.font.SysFont('couriernew', 100)
        text = font.render(str('YOU DEAD'), True, THECOLORS['red'])
        screen.blit(text, (Screen.WIDTH // 2 - 250, 100))
    elif len(robotAttack_list) == 0 and robot.get_health() > 0:
        Screen.is_final_scene = True
        screen.blit(win_img, (0, 0))
        font = pygame.font.SysFont('couriernew', 100)
        text = font.render(str('YOU WIN'), True, THECOLORS['green'])
        screen.blit(text, (Screen.WIDTH // 2 - 200, 100))


# ------IMAGE---------------------
robot_img = pygame.image.load("img/robot.png")
robotAttack_img = pygame.image.load("img/robotAttack.png")
shot_img = pygame.image.load("img/shot.png")
back_img = pygame.image.load("img/back.jpeg")
win_img = pygame.image.load("img/win.jpeg")
lose_img = pygame.image.load("img/lose.jpg")
# --------------------------------

# ------VAR-----------------------
robotAttack_list = []
# --------------------------------

with open("readme.md", "r", encoding="utf-8") as info:
    info_text = info.read().replace("\n\n", "\n")
    print(info_text)

count_robotAttack = int(input("\nСКОЛЬКО РОБОТОВ СОЗДАТЬ? "))

# ------PYGAME--------------------
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
pygame.display.set_caption("ROBOTS")
pygame.display.set_icon(robotAttack_img)
# --------------------------------

# ------CREATE OBJECTS-----------------------
robot = Robot((0, 0), robot_img, count_robotAttack)
RobotAttack.create_robotAttack(robotAttack_list, robotAttack_img, screen, robot)
health_holder = HealthHolder(robot)
dead_holder = DeadHolder(robot)
shoots = []
# -------------------------------------------


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s]:
                robot.move(chr(event.key))

            elif event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN] and len(shoots) == 0:
                shoots.append(Shot(robot, shot_img, event.key, screen))

            elif event.key == pygame.K_SPACE and len(shoots) == 0 and SuperShot_holder.is_superShot:
                SuperShot_holder.is_superShot = False
                SuperShot_holder.shot = 0
                for k in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
                    shoots.append(Shot(robot, shot_img, k, screen))

    if not Screen.is_final_scene:
        screen.blit(back_img, (0, 0))

    robot.update(screen)
    health_holder.update(screen)
    dead_holder.update(screen)
    SuperShot_holder.update(screen)

    for shot in shoots[::-1]:
        if not shot.is_active:
            shoots.remove(shot)
        else:
            shot.update()
            robot.robotAttack_collision(robotAttack_list, robot, shot)
    robot.robotAttack_collision(robotAttack_list, robot)

    check_final(robot, robotAttack_list)
    if Robot.IS_DEAD:
        RobotAttack.delete_robotAttack(robotAttack_list)
    RobotAttack.diff_move(robotAttack_list, screen)
    clock.tick(60)
    pygame.display.update()

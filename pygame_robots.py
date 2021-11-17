import pygame
import sys
from random import randint
from pygame.color import THECOLORS
from dead_holder import DeadHolder
from robot import Robot
from robotAttack import RobotAttack
from health_holder import HealthHolder
from shot import Shot
from screen import Screen
from superShot_holder import SuperShot_holder


# ------FUNCTION------------------
def check_final(robot, robotAttack_list, screen_obj):
    if robot.get_health() <= 0:
        back_mus.stop()
        dead_mus.play()
        RobotAttack.delete_robotAttack(robotAttack_list)
        screen_obj.is_final_scene = True
        screen.blit(lose_img, (0, 0))
        screen.blit(text_dead, (Screen.WIDTH // 2 - 200, 100))
    elif len(robotAttack_list) == 0:
        back_mus.stop()
        win_mus.play()
        RobotAttack.delete_robotAttack(robotAttack_list)
        screen_obj.is_final_scene = True
        screen.blit(win_img, (0, 0))
        screen.blit(text_win, (Screen.WIDTH // 2 - 200, 100))


def close_app(e):
    if e.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def control_robot_move(e):
    if e.key in [pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s]:
        robot.move(chr(e.key))


def control_shot(e):
    if e.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN] and len(shoots) == 0:
        shoots.append(Shot(robot, shot_img, event.key, screen))
        print(*shoots)
        shot_mus.play()


def control_super_shot(e):
    if e.key == pygame.K_SPACE and len(shoots) == 0 and superShot_holder.is_superShot:
        superShot_mus.play()
        superShot_holder.is_superShot = False
        superShot_holder.shot = 0
        for k in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
            shoots.append(Shot(robot, shot_img, k, screen))


def create_new_robotsAttack_by_time(speed, screen_obj):
    global counter_for_create_robot
    counter_for_create_robot += 1
    if counter_for_create_robot == speed and not screen_obj.is_final_scene:
        robot.count_robotAttack = randint(2, 3)
        RobotAttack.create_robotAttack(robotAttack_list, robotAttack_img, screen, robot)
        counter_for_create_robot = 0


def robotAttack_collision(robotAttack_list):
    for ra in robotAttack_list[::-1]:
        ra.collision_robot(robotAttack_list, ra, robot)
        ra.collision_shot(robotAttack_list, ra, superShot_holder, shoots, robot)


def shots_behavior(shoots):
    for sh in shoots[::-1]:
        if sh.is_active:
            sh.update(screen)
        else:
            shoots.remove(sh)
# --------------------------------


# -----CONSOLE INFO---------------
with open("readme.md", "r", encoding="utf-8") as info:
    info_text = info.read().replace("\n\n", "\n")
    print(info_text)

count_robotAttack = int(input("\nСКОЛЬКО РОБОТОВ СОЗДАТЬ? "))
# --------------------------------


pygame.init()

# ------IMAGE---------------------
robot_img = pygame.image.load("img/robot.png")
robotAttack_img = pygame.image.load("img/robotAttack.png")
shot_img = pygame.image.load("img/shot.png")
back_img = pygame.image.load("img/back.jpeg")
win_img = pygame.image.load("img/win.jpeg")
lose_img = pygame.image.load("img/lose.jpg")
# --------------------------------


# ------MUSIC---------------------
back_mus = pygame.mixer.Sound("music/music_for_back.mp3")
shot_mus = pygame.mixer.Sound("music/shot_music.mp3")
superShot_mus = pygame.mixer.Sound("music/superShot_mus.mp3")
dead_mus = pygame.mixer.Sound("music/lose_mus.mp3")
win_mus = pygame.mixer.Sound("music/win_mus.mp3")
# --------------------------------


# ------PYGAME--------------------
back_mus.play()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
pygame.display.set_caption("ROBOTS")
pygame.display.set_icon(robotAttack_img)
# --------------------------------


# ------VAR-----------------------
robotAttack_list = []
speed = 300
counter_for_create_robot = 0
font = pygame.font.SysFont('arial', 100)
text_dead = font.render(str('YOU DEAD'), True, THECOLORS['red'])
text_win = font.render(str('YOU WIN'), True, THECOLORS['green'])
# --------------------------------


# ------CREATE OBJECTS-----------------------
robot = Robot((0, 0), robot_img, count_robotAttack)
RobotAttack.create_robotAttack(robotAttack_list, robotAttack_img, screen, robot)
health_holder = HealthHolder(robot)
dead_holder = DeadHolder(robot)
superShot_holder = SuperShot_holder()
screen_obj = Screen(back_img)
shoots = []
# -------------------------------------------

object_list_for_update = [screen_obj, robot, health_holder, dead_holder, superShot_holder]

while True:
    # -------CONTROL PRESSED---------------------
    for event in pygame.event.get():
        close_app(event)
        if event.type == pygame.KEYDOWN:
            control_robot_move(event)
            control_shot(event)
            control_super_shot(event)
    # -------------------------------------------

    create_new_robotsAttack_by_time(speed, screen_obj)
    check_final(robot, robotAttack_list, screen_obj)

    # -------UPDATE OBJECTS---------------------
    for obj in object_list_for_update:
        if not screen_obj.is_final_scene:
            obj.update(screen)
    # -------------------------------------------

    RobotAttack.diff_move(robotAttack_list, screen)
    robotAttack_collision(robotAttack_list)
    shots_behavior(shoots)

    # ----PYGAME SETTINGS------------------------
    clock.tick(60)
    pygame.display.update()
    # -------------------------------------------

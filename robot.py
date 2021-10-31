from pygame import Vector2


class Robot:
    SIZE = 80

    def __init__(self, pos, robot_img, count_robotAttack, health=100):
        self.pos_x, self.pos_y = pos[0], pos[1]
        self.health = health
        self.image = robot_img
        self.SIZE = 80
        self.hit = 0
        self.count_robotAttack = count_robotAttack

    @property
    def pos(self):
        return self.pos_x, self.pos_y

    def update(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))

    def get_health(self):
        return self.health

    def get_hit(self):
        return self.hit

    def move_a(self, size):
        if self.health > 0:
                self.pos_x -= size

    def move_w(self,size):
        if self.health > 0:
                self.pos_y -= size

    def move_d(self,size):
        if self.health > 0:
                self.pos_x += size

    def move_s(self,size):
        if self.health > 0:
                self.pos_y += size

    # TODO: РАЗОБРАТЬСЯ
    # directions = {"a": move_a(SIZE),
    #               "w": move_w(SIZE),
    #               "s": move_s(SIZE),
    #               "d": move_d(SIZE)}

    def robotAttack_collision(self, robotAttack_list, shot):
        for ra in robotAttack_list[::-1]:
            if ra.pos_x - 40 <= shot.pos_x <= ra.pos_x + 40 and ra.pos_y - 40 <= shot.pos_y <= ra.pos_y + 70:
                robotAttack_list.remove(ra)
                self.hit += 1
            elif ra.pos_x - 40 <= self.pos_x <= ra.pos_x + 40 and ra.pos_y - 40 <= self.pos_y <= ra.pos_y + 70:
                robotAttack_list.remove(ra)
                self.health -= 100 // self.count_robotAttack

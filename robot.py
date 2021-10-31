from pygame import Vector2


class Robot:
    SIZE = 80

    def __init__(self, pos, robot_img, count_robotAttack, health=100):
        self.pos_x, self.pos_y = pos[0], pos[1]
        self.health = health
        self.image = robot_img
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

    def move_a(self):
        if self.health > 0:
            self.pos_x -= Robot.SIZE

    def move_w(self):
        if self.health > 0:
            self.pos_y -= Robot.SIZE

    def move_d(self):
        if self.health > 0:
            self.pos_x += Robot.SIZE

    def move_s(self):
        if self.health > 0:
            self.pos_y += Robot.SIZE

    def move(self, key):
        directions = {"a": self.move_a,
                      "w": self.move_w,
                      "s": self.move_s,
                      "d": self.move_d}

        if move_in_direction := directions.get(key):
            move_in_direction()


    def get_collison(self, ra, obj=None):
        if obj is None:
            obj = self
        if ra.pos_x - 40 <= obj.pos_x <= ra.pos_x + 40 and ra.pos_y - 40 <= obj.pos_y <= ra.pos_y + 70:
            return True
        else:
            return False

    def robotAttack_collision(self, robotAttack_list, shot):
        for ra in robotAttack_list[::-1]:
            if self.get_collison(ra, shot):
                robotAttack_list.remove(ra)
                self.hit += 1
                shot.is_active = False

            elif self.get_collison(ra):
                robotAttack_list.remove(ra)
                self.health -= 100 // self.count_robotAttack

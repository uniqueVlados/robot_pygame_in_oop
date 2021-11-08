from pygame import Vector2


class Robot:
    SIZE = 72

    def __init__(self, pos, robot_img, count_robotAttack, health=100):
        self.pos_x, self.pos_y = pos[0], pos[1]
        self.health = health
        self.image = robot_img
        self.hit = 0
        self.count_robotAttack = count_robotAttack
        Robot.SIZE = self.image.get_size()[0]

    def __repr__(self):
        return f"({self.pos_x}, {self.pos_y})"

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


    def get_collison(self, ra, obj):
        print(f"R: {obj.pos_x, obj.pos_y} A: {ra.pos_x, ra.pos_y}")
        return ra.pos_x <= obj.pos_x <= ra.pos_x + ra.image.get_size()[0] and ra.pos_y <= \
                obj.pos_y <= ra.pos_y + ra.image.get_size()[1]

    def robotAttack_collision(self, robotAttack_list, shot):
        for ra in robotAttack_list[::-1]:
            if self.get_collison(ra, shot):
                robotAttack_list.remove(ra)
                self.hit += 1
                shot.is_active = False

            elif self.get_collison(ra, self):
                print("CHECK ROB COL")
                robotAttack_list.remove(ra)
                self.health -= 100 // self.count_robotAttack

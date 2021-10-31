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

    def move(self, side, size):
        if self.health > 0:
            if side == "a":
                self.pos_x -= size
            elif side == "w":
                self.pos_y -= size
            elif side == "d":
                self.pos_x += size
            elif side == "s":
                self.pos_y += size

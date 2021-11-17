class Screen:
    WIDTH = 720
    HEIGHT = 720

    def __init__(self, back_img):
        self.is_final_scene = False
        self.back_img = back_img

    def update(self, screen):
        if not self.is_final_scene:
            screen.blit(self.back_img, (0, 0))

import pygame


class MenuButton(pygame.sprite.Sprite):
    def __init__(
        self, msg: str, position: tuple, fb_simulator, width=200, height=50
    ):
        super(MenuButton, self).__init__()
        self.x = position[0]
        self.y = position[1]
        self.width = width
        self.height = height
        self.fill_color = (255, 255, 255)
        self.msg = msg
        self.position = position

        self.surf = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.fb_simulator = fb_simulator

    def mouse_is_over(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def draw(self, window):
        self.text = self.fb_simulator.FONT.render(
            self.msg, True, self.fb_simulator.FONT_COLOR
        )
        center = (
            (self.width / 2 - self.text.get_width() / 2),
            (self.height / 2 - self.text.get_height() / 2),
        )

        self.surf.fill(self.fill_color)

        if self.mouse_is_over():
            self.surf.fill((0, 255, 0))

        self.surf.blit(self.text, center)
        window.blit(self.surf, self.position)

    def click(self):
        if self.fb_simulator.actions["mouse_click"]:
            if self.mouse_is_over():
                print("button click")
                pygame.time.wait(200)
                return True
        else:
            return False

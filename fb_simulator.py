from team import Team
from league import League
import argparse
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT


pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FONT = pygame.font.SysFont("Arial", 20)
FONT_COLOR = pygame.Color('black')


class PressText(pygame.sprite.Sprite):
    def __init__(self, element):
        super(PressText, self).__init__()
        self.surf = pygame.Surface((200, 50))
        self.surf.fill((255, 255, 255))
        self.text_surf = FONT.render(element, True, FONT_COLOR)
        self.text_rect = self.text_surf.get_rect(
            center=self.surf.get_rect().center
        )
        self.surf.blit(self.text_surf, self.text_rect)

        self.rect = self.surf.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.surf.fill((0, 255, 0))
            self.surf.blit(self.text_surf, self.text_rect)

        if not self.rect.collidepoint(mouse_pos):
            self.surf.fill((255, 255, 255))
            self.surf.blit(self.text_surf, self.text_rect)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--simulate",
        action="store_true",
        help="simulates a season outside of a gameloop",
    )
    args = parser.parse_args()

    if args.simulate:

        conference = League(
            (
                Team("Frazier"),
                Team("Geibel"),
                Team("Monessen"),
                Team("West Greene"),
            )
        )

        conference.start_season()
        conference.season_stats()

    else:

        screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

        box = PressText("Player Name")

        all_sprites = pygame.sprite.Group()
        all_sprites.add(box)

        game_running = True

        while game_running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        # eventually replace to back out of a menu or prompt
                        game_running = False
                elif event.type == pygame.QUIT:
                    game_running = False

                pressed_keys = pygame.key.get_pressed()

                # update state of game objects
                for sprite in all_sprites:
                    sprite.update()

                # Draw stuff here

                surf_center = (
                    (SCREEN_WIDTH - box.surf.get_width()) / 2,
                    (SCREEN_HEIGHT - box.surf.get_height()) / 2,
                )

                for entity in all_sprites:
                    screen.blit(entity.surf, entity.rect)

                pygame.display.flip()

                # maintain game speed

        pygame.quit()


if __name__ == "__main__":
    main()

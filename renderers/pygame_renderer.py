from .base import BaseRenderer


class PygameRenderer(BaseRenderer):
    WIDTH, HEIGHT = 160, 128

    def __init__(self):
        import pygame

        self._pygame = pygame
        self._screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self._font = pygame.font.SysFont(None, 24)

    def render(self, game):
        self._screen.fill((0, 0, 0))
        text = self._font.render(game.last_pressed, True, (255, 255, 255))
        rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self._screen.blit(text, rect)
        self._pygame.display.flip()

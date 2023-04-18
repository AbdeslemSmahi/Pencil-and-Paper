import pygame
class Graphics():
    def __init__(self, display_dimensions):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(display_dimensions)
        pygame.display.set_caption("Pencil and Paper")

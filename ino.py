import pygame
class Ino(pygame.sprite.Sprite):
    """bad somebodys class"""

    def __init__(self, screen):
        """inizialization start place"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0 (1).png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """output bad somebody to screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """changing place bad somebody"""
        self.y += 0.04
        self.rect.y = self.y

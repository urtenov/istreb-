import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        """inisialization bullet"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.colour = 150, 211, 221
        self.speed = 10.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """changing bulletplace"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """drawing bullet"""
        pygame.draw.rect(self.screen, self.colour, self.rect)

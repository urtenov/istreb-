import pygame
from pygame.sprite import Sprite
class Gun(Sprite):
    def __init__(self, screen):
        """inizialization gun"""
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
    def output(self):
        """drowing gun"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """position gun"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1
        #self.rect.centerx = self.center

    def create_gun(self):
        """placing gun in centerx"""
        self.center = self.screen_rect.centerx


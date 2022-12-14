import pygame.font
from gun import Gun
from pygame.sprite import Group


class Scores():
    """output game information"""
    def __init__(self, screen, stats):
        """initialization score"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (100, 100, 100)
        self.font = pygame.font.SysFont(None, 40)
        self.image_score()
        self.image_guns()

    def image_guns(self):
        """kolvo lives"""
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    def image_score(self):
        """text->image"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def show_score(self):
        """output score on the screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.guns.draw(self.screen)

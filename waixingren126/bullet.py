import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_game):#子弹类
        super().__init__()
        self.screen=ai_game.screen
        self.setting=ai_game.setting
        self.color=self.setting.bullet_color
        #设置子弹位置
        self.rect=pygame.Rect(0,0,self.setting.bullet_width,self.setting.bullet_height)
        self.rect.midright=ai_game.ship.rect.midright
        self.x=float(self.rect.x)

    def update(self):
        self.x+=self.setting.bullet_speed
        self.rect.x=self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
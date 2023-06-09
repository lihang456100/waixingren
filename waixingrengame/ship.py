import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        #初始化飞船位置
        self.screen=ai_game.screen
        self.settings=ai_game.setting
        self.screen_rect=ai_game.screen.get_rect()

        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()

        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
        #移动标志
        self.moving_right=False
        self.moving_left=False

    def update(self):#修改位置
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed
        self.rect.x=self.x

    def blitme(self):#创建对象
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)#重生
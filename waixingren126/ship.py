import pygame

class Ship:
    def __init__(self,ai_game):
        #初始化飞船位置
        self.screen=ai_game.screen
        self.settings=ai_game.setting
        self.screen_rect=ai_game.screen.get_rect()

        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()

        self.rect.midleft=self.screen_rect.midleft
        self.y=float(self.rect.y)
        #移动标志
        self.moving_up=False
        self.moving_down=False
    def update(self):#修改位置
        if self.moving_up and self.rect.y>0:
            self.y-=self.settings.ship_speed
        if self.moving_down and self.rect.y<=740:
            self.y+=self.settings.ship_speed
        self.rect.y=self.y
    def blitme(self):#创建对象
        self.screen.blit(self.image,self.rect)
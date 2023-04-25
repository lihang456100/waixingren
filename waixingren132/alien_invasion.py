import sys
from random import randint

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):#初始化
        pygame.init()
        self.setting=Settings()
        self.screen=pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #设置颜色
        self.bg_color=(230,230,230)
        self.ship=Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self.__create__fleet()

    def run__game(self):
        while True:
            self.__check__events()
            self.__update__screen()
            self.ship.update()
            self.__update_bullets()

    def __check__events(self):#监听鼠标和键盘用于关闭界面
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self.__check__keydown__events(event)
            elif event.type==pygame.KEYUP:
                self.__check__keyup__events(event)

    def __create__fleet(self):#创建外星人相关
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        available_space_x=self.setting.screen_width-(2*alien_width)
        number_aliens_x=available_space_x//(2*alien_width)

        ship_height=self.ship.rect.height
        available_space_y=(self.setting.screen_height-(3*alien_height)-ship_height)
        number_rows=available_space_y//(2*alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.__create__alien(alien_number,row_number)

    def __create__alien(self,alien_number,row_number):
        random_number=randint(-20,20)
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        alien.x=alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x+random_number
        alien.rect.y=alien.rect.height+2*alien.rect.height*row_number+random_number
        self.aliens.add(alien)

    def __check__keydown__events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key==pygame.K_SPACE:
            self.__fire__bullet()
    def __check__keyup__events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False

    def __fire__bullet(self):#创建新子弹并加入到bullets
        new_bullet=Bullet(self)
        self.bullets.add(new_bullet)

    def __update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    def __update__screen(self):
        # 重绘屏幕
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 显示界面
        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__=='__main__':#实例化
    ai=AlienInvasion()
    ai.run__game()

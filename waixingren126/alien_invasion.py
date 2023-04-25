import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

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
    def __check__keydown__events(self,event):
        if event.key==pygame.K_UP:
            self.ship.moving_up=True
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=True
        elif event.key==pygame.K_SPACE:
            self.__fire__bullet()
    def __check__keyup__events(self,event):
        if event.key==pygame.K_UP:
            self.ship.moving_up=False
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=False

    def __fire__bullet(self):#创建新子弹并加入到bullets
        new_bullet=Bullet(self)
        self.bullets.add(new_bullet)

    def __update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.x>=1200:
                self.bullets.remove(bullet)
        print(len(self.bullets))
    def __update__screen(self):
        # 重绘屏幕
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 显示界面
        pygame.display.flip()

if __name__=='__main__':#实例化
    ai=AlienInvasion()
    ai.run__game()

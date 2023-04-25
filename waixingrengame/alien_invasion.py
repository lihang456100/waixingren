import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
class AlienInvasion:
    def __init__(self):#初始化
        pygame.init()
        self.setting=Settings()
        self.screen=pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.stats=GameStats(self)
        #设置颜色
        self.bg_color=(230,230,230)
        self.ship=Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self.__create__fleet()

    def run__game(self):
        while True:
            self.__check__events()
            if self.stats.game_active:
                self.ship.update()
                self.__update__bullets()
                self.__update__aliens()
            self.__update__screen()

    def __check__events(self):#监听鼠标和键盘用于关闭界面
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self.__check__keydown__events(event)
            elif event.type==pygame.KEYUP:
                self.__check__keyup__events(event)

    def __check__aliens__bottom(self):#外星人到底部后销毁
        screen_rect=self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=screen_rect.bottom:
                self.__ship__hit()
                break
    def __ship__hit(self):
        #响应外星人与飞船碰撞
        if self.stats.ship_left>0:
            self.stats.ship_left-=1
            self.aliens.empty()
            self.bullets.empty()
            self.__create__fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active=False

    def __check__fleet__edges(self):#边缘检测
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.__change__fleet__direction()
                break

    def __change__fleet__direction(self):#改变外星人方向
        for alien in self.aliens.sprites():
            alien.rect.y+=self.setting.fleet_drop_speed
        self.setting.fleet_direction*=-1

    def __update__aliens(self):
        self.__check__fleet__edges()
        self.aliens.update()#更新外星人位置
        if pygame.sprite.spritecollideany(self.ship,self.aliens):#检测玩家与外星人碰撞
            self.__ship__hit()

        self.__check__aliens__bottom()

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
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        alien.x=alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x
        alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
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

    def __update__bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.__check__bullet__alien__collisions()

    def __check__bullet__alien__collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) #检测子弹与外星人碰撞
        if not self.aliens:  # 刷新外星人
            self.bullets.empty()
            self.__create__fleet()
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

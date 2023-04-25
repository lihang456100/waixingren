import sys
import pygame
class AlienInvasion:
    def __init__(self):#初始化
        pygame.init()

        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        #设置颜色
        self.bg_color=(230,230,230)

    def run__game(self):
        while True:  #监听鼠标和键盘用于关闭界面
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                    #重绘屏幕
            self.screen.fill(self.bg_color)
                    #显示界面
            pygame.display.flip()
if __name__=='__main__':#实例化
    ai=AlienInvasion()
    ai.run__game()

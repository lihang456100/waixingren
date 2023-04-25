class GameStats:
    def __init__(self,ai_game):
        self.setting=ai_game.setting
        self.reset_stats()
        self.game_active=False#设置游戏状态
        f = open("score_highest.txt", "r")
        self.high_score= int(f.readline())#记录最高得分

    def reset_stats(self):#记录统计信息
        self.ship_left=self.setting.ship_limit
        self.score=0
        self.level=1
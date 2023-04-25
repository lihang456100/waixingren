class GameStats:
    def __init__(self,ai_game):
        self.setting=ai_game.setting
        self.reset_stats()
        self.game_active=True#设置游戏状态

    def reset_stats(self):#记录统计信息
        self.ship_left=self.setting.ship_limit
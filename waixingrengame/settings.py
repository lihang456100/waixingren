class Settings:
    def __init__(self):
        #基础设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.ship_speed=1.5
        self.ship_limit=3

        self.bullet_speed=1.5
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        #外星人设置
        self.alien_speed=1.0
        self.fleet_drop_speed=10
        self.fleet_direction=1
        #加快游戏速度即 提高等级
        self.speedup_scale=1.1
        self.initialize_dynamic_settings()
        #记分
        self.alien_points=50
        #提高分数速度
        self.score_scale=1.5

    def initialize_dynamic_settings(self):
        self.ship_speed=1.5
        self.bullet_speed=3.0
        self.alien_speed=1.0

        self.fleet_direction=1

    def increase_speed(self):
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
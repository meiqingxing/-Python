"""
设置
"""
class Settings():
    """
    存储《外星人入侵》的所有设置的类
    """
    def __init__(self):
        """初始化游戏的静态设置：游戏外观和飞船速度的属性"""
        # 屏幕设置
        self.screen_width = 1200  # 宽度，像素值
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 3  # 飞船的次数为3次

        # 子弹属性设置
        self.bullet_width = 3  # 宽
        self.bullet_height = 15  # 高
        self.bullet_color = 60, 60, 60  # 颜色
        self.bullets_allowed = 5  # 同时出现在屏幕上的子弹的数量

        # 外星人设置
        self.fleet_drop_speed = 10  # 指定外星人撞到屏幕边缘时，外星人向下移动的速度

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1  # 用于控制游戏节奏的加快速度
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()  # 初始化随游戏进行而变化的属性


    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5  # 飞船速度
        self.bullet_speed_factor = 3  # 子弹速度
        self.alien_speed_factor = 1  # 外星人速度

        self.fleet_direction = 1  # fleet_direction为1表示向右移，为-1表示向左移

        # 计分
        self.alien_points = 50  # 每个外星人的分数


    def increase_speed(self):
        """提高速度设置和外星人的点数"""
        self.ship_speed_factor *= self.speedup_scale  # 飞船的速度
        self.bullet_speed_factor *= self.speedup_scale  # 子弹速度
        self.alien_speed_factor *= self.speedup_scale  # 外星人速度

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

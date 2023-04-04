"""
显示当前得分
后面可以用来记录最高得分、等级和余下的飞船数
"""
import pygame.font  # 在屏幕上显示文本，导入此模块
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化现实得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)  # 实例化一个字体对象

        # 准备包含最高得分和当前得分的图像
        self.prep_score()  # 将要显示的文本转换为图像
        self.prep_high_score()
        self.prep_level()  # 在当前得分下方显示玩家当前等级
        self.prep_ships()


    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        round_score = int(round(self.stats.score, -1))
        # round()函数让小数精确到小数点后多少位，小数位数由第二个实参指定；若第二个实参为负数，将圆整到最近的10、100、1000等整数倍
        score_str = "{:,}".format(round_score)
        # 将数值转换为字符串时在其中插入逗号
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)  # 创建图像

        # 将得分放在屏幕的右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # 右边缘与屏幕右边缘相距20像素
        self.score_rect.top = 20  # 上边缘与屏幕上边缘相距20像素


    def show_score(self):
        """在屏幕上显示当前得分和最高得分，飞船的等级"""
        self.screen.blit(self.score_image, self.score_rect)  # 显示渲染好的得分图像，并放在score_rect指定的位置
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)


    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx  # 水平居中
        self.high_score_rect.top = self.score_rect.top  # 将top属性设置为当前得分图像的top属性


    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.screen_rect.bottom + 10  # 得分和等级之间留出空间


    def prep_ships(self):
        """显示还剩下多少艘飞船"""
        self.ships = Group()  # 创建一个空编组，用于存储飞船实例
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)




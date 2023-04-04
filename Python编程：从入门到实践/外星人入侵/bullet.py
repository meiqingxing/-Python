"""
存储Bullet类
"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_setting, screen, ship):
        # 为创建子弹实例，需要向__init__()传递ai_settings,screen,ship实例，还调用了supper()来继承Sprite
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()  # Python2.7的写法，也适用于Python3，可简写为super().__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx  # 子弹的初始位置取决于飞船当前的位置
        self.rect.top = ship.rect.top  # 子弹从飞船的顶部射出

        # 存储用小数表示的子弹y坐标位置
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color  # 将子弹的颜色和速度设置分别存储到self.color、self.speed_factor中
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor  # 子弹在屏幕上向上移动，y坐标不断减小，所以减去；speed_factor可以改变子弹的速度
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)  # 使用存储在self.color中的颜色填充表示子弹的rect占据的屏幕部分。
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):  # 让Ship继承Sprite，以便能够创建飞船编组

    def __init__(self, ai_settings, screen):
        # 初始化飞船并设置其初始位置
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')  # 加载图像
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # 在pygame中，原点(0, 0)位于屏幕左上角
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False  # 向上
        self.moving_down = False  # 向下

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 飞船移动到屏幕边缘后停止移动；self.rect.right返回飞船外接矩形的右边缘的x坐标；只有当飞船在屏幕内时，才调整self.center的值
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:  # 这样两个优先级一样
            self.center -= self.ai_settings.ship_speed_factor
        # if self.moving_up and self.rect.height < self.screen_rect.height:
        #     self.center += self.ai_settings.ship_speed_factor  # 向上走
        # if self.moving_dwon and self.rect. > 0:
        #     self.center -= self.ai_settings.ship_speed_factor  # 向下走

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):  # 在屏幕上绘制飞船的方法
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx  # 将飞船的属性center设置为屏幕中心的x坐标，该坐标通过属性screen_rect获得

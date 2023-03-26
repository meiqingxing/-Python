"""
演示外星人入侵游戏
创建一系列整个游戏都要用到的对象
"""
# 导包
import pygame  # 具有游戏开发所需的功能
# import sys  # 使用sys退出游戏；注释掉是因为game_functions中已经调用了这个库；在这个文件中没有用到这个库
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group  # pygame.sprite.Group类类似于列表，但提供了有助于开发游戏的额外功能
# from alien import Alien  # 由于不在此直接创建外星人，因此无需导入Alien类
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

# 定义初始化函数
def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()  # 初始化背景设置
    ai_settings = Settings()  # 存储在ai_settings中的设置
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 创建显示窗口
    pygame.display.set_caption("Alien Invasion")  # 设置显示窗口的名称

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)  # 飞船实例；  # 创建一艘飞船
    bullets = Group()  # 创建一个用于存储子弹的编组
    aliens = Group()  # 创建一个空编组,用来存储所有的外星人
    # 创建一个外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)  # 检查玩家的输入

        if stats.game_active:  # 只有在游戏状态为活动时，才会运行这一部分
            # gf.check_events(ship)
            ship.update()  # 更新飞船的位置
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)  # 更新所有屏幕上未消失的子弹的位置
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)  # 更新外星人的位置

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)  # 使用更新后的位置来绘制新屏幕



run_game()

# from info_print import print_info
# print_info()
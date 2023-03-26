"""
将事件管理与游戏的其他方面（如更新屏幕）分离
"""
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

# def check_events(ship):
#     """相应按键和鼠标事件"""
#     # 监听键盘和鼠标事件
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()  # 调用sys.exit()来退出游戏
#
#         elif event.type == pygame.KEYDOWN:
#             if event.type == pygame.K_RIGHT:
#                 ship.moving_right = True
#             elif event.type == pygame.K_LEFT:  # 使用elif，因为一个事件只能对应一种按键
#                 ship.moving_left = True
#
#         elif event.type == pygame.KEYUP:  # 松开右键，将moving_right改为False
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = False
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = False

# 上面定义的check_events()函数越来越长，所以将部分代码放在两个函数中，一个处理KEYDOWN事件，一个处理KEYUP事件，如下：
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:  # 向右
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # 向左
        ship.moving_left = True
    # elif event.key == pygame.K_UP:  # 向上
    #     ship.moving_up = True
    # elif event.key == pygame.K_DOWN:  # 向下
    #     ship.moving_down = True
    elif event.key == pygame.K_SPACE:  # 发射子弹
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:  # 每次为测试新功能运行程序后，都需要用鼠标关闭游戏，麻烦故设置快捷键Q结束游戏
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果子弹没有达到限制，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:  # 检查屏幕上未消失的子弹数是否小于数量限制
        # 创建新子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:  # 向右
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:  # 向左
        ship.moving_left = False
    # elif event.key == pygame.K_UP:  # 向上
    #     ship.moving_up = False
    # elif event.key == pygame.K_DOWN:  # 向下
    #     ship.moving_down = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):  # 添加形参bullets
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # 调用sys.exit()来退出游戏
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)  # 换成对check_keydown_events()函数的调用； # 将bullets作为实参传递
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)  # 换成对check_keyup_events()函数的调用
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # 获取玩家单击鼠标时的x和y坐标，返回元组
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)  # 使用collidepoint()检查鼠标单击位置是否在play按钮的rect内，返回True或False
    if button_clicked and not stats.game_active:  # 当点击了Play按钮且游戏当前处于非活动状态时，游戏才重新开始
        # 重置游戏设置，如飞船子弹外星人的速度
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标，游戏开始之后，光标会造成干扰
        pygame.mouse.set_visible(False)  # 光标位于游戏窗口内时暂时隐藏

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()  # 在游戏开始时让玩家知道他有多少艘飞船

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):  # 每次执行主循环都重绘屏幕； # 添加形参bullets
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():  # 方法bullets.sprites()返回一个列表，其中包含编组中的所有精灵
        bullet.draw_bullet()
    ship.blitme()  # 将飞船绘制在屏幕上
    aliens.draw(screen)  # 对编组调用draw()，自动绘制编组的每个元素，绘制位置由元素属性rect决定

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:  # 因为game_active是False
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()  # 每次执行while循环都绘制一个空屏幕，在移动游戏元素时，将不断更新屏幕，达到平滑移动的效果


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """更新子弹的位置，并删除屏幕上已经消失的子弹"""
    # 更新子弹的位置
    # 当你对编组调用update()时，编组将自动对其中的每个精灵调用update()，即为编组bullets中的每颗子弹调用bullet.update()
    bullets.update()
    # 删除屏幕上消失的子弹
    # 删除已消失的子弹；子弹到达顶部消失但依然存在，只是Pygame无法在屏幕外面绘制它们，子弹y坐标为负数，且越来越小
    for bullet in bullets.copy():  # 不应在列表或编组中删除条目，通过copy()遍历编组的副本
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))  # 打印当前还有多少颗子弹，用于核实消失的子弹是否被删除
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 将每颗子弹的rect和每个外星人的rect进行比较，并返回一个字典，键是子弹，值是被击中的外星人；两个实参True告诉Pygame删除发生碰撞的子弹和外星人

    if collisions:  # 检查字典是否存在，存在就加分
        for aliens in collisions.values():  # 在字典中，每个子弹是key；与子弹相关的value都是list，其中包含该子弹撞到的外星人
            stats.score += ai_settings.alien_points * len(aliens)  # 将一个外星人的点数乘以list中包含的外星人数量
            sb.prep_score()
        check_high_score(stats, sb)  # 每当有外星人被消灭，都需要在更新得分后调用check_high_score()

    if len(aliens) == 0:
        # 如果整群外星人都被消灭，删除现有子弹，加快游戏节奏，并创建一群新的外星人；玩家提高一个等级
        bullets.empty()  # 删除编组余下的所有精灵，从而删除现有的所有的子弹
        ai_settings.increase_speed()
        # 提高等级
        stats.level += 1
        sb.prep_level()  # 调用，以确保正确的显示新等级

        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width  # 屏幕左右边缘各留出一个外星人宽度的空间
    number_aliens_x = int(available_space_x / (2 * alien_width))  # 每个外星人之间的间隔为一个宽度；int确保外星人数量为整数
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)  # 计算垂直空间有多少
    number_rows = int(available_space_y / (2 * alien_height))  # 计算可容纳的行数
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)  # 创建alien实例
    alien_width = alien.rect.width  # 从外星人图像的rect属性中获取宽度，避免反复访问属性rect
    alien.x = alien_width + 2 * alien_width * alien_number  # 因为alien_number从0开始； # 修改外星人的x坐标
    alien.rect.x = alien.x  # 创建一个外星人，并通过设置其x坐标将其加入当前行
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number  #修改外星人的y坐标
    aliens.add(alien)  # 添加到编组


def create_fleet(ai_settings, screen, ship, aliens):  # 增加了用于存储ship对象的形参
    """创建外星人群"""
    alien = Alien(ai_settings, screen)  # 创建alien实例
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():  # 遍历外星人群
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)  # 调用函数，改变行进方向
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ship_left减1
        stats.ships_left -= 1

        # 更新计分牌
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)  # 飞船爆炸后，暂停0.5秒，让玩家看到飞船被撞了
    else:
        stats.game_active = False  # 如果没有飞船了，游戏状态改变
        pygame.mouse.set_visible(True)  # 游戏结束，光标在窗口内可见


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break  # 只要检测到一个外星人到达屏幕底端，就无需检查其他，直接退出循环


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边缘，并更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()  # 对编组调用

    # 检测外星人和飞船之间的碰撞
    # 接收两个实参：一个精灵和一个编组；找到与精灵发生碰撞的外星人后就停止遍历编组，并返回这个外星人；如果没有发生碰撞，就返回None，因此if语句不会执行
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_high_score(stats, sb):  # 用stats来比较当前得分和最高得分，并在必要时使用sb来修改最高得分图像
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()  # 来更新包含最高得分的图像



























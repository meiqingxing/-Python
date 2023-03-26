"""
不销毁ship实例，记录跟踪游戏的统计信息来记录飞船被装了多少次
"""


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时处于非活动状态
        self.game_active = False
        # 在任何情况下都不重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息
            在__init__()中调用这个方法，这样创建GameStats实例时将妥善的设置统计信息，同时在玩家开始新游戏时也能调用reset_stats()
        """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

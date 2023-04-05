class Song(object):   # 第一个类的例子

    # 构造方法
    def __init__(self, lyrics):   # init前面和后面应该有两个下划线，否则报错
                                  # __init__()特殊的类实例方法，构造函数
        self.lyrics = lyrics   # 指的是实例中的lyrics属性，而不是一个叫lyrics的局部变量
    # 定义函数
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",   # 字符串列表
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["There rally around the family",    # 字符串列表
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()   # 调用sing_me_a_song函数

bulls_on_parade.sing_me_a_song()

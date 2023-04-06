from django.db import models

# Create your models here.

class Topic(models.Model):
    """用户学习的主题
    继承Model（Django中一个定义了模型基本功能的类
    """
    text = models.CharField(max_length=200)  # 由字符或文本组成的数据；必须告诉Django应该在数据库中预留多少空间
    date_added = models.DateTimeField(auto_now_add=True)  # 记录日期和时间的数据；True：每当用户创建新主题时，将这个属性自动设置为当前日期和时间

    def __str__(self):

        """返回存储在属性text中的字符串
        告诉Django默认应使用哪个属性来显示有关主题的信息
        """
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识
    继承Django基类Model
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # 外键是一个数据库术语，它引用了数据库中的另一条记录；这些代码将每个条目关联到特定的主题。每个主题创建时。都给它分配了一个键（ID）
    # django升级到2.0之后,表与表之间关联的时候,必须要写on_delete参数,否则会报异常:TypeError: init() missing 1 required positional argument:'on_delete'

    text = models.TextField()  # 不限制字段长度
    date_added = models.DateTimeField(auto_now_add=True)  # 按创建顺序呈现条目，并放置时间戳

    class Meta:
        """Meta存储用于管理模型的额外信息，在这里，它让我们能够设置一个特殊属性，让Django在需要时使用Entries来表示多个条目。
        如果没有这个类，Django将使用Entrys来表示多个条目。
        """
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."  # 由于条目包含的文本可能很长，我们让Django只显示text的前50个字符


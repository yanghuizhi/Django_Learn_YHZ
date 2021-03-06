import math
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils.html import mark_safe
from markdown import markdown
# Create your models here.

"""
    django 要求模型必须继承 models.Model 类
    django 内置全部类型文档：
    https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
"""

class Board(models.Model):
    """
        模版
    """
    # unique=True，强制数据库级别字段的唯一性。
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    """
        书籍名称
    """
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    # 外键关联，ForeignKey(关联表，related_name=自定义关联名称,'+'号代表忽略)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)  # <- 页面浏览量

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def get_page_count(self):
        count = self.posts.count()
        pages = count / 20
        return math.ceil(pages)

    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 6

    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)

        return range(1, count + 1)

    # 展示最近的10个回复
    def get_last_ten_posts(self):
        return self.posts.order_by('-created_at')[:10]


class Post(models.Model):
    """
        帖子
    """
    # 文章标题
    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    message = models.TextField(max_length=4000)
    # auto_now_add=True 当前日期和时间
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        truncated_message = Truncator(self.message)
        # 将一个⻓字符串截取为 任意⻓度字符的简便方法(这里我们使用30个字符)
        return truncated_message.chars(30)

    def get_message_as_markdown(self):
        # Markdown支持
        return mark_safe(markdown(self.message, safe_mode='escape'))


    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

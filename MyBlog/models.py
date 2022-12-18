from django.db import models
from tinymce.models import HTMLField


class Category(models.Model):
    cname = models.CharField(max_length=50, unique=True, verbose_name='分类')

    def __str__(self):
        return self.cname

    class Meta:
        db_table = 'B_Category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name

class Tag(models.Model):
    tname = models.CharField(max_length=50, unique=True, verbose_name='标签')

    def __str__(self):
        return self.tname

    class Meta:
        db_table = 'B_Tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

class Article(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='标题')
    desc = models.CharField(max_length=200, verbose_name='描述')
    content = HTMLField(blank=True, verbose_name='内容')
    create = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    modify = models.DateTimeField(auto_now=True, verbose_name='修改日期')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')
    category = models.ForeignKey('Category',on_delete=models.DO_NOTHING, verbose_name='分类')
    tag = models.ManyToManyField('Tag', verbose_name='标签')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'B_Article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['id']
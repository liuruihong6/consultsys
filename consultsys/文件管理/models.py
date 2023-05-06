
from django.db import models


# Create your models here.

# class file(models.Model):
#     filename = models.FileField()
#
#     def __unicode__(self):
#         return u
#         'self.filename'
#
# coding:utf-8
from django.db import models


class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    ph = models.ImageField(u'图片',upload_to='uploadImages')

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
    class Meta:
        verbose_name_plural = '文件上传'




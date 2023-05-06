from django.db import models

# Create your models here.
class form(models.Model):
    投保人 = models.CharField(max_length=200,null=True,blank=True)
    保单号 = models.CharField(max_length=200,null=True,blank=True)
    性别 = models.CharField(max_length=200,null=True,blank=True)
    年龄 = models.CharField(max_length=200, null=True, blank=True)
    身份证 = models.CharField(max_length=200, null=True, blank=True)
    电话号 = models.CharField(max_length=200, null=True, blank=True)
    邮箱 = models.EmailField(max_length=200, null=True, blank=True)
    家庭住址 = models.CharField(max_length=200, null=True, blank=True)
    投保时间 = models.DateField(max_length=200,null=True,blank=True)
    class Meta:
        verbose_name_plural = '投保信息'

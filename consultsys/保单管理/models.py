from django.db import models

# Create your models here.
class custom3(models.Model):
    投保人 = models.CharField(max_length=200,null=True,blank=True)
    sex_type1 = (('1', u'全家保'), ('2', u'吉祥保'), ('3', u'女神保'), ('4', u'男神保'), ('5', u'育才保'), ('6', u'孝心保'))
    sex1 = models.CharField(u"投保类型", choices=sex_type1, max_length=32, null=True, blank=True)
    保单号 = models.CharField(max_length=200,null=True,blank=True)
    sex_type = (('male', u'男'), ('female', u'女'))
    sex = models.CharField(u"性别", choices=sex_type, max_length=32, null=True, blank=True)
    年龄 = models.CharField(max_length=200, null=True, blank=True)
    身份证 = models.CharField(max_length=200, null=True, blank=True)
    电话号 = models.CharField(max_length=200, null=True, blank=True)
    邮箱 = models.EmailField(max_length=200, null=True, blank=True)
    家庭住址 = models.CharField(max_length=200, null=True, blank=True)
    投保时间 = models.DateField(max_length=200,null=True,blank=True)

    class Meta:
        verbose_name_plural = '在线投保'

# class person(models.Model):
#     sex_type = (('male', u'男'), ('female', u'女'))
#     sex = models.CharField(u"性别", choices=sex_type, max_length=32)


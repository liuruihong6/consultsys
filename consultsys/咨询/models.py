from django.db import models

# Create your models here.
class custom(models.Model):
    咨询号 = models.CharField(max_length=200,null=True,blank=True)
    客户提问 = models.CharField(max_length=200,null=True,blank=True)
    备注 = models.CharField(max_length=200,null=True,blank=True)
    class Meta:
        verbose_name_plural = '客户提问 '




class custom1(models.Model):
    咨询号 = models.CharField(max_length=200, null=True, blank=True)
    业务员解答 = models.CharField(max_length=200,null=True,blank=True)
    备注 = models.CharField(max_length=200,null=True,blank=True)
    class Meta:
        verbose_name_plural = '业务员解答 '
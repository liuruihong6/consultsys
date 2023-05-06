from django.db import models

# Create your models here.

class notice(models.Model):
    ...
    content = models.TextField(verbose_name='通知',null=True,blank=True)
    class Meta:
        verbose_name_plural = '审核员通知'

    # 判断指定字段长度,超出部分用省略号代替
    def update_content(self):
        if len(str(self.content)) > 50:
            return '{}...'.format(str(self.content)[0:50])
        else:
            return self.content

    # 字段数据处理后,字段verbose_name参数失效
    # 需要重新指定,否则列表页字段名显示的是方法名(update_content)
    update_content.short_description = '通知'




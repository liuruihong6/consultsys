from django.db import models

# Create your models here.
class TestModel(models.Model):
    ...
    content = models.TextField(verbose_name='产品介绍')
    class Meta:
        verbose_name_plural = '产品1'

    # 判断指定字段长度,超出部分用省略号代替
    def update_content(self):
        if len(str(self.content)) > 35:
            return '{}...'.format(str(self.content)[0:35])
        else:
            return self.content

    # 字段数据处理后,字段verbose_name参数失效
    # 需要重新指定,否则列表页字段名显示的是方法名(update_content)
    update_content.short_description = '产品介绍'


class TestModel2(models.Model):
    ...
    content = models.TextField(verbose_name='产品介绍')
    class Meta:
        verbose_name_plural = '产品2'

    # 判断指定字段长度,超出部分用省略号代替
    def update_content(self):
        if len(str(self.content)) > 35:
            return '{}...'.format(str(self.content)[0:35])
        else:
            return self.content

    # 字段数据处理后,字段verbose_name参数失效
    # 需要重新指定,否则列表页字段名显示的是方法名(update_content)
    update_content.short_description = '产品介绍'


class TestModel3(models.Model):
    ...
    content = models.TextField(verbose_name='产品介绍')
    class Meta:
        verbose_name_plural = '产品3'

    # 判断指定字段长度,超出部分用省略号代替
    def update_content(self):
        if len(str(self.content)) > 35:
            return '{}...'.format(str(self.content)[0:35])
        else:
            return self.content

    # 字段数据处理后,字段verbose_name参数失效
    # 需要重新指定,否则列表页字段名显示的是方法名(update_content)
    update_content.short_description = '产品介绍'

class TestModel4(models.Model):
    ...
    content = models.TextField(verbose_name='产品介绍')
    class Meta:
        verbose_name_plural = '产品4'

    # 判断指定字段长度,超出部分用省略号代替
    def update_content(self):
        if len(str(self.content)) > 35:
            return '{}...'.format(str(self.content)[0:35])
        else:
            return self.content

    # 字段数据处理后,字段verbose_name参数失效
    # 需要重新指定,否则列表页字段名显示的是方法名(update_content)
    update_content.short_description = '产品介绍'



class TestModel5(models.Model):
    ...
    content = models.TextField(verbose_name='产品介绍')
    class Meta:
        verbose_name_plural = '产品5'

    # 判断指定字段长度,超出部分用省略号代替
    def update_content(self):
        if len(str(self.content)) > 35:
            return '{}...'.format(str(self.content)[0:35])
        else:
            return self.content

    # 字段数据处理后,字段verbose_name参数失效
    # 需要重新指定,否则列表页字段名显示的是方法名(update_content)
    update_content.short_description = '产品介绍'



class TestModel6(models.Model):
    ...
    content = models.TextField(verbose_name='产品介绍')
    class Meta:
        verbose_name_plural = '产品6'

    # 判断指定字段长度,超出部分用省略号代替
    def update_content(self):
        if len(str(self.content)) > 35:
            return '{}...'.format(str(self.content)[0:35])
        else:
            return self.content

    # 字段数据处理后,字段verbose_name参数失效
    # 需要重新指定,否则列表页字段名显示的是方法名(update_content)
    update_content.short_description = '产品介绍'
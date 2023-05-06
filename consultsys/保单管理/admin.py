from django.contrib import admin
from 保单管理.models import custom3



# Register your models here.
class custom3Admin(admin.ModelAdmin):
    #显示字段
    list_display = ('保单号','sex1','投保人','sex','年龄','身份证','电话号','邮箱','投保时间',)
    # 增加字段筛选
    search_fields = ('保单号','sex1','投保人','sex','年龄','身份证','电话号','邮箱','投保时间',)
admin.site.register(custom3,custom3Admin)

# from .models import person
#
# # -*- coding: utf-8 -*-
#
#
# from django.contrib import admin
#
# from 保单管理.models import person
#
#
# admin.site.register(person)

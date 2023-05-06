from django.contrib import admin
from 保单跟进.models import form
from django.utils.html import format_html
# Register your models here.
class formAdmin(admin.ModelAdmin):
    #显示字段
    list_display = ('保单号','投保人','性别','年龄','身份证','电话号','邮箱','投保时间','operator')
    # 增加字段筛选
    search_fields = ('保单号','投保人','性别','年龄','身份证','电话号','邮箱','投保时间')
    def operator(self, obj):
        return format_html(
            '<a href="/update_data/">通过<a/>'
        )
    operator.short_description = '审核'
admin.site.register(form,formAdmin)
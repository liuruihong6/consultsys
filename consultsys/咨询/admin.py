from django.contrib import admin
from 咨询.models import custom
from 咨询.models import custom1
from django.utils.html import format_html
# Register your models here.
admin.AdminSite.site_header = '人寿保险客户端咨询管理系统'
admin.AdminSite.site_title = '人寿保险客户端咨询管理系统'
admin.AdminSite.index_title = '首页'


class customAdmin(admin.ModelAdmin):

    #显示字段
    list_display = ('咨询号','客户提问','备注','operator')
    # 增加字段筛选
    search_fields = ('咨询号','客户提问','备注')

    def operator(self, obj):
        return format_html(
            '<a href="/update/">同步对话<a/>'
        )

    operator.short_description = '刷新'




admin.site.register(custom,customAdmin)

class custom1Admin(admin.ModelAdmin):
    #显示字段
    list_display = ('咨询号','业务员解答','备注','operator')
    # 增加字段筛选
    search_fields = ('咨询号','业务员解答','备注')
    def operator(self, obj):
        return format_html(
            '<a href="/update/">同步对话<a/>'
        )

    operator.short_description = '刷新'
admin.site.register(custom1,custom1Admin)
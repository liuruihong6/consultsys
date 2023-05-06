from django.contrib import admin
from 产品管理.models import TestModel
from 产品管理.models import TestModel2
from 产品管理.models import TestModel3
from 产品管理.models import TestModel4
from 产品管理.models import TestModel5
from 产品管理.models import TestModel6
from django.utils.html import format_html
# Register your models here.




class TestModelAdmin(admin.ModelAdmin):
    list_display = ['update_content','operator']
    def operator(self, obj):
        return format_html(
            '<a href="/details/">查看详情<a/>'
        )

    operator.short_description = '详情'
admin.site.register(TestModel,TestModelAdmin)

class TestModel2Admin(admin.ModelAdmin):
    list_display = ['update_content','operator']
    def operator(self, obj):
        return format_html(
            '<a href="/details2/">查看详情<a/>'
        )

    operator.short_description = '详情'
admin.site.register(TestModel2,TestModel2Admin)
class TestModel3Admin(admin.ModelAdmin):
    list_display = ['update_content','operator']
    def operator(self, obj):
        return format_html(
            '<a href="/details3/">查看详情<a/>'
        )

    operator.short_description = '详情'
admin.site.register(TestModel3,TestModel3Admin)
class TestModel4Admin(admin.ModelAdmin):
    list_display = ['update_content','operator']
    def operator(self, obj):
        return format_html(
            '<a href="/details4/">查看详情<a/>'
        )

    operator.short_description = '详情'
admin.site.register(TestModel4,TestModel4Admin)
class TestModel5Admin(admin.ModelAdmin):
    list_display = ['update_content','operator']
    def operator(self, obj):
        return format_html(
            '<a href="/details5/">查看详情<a/>'
        )

    operator.short_description = '详情'
admin.site.register(TestModel5,TestModel5Admin)
class TestModel6Admin(admin.ModelAdmin):
    list_display = ['update_content','operator']
    def operator(self, obj):
        return format_html(
            '<a href="/details6/">查看详情<a/>'
        )

    operator.short_description = '详情'
admin.site.register(TestModel6,TestModel6Admin)

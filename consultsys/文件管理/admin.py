from django.contrib import admin

# Register your models here.
# class filelist(admin.ModelAdmin):
#     list_display = ('filename',)
#
#
# admin.site.register(file, filelist)
from .models import Article




admin.site.register(Article)
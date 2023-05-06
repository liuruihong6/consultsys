from django.contrib import admin

# Register your models here.
from .models import notice





@admin.register(notice)
class TestAdmin(admin.ModelAdmin):
    list_display = ['update_content']


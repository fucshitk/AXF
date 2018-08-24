'''
定义站点管理
# TODO 谈谈如何使用django的站点管理?
'''

from django.contrib import admin
from App.models import FoodType

class FoodTypeAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(FoodType,FoodTypeAdmin)

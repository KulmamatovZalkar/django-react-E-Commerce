from pyclbr import Class
from django.contrib import admin
from .models import CategoryModel
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(CategoryModel, CategoryAdmin)
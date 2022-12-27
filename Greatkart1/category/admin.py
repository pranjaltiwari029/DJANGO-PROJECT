from django.contrib import admin
from .models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_feilds = {'slug': ('category_name',)}
    
admin.site.register(Category, CategoryAdmin)

from django.contrib import admin

from models import TypeInfo,ProductInfo
# Register your models here.

@admin.register(TypeInfo)
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ['id','pname','pprice']
    list_per_page = 15
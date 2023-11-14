from django.contrib import admin
from .models import Product, Category


# Register your models here.

class admincategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, admincategory)


class productcategory(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 15


admin.site.register(Product, productcategory)

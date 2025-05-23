from django.contrib import admin

from goods.models import Categories
from goods.models import Products


#admin.site.register(Products)
#admin.site.register(Categories)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
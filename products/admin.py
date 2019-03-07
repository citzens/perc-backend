from django.contrib import admin
from products.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['Product_Name','id','Product_Price']


admin.site.register(Product, ProductAdmin)

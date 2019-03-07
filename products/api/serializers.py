from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        fields = ['Product_Name','Product_Price','Product_Image']



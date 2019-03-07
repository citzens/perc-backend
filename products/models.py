from django.db import models

# Create your models here.



class Product(models.Model):
    Product_Name = models.CharField(max_length=200)
    Product_Price = models.CharField(max_length=250)
    Product_Image = models.ImageField()

    def __str__(self):
        return self.Product_Name

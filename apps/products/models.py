from __future__ import unicode_literals

from django.db import models
from django import forms



class Category(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=45)
    category = models.ForeignKey(Category)
    quantity = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


"""
This is for image upload
"""


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    product_pic = models.ImageField(upload_to="apps/products/static/products/images",
                                    default="apps/products/static/products/images/None/default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

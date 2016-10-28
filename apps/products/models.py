from __future__ import unicode_literals

from django.db import models
from django import forms
from django.conf import settings
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location=settings.MEDIA_ROOT)


class Category(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=45)
    category = models.ForeignKey(Category)
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(storage=fs)#, default=settings.MEDIA_ROOT + "/None/default.png")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


"""
This is for image upload
"""

class ImageUploadForm(forms.Form):
    name=forms.CharField(max_length=45) 
    category=forms.IntegerField()
    categorynew=forms.CharField(max_length=45)
    quantity=forms.IntegerField()
    description=forms.CharField(max_length=255)
    price=forms.FloatField()
    image = forms.ImageField()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True)
    product_pic = models.ImageField(upload_to="apps/products/static/products/images",
                                    default="apps/products/static/products/images/None/default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
	name = models.CharField(max_length = 45)
	category = models.ForeignKey(Category)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Quantity(models.Model):
	amount = models.IntegerField()
	product = models.ForeignKey(Product)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

# class Order(model.Model):
# 	user = models.ForeignKey(User)
# 	#limited choices
# 		#Cancelled
# 		#Order in Process
# 		#Order Shipped
# 	# status = models.()
# 	product = models.ForeignKey(Product)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

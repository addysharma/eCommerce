from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
import bcrypt
import re

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.

class UserManager(models.Manager):
	def login(self, post):
		user_list = User.objects.filter(email = post['email'])
		if user_list:
			user = user_list[0]
			if bcrypt.hashpw(post['password'].encode(), user.password.encode()) == user.password:
				return user
			return None

	def register(self, post):
		encrypted_password = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt())
		User.objects.create(first_name = post['first_name'], last_name= post['last_name'], email = post['email'], password = encrypted_password)

class ShippingManager(models.Manager):

	pass

class BillingManager(models.Manager):
	pass

class OrderManager(models.Manager):

	pass

class User(models.Model):
	first_name = models.TextField(max_length = 100)
	last_name = models.TextField(max_length = 100)
	billing_address = models.ForeignKey(Address)
	shipping_address = models.ForeignKey(Address)
	admin = BooleanField(default = False)
	email = models.TextField(max_length = 1000)
	password = models.TextField(max_length = 1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

class Address(models.Model):
	user_ship = models.ForeignKey(User)
	country = models.TextField(max_length = 3)
	state = models.TextField(max_length = 2)
	city = models.TextField(max_length = 1000)
	street = models.TextField(max_length = 1000)
	zip_code = models.TextField(max_length = 6)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = ShippingManager()



class Order(models.Model):
	customer = ForeignKey(User)
	items = models.ManyToManyField(Product, related_name="item_order")
	total_price = models.DecimalField(max_digits=6, decimal_places=2)
	ship_to = ForeignKey(Address)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = OrderManager()

# class Quantity(models.Model):
#

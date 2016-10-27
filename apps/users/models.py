from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
import bcrypt
import re
from ..products.models import Product

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

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
		User.objects.create(first_name = post['first_name'], last_name= post['last_name'], email = post['email'], password = encrypted_password, admin = post['adminStatus'])

class ShippingManager(models.Manager):
	pass

class BillingManager(models.Manager):
	pass

class OrderManager(models.Manager):
	def total(self, post):
		sumOrder = 0
		for item in post.items:
			sumOrder += item.price
		return sumOrder

	def generate(self, post):
		user = User.objects.get(id = request.session['logged_user'])
		order = Product.objects.get(id = post['id'])
		order.items.add(customer = user, )
		order.save()


class User(models.Model):
	first_name = models.TextField(max_length = 100)
	last_name = models.TextField(max_length = 100)
	admin = models.BooleanField(default = False)
	email = models.TextField(max_length = 1000)
	password = models.TextField(max_length = 1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

class Shipping_Address(models.Model):
	name = models.TextField(max_length= 100)
	user_ship = models.ForeignKey(User)
	country = models.TextField(max_length = 3)
	state = models.TextField(max_length = 2)
	city = models.TextField(max_length = 1000)
	street = models.TextField(max_length = 1000)
	zip_code = models.TextField(max_length = 6)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = ShippingManager()

class Billing_Address(models.Model):
	name = models.TextField(max_length= 100)
	user_bill = models.ForeignKey(User)
	country = models.TextField(max_length = 3)
	state = models.TextField(max_length = 2)
	city = models.TextField(max_length = 1000)
	street = models.TextField(max_length = 1000)
	zip_code = models.TextField(max_length = 6)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class Order(models.Model):
	customer = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = OrderManager()

class Order_Products(models.Model):
	order_id = models.ForeignKey(Order)
	product_id = models.ForeignKey(Product)
	quantity = models.DecimalField(max_digits=6, decimal_places = 0)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

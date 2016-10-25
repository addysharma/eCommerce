from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

# Create your models here.

class UserManager(models.Manager):
    def login(self, current):
        user_list = User.objects.filter(email = post['email'])
        if user_list:
            user = user_list[0]
            if bcrypt.hashpw(current['password'].encode(), user.password.encode()) == user.password:

	def register(self, current):
        encrypted_password = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = current['first_name'], last_name= current['last_name'], email = current['email'], password = encrypted_password)



class User(models.Model):
	first_name = models.TextField(max_length = 100)
	last_name = models.TextField(max_length = 100)
	email = models.TextField(max_length = 1000)
	password = models.TextField(max_length = 1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	card_number = models.TextField(max_length = 100)
	card_expiration = models.DateTimeField()
	card_CVS = models.TextField(max_length = 3)
	admin = models.BooleanField(default = False)
	objects = UserManager()

class Address(models.Model):
	country = models.TextField(max_length = 3)
	state = models.TextField(max_length = 2)
	city = models.TextField(max_length = 1000)
	street = models.TextField(max_length = 1000)
	zip_code = models.TextField(max_length = 6)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

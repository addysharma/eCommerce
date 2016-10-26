from __future__ import unicode_literals

from django.db import models

# Create your models here.
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

class Address(models.Model):
	country = models.TextField(max_length = 3)
	state = models.TextField(max_length = 2)
	city = models.TextField(max_length = 1000)
	street = models.TextField(max_length = 1000)
	zip_code = models.TextField(max_length = 6)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
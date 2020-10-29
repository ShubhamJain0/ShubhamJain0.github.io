from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from datetime import (date, datetime)
from django.utils.timezone import now

from django.db.models import Q
# Create your models here.

CATEGORIES = (

	('BreakFast', 'BreakFast'),
	('Lunch', 'Lunch'),
	('Dinner', 'Dinner'),

	)



STATUS_CATEGORY = (

	('Accepted', 'Accepted'),
	('Reservations are full!', 'Reservations are full!'),

	)






class CustomUserModelManager(BaseUserManager):

	def create_user(self, email, password=None, **extra_fields):

		if not email:
			raise ValueError('Email is needed!')

		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)

		return user


	def create_superuser(self, email, password):

		user = self.create_user(email, password)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)

		return user




class orderfoodQuerySet(models.QuerySet):
	def search(self, query):

		lookup = (Q(items__iexact=query)|
					Q(items__contains=query))

		return self.filter(lookup)



class orderfoodManager(models.Manager):
	def get_queryset(self):
		return orderfoodQuerySet(self.model, using=self._db)


	def search(self, query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)



class CustomUserModel(AbstractBaseUser, PermissionsMixin):

	email = models.EmailField(unique=True, max_length=255)
	name = models.CharField(null=True, max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = CustomUserModelManager()

	USERNAME_FIELD = 'email'



class orderfood(models.Model):


	items = models.CharField(max_length=255)
	image = models.ImageField(null=True, upload_to='images/')
	category = models.CharField(max_length=20, null=True, choices=CATEGORIES)
	price = models.IntegerField(null=True)

	objects = orderfoodManager()



class yourorder(models.Model):

	ordereditems = models.CharField(max_length=255, null=True)
	ordereddate = models.DateField(default=now)
	orderedtime = models.TimeField(default=now)
	houseno = models.CharField(null=True, max_length=15)
	street = models.IntegerField(null=True)
	locality = models.CharField(null=True,max_length=255)
	city = models.CharField(default='Hyderabad', max_length=255)
	phone = models.CharField(max_length=10, null=True)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		)



class cartitems(models.Model):

	ordereditems = models.CharField(max_length=255)
	price = models.IntegerField(null=True)
	ordereddate = models.DateField(default=now)
	orderedtime = models.TimeField(default=now)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		)
	


class manageaddress(models.Model):


	houseno = models.CharField(null=True, max_length=15)
	street = models.IntegerField()
	locality = models.CharField(max_length=255)
	city = models.CharField(default='Hyderabad', max_length=255)
	phone = models.CharField(max_length=10, null=True, unique=True)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE
		)


class addressid(models.Model):

	addressidofuser = models.IntegerField()
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE
		)



class search(models.Model):

	user=models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
	query=models.CharField(max_length=200)



class Order(models.Model):

	ordereditems = models.CharField(max_length=255)
	ordereddate = models.DateField(default=now)
	orderedtime = models.TimeField(default=now)
	houseno = models.CharField(null=True, max_length=15)
	street = models.IntegerField(null=True)
	locality = models.CharField(null=True,max_length=255)
	city = models.CharField(default='Hyderabad', max_length=255)
	phone = models.CharField(max_length=10, null=True)
	price = models.IntegerField(null=True)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		)



class Image(models.Model):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE
	
		)
	image = models.FileField(null=True, upload_to='images/')



class BookingTable(models.Model):

	name = models.CharField(null=True, max_length=20)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=10, null=True)
	persons = models.CharField(max_length=20)
	date = models.DateField(default=now)
	time = models.TimeField(default=now)
	status = models.CharField(null=True, choices=STATUS_CATEGORY, default='Pending...', max_length=100)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE
		)

class Slot(models.Model):

	name = models.CharField(null=True, max_length=20)
	servicedurationfrom = models.TimeField(default=now)
	servicedurationto = models.TimeField(default=now)
	availability = models.CharField(null=True, choices=STATUS_CATEGORY, default='Not Available', max_length=100)



class Slotlist(models.Model):

	name = models.CharField(null=True, max_length=20)
	servicedurationfrom = models.TimeField(default=now)
	servicedurationto = models.TimeField(default=now)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE
		)

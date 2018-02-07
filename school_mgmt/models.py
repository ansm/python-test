from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
       Token.objects.create(user=instance)


# Create your models here.
class Universities(models.Model):

	name = models.CharField(max_length=200)
	logo=models.ImageField(upload_to='post_images/', null=True, blank=True)
	website= models.CharField(max_length=200, blank=True,null=True)
	created_date = models.DateTimeField(default=timezone.now)
	modified_at = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	


	def __str__(self):
		return self.name



class School(models.Model):
	#creator = models.ForeignKey(User)
	owner = models.ForeignKey(User, related_name='Owners')
	universities = models.ForeignKey(Universities)
	name = models.CharField(max_length=200)
	logo=models.ImageField(upload_to='post_images/')
	website=models.CharField(max_length=300, blank=True,null=True)
	created_date = models.DateTimeField(default=timezone.now)
	modified_at = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	


	def __str__(self):
		return self.name		

class Address(models.Model):

	country = (
			('1', 'India'),
			('2', 'Pakistan'), 
			('3', ' Nepal'),
			('4', ' Japan'),
			('5', ' Iran'),
		)

	
	#owner = models.ForeignKey(User)
	street_1 = models.CharField(max_length=200)
	street_2 = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	country = models.CharField(choices=country, max_length=10, null=True, blank=True)
	zipcode=models.IntegerField(null=True, blank=True)
	mobile=models.IntegerField(null=True, blank=True)
	


	def __str__(self):
		return self.city		


class Student(models.Model):

	
	school = models.ForeignKey(School)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	roll_number=models.IntegerField()
	email=models.EmailField(max_length=300, blank=True,null=True)
	date_of_birth=models.DateField(default=timezone.now)
	# date_of_birth = models.CharField(max_length=200)
	address =  models.ManyToManyField(Address)
	created_date = models.DateTimeField(default=timezone.now)
	modified_at = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	


	def __str__(self):
		return self.first_name
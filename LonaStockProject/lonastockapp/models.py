from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.name

class Product(models.Model):
    
	received_quantity = models.IntegerField(default='0', blank=True, null=False)
	product_name = models.CharField(max_length=50, blank=True, null=True)
	received_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='0', blank=True, null=False)
	issued_by = models.CharField(max_length=50, blank=True, null=True)
	# category = models.ForeignKey(Category,default='1', on_delete=models.CASCADE)
	reorder_level = models.IntegerField(default='0', blank=True, null=False)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	# export_to_CSV = models.BooleanField(default=False)
	id = models.AutoField(primary_key=True)
	def __str__(self):
         return self.product_name + " " + str(self.received_quantity) 
    


class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,null=True)
    second_name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
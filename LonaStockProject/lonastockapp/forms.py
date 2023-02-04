from django import forms
from .models import  Product
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductCreateForm(forms.ModelForm):
   class Meta:
     model = Product
     fields = ['product_name','received_quantity','received_by','issue_quantity']
#Intended to prevent having duplicates of  same product names within the system 
     def clean_products(self):
      product_name = self.cleaned_data.get ('product_name')

      if  not product_name:
        raise forms.ValidationError('This field is required')

      for item in Product.objects.all():
          if item.product_name == product_name:
           raise forms.ValidationError(product_name + ' already exists')
          print (product_name)
      return product_name
     
class ProductSearchForm(forms.ModelForm):
   export_to_CSV= forms.BooleanField(required=False)
   class Meta:
      model = Product
      fields = ['product_name',]

class ProductUpdateForm(forms.ModelForm):
  class Meta:
   model = Product
   fields = ['product_name','received_quantity','received_by','issue_quantity']
   
   
 
#class that extends django’s UserCreationForm  to register new users that can access Lona's stock inventory system
class CustomUserCreationForm(UserCreationForm):
    class Meta:
       model = User
       fields = ['username',  'email', 'password1', 'password2']
       
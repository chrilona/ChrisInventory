from ast import Delete
from django.shortcuts import render,redirect
from .models import Product
from .forms import *
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
import csv

# Create your views here.
def Login(request):
  if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request,username=username,password=password)

      if user is not None:
          login(request,user)
          return redirect('list_products')
      else:
          messages.info(request,'Username or Password is incorrect')
            
  return render (request, "login.html")

def register(request):
  form = CustomUserCreationForm()
  
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    
    if form.is_valid():
      user = form.save()
      messages.success(request,'Account created')
    return redirect('list_products') 
  context = {
    'form':form,
  }
  return render (request, "register.html" , context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def home(request):
 
  context = {
   
  }
  return render (request, "home.html" , context)



def change_password(request):
  title = 'Reset password'
  context = {
    "title" : title,
  }
  return render (request, "change_password.html" , context)

def password_changed(request):
  title = 'Password changed succesfully'
  context = {
    "title" : title,
  }
  return render (request, "password_changed.html" , context)
 
def list_products(request):
  title = 'LIST OF PRODUCTS'
  form=ProductSearchForm(request.POST)
  products = Product.objects.all()
  context = {
    "products" : products,
    "form" : form,
    }
  #Enabling checking of a product through filtering content in the list by the name field
  if request.method == 'POST':
    products = Product.objects.filter(product_name__icontains=form['product_name'].value(),)
    if form['export_to_CSV'].value()==True:
      response=HttpResponse(content_type='text/csv')
      response['Content-Disposition']='attachments;filename="List of products.csv"'
      writer=csv.writer(response)
      writer.writerow(['Product Name','Received Quantity','Receiving Clerk'])
      instance=products
      for product in instance:
        writer.writerow([ product.product_name,product.received_quantity,product.received_by])
        return response
      
    context = {
    "products" : products,
    "form" : form,
  }
  return render (request, "list_products.html" , context)


# Enabling user to directly add new information on new entries to the db
def add_product(request):
  form = ProductCreateForm()
  
  if request.method == 'POST':
    form = ProductCreateForm(request.POST)
    
    if form.is_valid():
      form.save()
      messages.success(request, "Product created successfully")
      return redirect('/list_products')
  
  context = {
    "form" : form,
  }
  return render (request, "add_product.html" , context)

#Updating details on a specific product as a product_name cannot have multiple entries
def update_product(request, pk):
	products = Product.objects.get(id=pk)
	form = ProductUpdateForm(instance=products)
	if request.method == 'POST':
		form = ProductUpdateForm(request.POST, instance=products)
		if form.is_valid():
			form.save()
			return redirect('/list_products')

	context = {
		'form':form
	}
	return render(request, 'add_product.html', context)

# View to delete product by filtering it through its ID the pk(primary key)
def delete_product(request):
	products = Product.objects
	if request.method == 'POST':
		Delete(products)
    # messages.success(request,'Product deleted successfully')
		return redirect('/list_products')
	return render(request, 'delete_product.html')




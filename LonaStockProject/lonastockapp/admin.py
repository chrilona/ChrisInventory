from django.contrib import admin
from .models import  Category,Product
from .forms import ProductCreateForm
# Register your models here.

class ProductCreateAdmin(admin.ModelAdmin):
    list_display= ('product_name','received_quantity','received_by','issue_quantity','last_updated')
    form=ProductCreateForm
    search_fields= ('product_name','received_quantity','received_by','issue_quantity')
admin.site.register(Category)
admin.site.register(Product,ProductCreateAdmin)



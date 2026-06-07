from django.contrib import admin
from .models import Collection, Customer, Order, Product

# Register your models here.
admin.site.register(Collection)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)

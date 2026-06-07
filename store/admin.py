from django.contrib import admin
from .models import Collection, Customer, Order, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =  ['title','unit_price']

# Register your models here.
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display=['title','featured_product']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
      list_display =['first_name','last_name','membership','email']
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','customer','payment_status','placed_at']
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from order.models import Order, Customer, Items, ItemCategory


# Register your models here.
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Items)
admin.site.register(ItemCategory)
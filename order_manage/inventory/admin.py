from django.contrib import admin
from inventory.models import DeliveryTeam, Delivery

# Register your models here.
admin.site.register(Delivery)
admin.site.register(DeliveryTeam)

from django.db import models

# Create your models here.
from django.db import models
from order.models import Order
# Create your models here.


class DeliveryTeam(models.Model):
    name = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    last_delivery_time = models.TimeField(null=True, blank=True)

class Delivery(models.Model):
    ONGOING = 0
    COMPLETED = 1
    STATUS_CHOICES  = (
        (0, ONGOING),
        (1, COMPLETED)
    )
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    order_time = models.DateTimeField()
    team = models.ForeignKey(DeliveryTeam, on_delete=models.CASCADE, null=True, blank=True)
    estimated_delivery_time = models.TimeField(null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
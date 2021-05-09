from order.models import Order
from inventory.models import Delivery, DeliveryTeam
from datetime import datetime, timedelta
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from random import randint


@receiver(post_save)
def create_delivery(sender=Order, instance=None, created=None, **kwargs):
    """
        creates Delivery object for every Order placed
        team selected: team with first last_delivery_time
        last_delivery_time: estimated_time of order
    """
    if sender == Order:
        if created:
            prev_delivery = Delivery.objects.all().order_by('order_time').last().order_time.date()
            #if it is the first delivery of the day, pick team randomly
            if prev_delivery != datetime.today():
                i = randint(0,1)
                if i == 0:
                    team = DeliveryTeam.objects.last()
                else:
                    team = DeliveryTeam.objects.first()
            #else: pick the team whose latest_delivery_time is least
            # last_delivery_time is updated after each order is associated with the team
            else:
                team = DeliveryTeam.objects.all().order_by('-last_delivery_time').last()
            delivery = Delivery.objects.create(order=instance, order_time=datetime.now())
            delivery.team = team
            if instance.distance < 5:
                delivery.estimated_delivery_time = (delivery.order_time + timedelta(minutes=40)).time()
            else:
                delivery.estimated_delivery_time = (delivery.order_time + timedelta(minutes=60)).time()
            delivery.save()
            team.last_delivery_time = delivery.estimated_delivery_time
            team.save()
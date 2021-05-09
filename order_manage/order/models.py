from django.db import models
from datetime import date, datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.PositiveIntegerField()
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ItemCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Items(models.Model):
    model_num = models.CharField(max_length=25, unique=True)
    availble = models.PositiveIntegerField()
    price = models.IntegerField()
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_num


class Order(models.Model):
    order_id = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    distance = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(10)])
    items = models.ManyToManyField(Items, through='Quantity')
    created_at = models.DateField(auto_now=timezone.now)

    def save(self, *args, **kwargs):
        curr_order = Order.objects.all().order_by('id').last() 
        super(Order, self).save(*args, **kwargs)
        if curr_order:
            curr_order_id = curr_order.order_id
        else:
            curr_order_id = None
        #first order creation for the day
        if not curr_order or (curr_order.created_at != date.today() and not curr_order_id):
            order_id = datetime.strftime(date.today(),'%d%m-%Y').split('-')
            b = order_id.pop()[2:]
            order_id.append(b)
            order_id = ''.join(order_id)
            order_id = order_id + "_01"        
        elif curr_order.created_at == date.today() and curr_order_id:
            order_id = curr_order.order_id.split('_')
            slno = int(order_id[1]) + 1
            order_id = order_id[0] + "_" + str(slno).zfill(2) 
        if not curr_order_id or order_id:
            Order.objects.filter(id=self.pk).update(order_id=order_id)

    def __str__(self):
        return self.order_id


class Quantity(models.Model):
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
from rest_framework import serializers
from order.models import Order, Customer, Items

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_id = serializers.CharField(required=False)
    class Meta():
        model = Order
        fields = '__all__'
        extra_kwargs = {'items': {'required': False}}

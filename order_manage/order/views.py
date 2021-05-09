from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from order.serializers import CustomerSerializer, OrderSerializer, ItemSerializer
from order.models import Order, Customer, Items, Quantity
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, ListAPIView, RetrieveUpdateAPIView

class OrderCreateRetrieveView(APIView):
    """
        request:  contains data related to the order object to be created
    """
    def post(self, request):
        data = request.data
        print(data)
        order_obj = Order.objects.create(distance=data['distance'], customer=Customer.objects.get(id=data['customer']))
        items = data['items']
        amount = data['amount']
        for i in range(0, len(items)):
            item_obj = Items.objects.get(id=items[i])
            if item_obj.availble < amount[i]:
                return Response({"msg": item_obj.model_num + "is not in sufficient quantity"})
            quan = Quantity.objects.create(items=item_obj, order=order_obj, amount=amount[i])
            item_obj.availble = item_obj.availble - amount[i]
            item_obj.save()
        order_obj = Order.objects.get(id=order_obj.id)
        return Response({"order_id": order_obj.order_id})
        #order_serializer = OrderSerializer(data=data)

class InventoryListAPI(ListAPIView):
    queryset = Items
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Items.objects.all()
    
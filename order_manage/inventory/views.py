from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
import reportlab
from order.models import Order
from inventory.models import Delivery
from datetime import timedelta, datetime


class DeliveryTimeAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            order_obj = Order.objects.get(order_id=request.data['order_id'])
        except Exception as e:
            return Response({"msg ": " Order with the requested id does not exist", "status":status.HTTP_404_NOT_FOUND})
        delivery_obj = Delivery.objects.get(order=order_obj)
        return Response({"msg": "The Estimated Delivery Time is " + str(delivery_obj.estimated_delivery_time) + 
        " for your order " + order_obj.order_id})


class OrderConfirmationStatusAPI(APIView):
    def post(self, request):
        try:
            order_obj = Order.objects.get(order_id=request.data['order_id'])
        except:
            return Response({"msg ": " Order with the requested id does not exist", "status":status.HTTP_404_NOT_FOUND})
        delivery_obj = Delivery.objects.get(order=order_obj)
        status = delivery_obj.status
        team = delivery_obj.team.name
        if status == 0:
            status = "ongoing"
        else:
            status = "completed"
        return Response({"msg": "Your order has confirmed and is in " + status + " state. Team: " + team})


class OrderFinishedAPI(APIView):
    def post(self, request):
        try:
            order_obj = Order.objects.get(order_id=request.data['order_id'])  
        except:
            return Response({"msg ": " Order with the requested id does not exist", "status":status.HTTP_404_NOT_FOUND})
        delivery_obj = Delivery.objects.get(order=order_obj)
        dist = order_obj.distance
        delivery_obj.status = 1
        delivery_obj.team.available  = True
        delivery_obj.save()
        return Response({"msg ": "The order has been changed to completed. "})
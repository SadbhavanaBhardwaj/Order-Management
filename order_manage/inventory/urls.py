
from django.urls import path, include
from inventory.views import DeliveryTimeAPI, OrderConfirmationStatusAPI, OrderFinishedAPI


urlpatterns = [
    path('get_order/', DeliveryTimeAPI.as_view()), 
    path('order_confirmation_status/', OrderConfirmationStatusAPI.as_view()),
    path('finish_order/', OrderFinishedAPI.as_view())
]
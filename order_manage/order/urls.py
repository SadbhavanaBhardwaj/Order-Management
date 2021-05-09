
from django.urls import path, include
from order.views import OrderCreateRetrieveView, InventoryListAPI


urlpatterns = [
    path('create_order/', OrderCreateRetrieveView.as_view()),
    path('get_items/', InventoryListAPI.as_view())
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
]

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('water_order', views.water_order_page, name='water_order'),
    path('order_list', views.order_list, name='order_list'),
    path('test', views.test, name='test'),
]

# doplnit url paterns and get
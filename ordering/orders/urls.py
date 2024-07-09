from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('water_order', views.water_order_page, name='water_order'),
    path('order_list', views.order_list, name='order_list'),
    path('test/<int:id>', views.test, name='test'),
    path('test', views.test2, name='test2'),
]

# doplnit url paterns and get
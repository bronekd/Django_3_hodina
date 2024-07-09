from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def home_page(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def water_order(request):
    template = loader.get_template('water_order.html')
    return HttpResponse(template.render())

def order_list(request):
    template = loader.get_template('order_list.html')
    return HttpResponse(template.render())
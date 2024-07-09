from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import OrderForm


# Create your views here.

def home_page(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
"""
def water_order(request):
    template = loader.get_template('water_order.html')
    return HttpResponse(template.render())
"""

def water_order_page(request):
    #print(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            #first_name = form.cleaned_data['firstname']
            #last_name = form.cleaned_data['lastname']
            #greeting = f"Hi, {first_name} {last_name}!"
            #print(greeting)
            form.save()
            return render(request, 'home.html')
    else:
        form = OrderForm()

    return render(request, 'water_order.html', {'form': form})
def order_list(request):
    template = loader.get_template('order_list.html')
    return HttpResponse(template.render())

def test(request):
    template = loader.get_template('test.html')
    return HttpResponse(template.render())
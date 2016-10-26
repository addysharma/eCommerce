from django.shortcuts import render, HttpResponse, redirect
from .models import User, ShippingAddress, BillingAddress, Order
from ..products.models import Product
# Create your views here.
def index(request):

    return render(request, 'login.html')

def register(request):
    User.objects.register(request.POST)

    return redirect('login-index')

def login(request):
    user = User.objects.login(request.POST)
    request.session['logged_user']= user.id

    return redirect('manage')

def manage(request):
    me = User.objects.get(id=request.session['logged_user'])
    context = {
        'user' : me
    }
    return render(request, 'manage.html', context)

def manage_status(request):

    return redirect('manage')

def order_show(request):

    context = {
        
    }

    return render(request, 'order_show', context)

from django.shortcuts import render, HttpResponse, redirect
from .models import User, Shipping_Address, Billing_Address, Order
from ..products.models import Product
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'login.html')

def register(request):
    User.objects.register(request.POST)

    return redirect('login-index')

def login(request):
    user = User.objects.login(request.POST)
    request.session['logged_user']= user.id
    return redirect('users:manage')

def manage(request):
    me = User.objects.get(id=request.session['logged_user'])
    orders = Order.objects.all()
    context = {
        'user' : me,
        'orders':orders
    }
    return render(request, 'users/orders.html', context)

def manage_status(request):

    return redirect('manage')

def order_show(request):
    context = {
    }

def logout(request):
    if 'logged_user' in request.session:
        request.session.pop('logged_user')
    return redirect('users:login-index')

def productRoute(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request, 'users/products.html', context)

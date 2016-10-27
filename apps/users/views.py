from django.shortcuts import render, HttpResponse, redirect
from .models import User, Shipping_Address, Billing_Address, Order, Order_Products
from ..products.models import Product, Category
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'login.html')

def register(request):
    User.objects.register(request.POST)

    return redirect('users:login-index')

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
    user = User.objects.get(id=1)
    product = Product.objects.get(id=1)
    shipping = Shipping_Address.objects.get(id=1)
    order = Order.objects.get(id=1)
    order_items = Order_Products.objects.all()
    # order = Order.objects.add(customer = user)
    # order = Order.objects.create(customer = user, ship_to = shipping)
    # shipping = Shipping_Address.objects.create(user_ship=user, country="USA", state="CA", city="CoolguyTown", street="1 olive st", zip_code="666")
    # add_item = Order_Products.objects.create(order_id = order, product_id = product, quantity=1)
    # print "added item"
    return HttpResponse(user.first_name + " : " + product.name)

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

def frontpage(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        "categories":categories,
        "products":products
    }
    return render(request, 'products/ecommerce.html', context)
from django.shortcuts import render, HttpResponse, redirect
from .models import User, Shipping_Address, Billing_Address, Order
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

def cart(request):
    user_id= request.session['logged_user']
    user = User.objects.get(id = user_id)
    ship = Shipping_Address.objects.get(user_ship = user)
    bill = Billing_Address.objects.get(user_bill = user)
    print user_id
    print Shipping_Address.objects.get(user_ship = user)
    context = {
        'user': user_id,
        'ships' : ship,
        'bill' : bill
    }

    return render(request, 'realp_cart.html', context)

def cart_process(request):
    user_id = request.session['logged_user']
    user = User.objects.get(id=user_id)
    Shipping_Address.objects.create(name = request.POST['ship_name'], street = request.POST['shipping_address'], city = request.POST['city'], state = request.POST['state'], zip_code = request.POST['zipcode'], user_ship = user)
    Billing_Address.objects.create(name = request.POST['bill_name'], street = request.POST['billing_address'], city = request.POST['city'], state = request.POST['state'], zip_code = request.POST['zipcode'], user_bill = user)
    return redirect('users:cart')

def userRoute(request):
    users = User.objects.all()
    context = {
        "users":users
    }
    return render(request, 'users/users.html', context)

def userDelete(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('users:userRoute')

def productDelete(request, id):
    product = Product.objects.get(id = id)
    product.delete()
    return redirect('users:productRoute')
from django.shortcuts import render, HttpResponse, redirect
from .models import User, Shipping_Address, Billing_Address, Order, Order_Products
from ..products.models import Product, Category
from django.urls import reverse

# Create your views here.
def set_session_data(self, key, value):
    """Shortcut for setting session data regardless of being authenticated"""

    if not self.client.session:
        # Save new session in database and add cookie referencing it

        engine = import_module(settings.SESSION_ENGINE)

        self.client.session = engine.SessionStore()
        self.client.session.save()

        session_cookie = settings.SESSION_COOKIE_NAME
        self.client.cookies[session_cookie] = self.client.session.session_key
        cookie_data = {
            'max-age': None,
            'path': '/',
            'domain': settings.SESSION_COOKIE_DOMAIN,
            'secure': settings.SESSION_COOKIE_SECURE or None,
            'expires': None,
        }
        self.client.cookies[session_cookie].update(cookie_data)

    self.client.session[key] = value
    self.client.session.save()
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
   # me = User.objects.get(id=request.session['logged_user'])
   # context = {
   #     'user' : me,
   #     }
    return render(request, 'users/orders.html')

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

def cart(request):

    return render(request, 'realp_cart.html')

def cart_process(request):

    user_id = request.session['logged_user']
    user = User.objects.get(id=user_id)
    Shipping_Address.objects.create(name = request.POST['ship_name'], street = request.POST['shipping_address'], city = request.POST['city'], state = request.POST['state'], zip_code = request.POST['zipcode'], user_ship = user)
    Billing_Address.objects.create(name = request.POST['bill_name'], street = request.POST['billing_address'], city = request.POST['city'], state = request.POST['state'], zip_code = request.POST['zipcode'], user_bill = user)
    return redirect('users:cart')

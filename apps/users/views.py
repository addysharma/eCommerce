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
    if user.admin == True:
        return redirect('users:manage')
    else:
        return redirect('users:frontpage')

def manage(request):
    #me = User.objects.get(id=request.session['logged_user'])
   # orders = Order.objects.all()
   # context = {
 #       'user' : me,
   #     'orders':orders
  #  }
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
    categories = Category.objects.all()
    context = {
        "products":products,
        "categories":categories
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

def cart(request, id):
    # product = Product.objects.get(id=id)
    # user_id= request.session['logged_user']
    # user = User.objects.get(id = user_id)
    # ship = Shipping_Address.objects.get(user_ship = user)
    # bill = Billing_Address.objects.get(user_bill = user)
    # print user_id
    # print Shipping_Address.objects.get(user_ship = user)
    # context = {
    #     'user': user_id,
    #     'ships' : ship,
    #     'bill' : bill,
    #     'products' : product
    # }

    return render(request, 'realp_cart.html')

def cart_process(request):
# Get the credit card details submitted by the form
    token = request.POST['stripeToken']

    # Create a charge: this will charge the user's card
    try:
      charge = stripe.Charge.create(
          amount=1000, # Amount in cents
          currency="usd",
          source=token,
          description="Example charge"
      )
    except stripe.error.CardError as e:
      # The card has been declined
      pass
    # user_id = request.session['logged_user']
    # user = User.objects.get(id=user_id)
    # Shipping_Address.objects.create(name = request.POST['ship_name'], street = request.POST['shipping_address'], city = request.POST['city'], state = request.POST['state'], zip_code = request.POST['zipcode'], user_ship = user)
    # Billing_Address.objects.create(name = request.POST['bill_name'], street = request.POST['billing_address'], city = request.POST['city'], state = request.POST['state'], zip_code = request.POST['zipcode'], user_bill = user)
    # return redirect('users:cart')

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

def categoryRoute(request):
    categories = Category.objects.all()
    context = {
        "categories":categories
    }
    return render(request, 'users/categories.html', context)

def categoryDelete(request, id):
    category = Category.objects.get(id = id)
    category.delete()
    return redirect('users:categoryRoute')

def makeAdmin(request, id):
    users = User.objects.get(id=id)
    users.admin = True
    print "in the makeAdmin"
    return redirect('users:userRoute')

def removeAdmin(request, id):
    users = User.objects.get(id=id)
    users.admin = False
    print "in the removeAdmin"
    return redirect('users:userRoute')
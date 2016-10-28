from django.shortcuts import render, HttpResponse, redirect
from .models import User, Shipping_Address, Billing_Address, Order, Order_Products
from ..products.models import Product, Category
from django.urls import reverse
import stripe

# Create your views here.
# Set your secret key: remember to change this to your live secret key in production
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = "sk_test_N6LLxkjC77abe8vBl2pGKgzE"


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
    request.session['prod'] = []
    request.session['logged_user']= user.id
    if user.admin == True:
        return redirect('users:manage')
    else:
        return redirect('users:frontpage')

def manage(request):
    orders = Order.objects.all()
    orders2products = Order_Products.objects.all()
    print "in manage"
    for o2p in orders2products:
        print o2p
    products = Product.objects.all()
    context = {'orders':orders,
                'orders2products':orders2products,
                'products':products}
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
    user_id = request.session['logged_user']
    user = User.objects.get(id=user_id)
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        "products":products,
        "categories":categories,
        'user':user
    }
    return render(request, 'users/products.html', context)

def frontpage(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    nums = len(request.session['prod'])

    if request.method == "POST":
        category = Category.objects.get(id=request.POST['category'])
        products= Product.objects.filter(category=category)
        context = {
        'categories' : categories,
            "products":products,
            "nums":nums
        }
    else:
        context = {
            "categories":categories,
            "products":products,
            "nums":nums
        }
    return render(request, 'products/ecommerce.html', context)

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

def cart(request):

    return render(request, 'realp_cart.html')

def add_to_cart(request, id):
    categories = Category.objects.all()
    item = Product.objects.get(id=id)
    if request.method == "POST":
        user_id = request.session['logged_user']
        if not 'prod' in request.session:
            request.session['prod'] = []
        number = request.POST['num']
        appendRoute = request.session['prod']
        appendRoute.append([item.id,number])
        request.session['prod'] = appendRoute
        # request.session['prod'].append([item.id,number])
        print request.session['prod']

    return redirect('products:item_description', id=request.POST['product_id'])


def cart_process(request):
    pass

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

def shoppingCartDisplay(request):
    user  = request.session['logged_user']
    items = request.session['prod']
    products = Product.objects.all()
    total = 0
    for item in items:
        item.append(Product.objects.get(id=item[0]).name)
        price = Product.objects.get(id=item[0]).price
        total = total + int(item[1]) * price
        item.append(price)

    for i in range(0, len(items)):
        items[i].append(i)
        print items[i]
    # for i in range(0, len(items)-1):
    #     item.append(i)
    nums = len(request.session['prod'])
    context = {
        "items":items,
        "products":products,
        "total":total,
        "nums":nums,
        "user" : user
    }
    return render(request,'products/shoppingcart.html', context)

def shoppingCartDelete(request, id):
    items = request.session['prod']
    items.pop(int(id))
    request.session['prod'] = items
    print "after the delete " + str(items)
    return redirect('users:shoppingCartDisplay')

def resetShoppingCart(request):
    request.session['prod'] = []
    return redirect('users:shoppingCartDisplay')

def commitOrder(request):
    items = request.session['prod']
    user = User.objects.get(id=request.session['logged_user'])
    order = Order.objects.create(customer = user)
    for item in items:
        a = Order_Products.objects.create(order = order, product_id = int(item[0]), quantity = int(item[1]))
        print a
    return redirect('users:shoppingCartDisplay')

def generate_order(request):
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
    user = request.session['logged_user']
    shippingA = Shipping_Address.obects.create(user_ship=user ,name = request.POST['name'],country = request.POST['country'], city= request.POST['city'], street = request.POST['street'], zip_code = request.POST['zip_code'])
    billingA = Billing_Address.obects.create(user_bill=user,name = request.POST['name'],country = request.POST['country'], city= request.POST['city'], street = request.POST['street'], zip_code = request.POST['zip_code'])

    return redirect('users:shoppingCartDisplay')

def delete_order(request, id):
    order = Order.objects.get(id = id)
    order.delete()
    return redirect('users:manage')
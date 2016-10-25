from django.shortcuts import render, HttpResponse, redirect
from .models import User, Address
# Create your views here.
def index(request):

    return render(request, 'login.html')

def register(request):
    User.objects.register(request.POST)

    return redirect('/')

def login(request):

    user = User.objects.login(request.POST)
    request.session['logged_user']= user.id

    return redirect('/manage')

def manage(request):
    orders= Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'manage.html', context)

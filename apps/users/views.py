from django.shortcuts import render, HttpResponse

# Create your views here.
def adminLogIn(request):
	render(request, '/adminLogIn.html')

def adminLogInSubmit(request):
	email = request.POST['email']
	password = request.POST['password']

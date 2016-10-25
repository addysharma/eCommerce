from django.shortcuts import render

# Create your views here.
def adminLogIn(request):
	render(request, '/adminLogIn.html')

def adminLogInSubmit(request):
	
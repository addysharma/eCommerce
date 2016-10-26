from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def index(request):
	# category = Category.objects.create(name="Digital Camera")
	category = Category.objects.get(id=1)
	# Product.objects.create(name="Hasselblad H6D", category=category, quantity=2, description="Built like a tank, with a sensor as big as one.", price = 9999.99)
	allproducts = Product.objects.all()
	context ={ 'allproducts':allproducts}
	return render(request, 'products/index.html', context)

def show(request, id):
	product = Product.objects.get(id=id)
	context = {'product': product}
	return render(request, 'products/show.html', context)	


# Create a category
# Category.objects.create(name="Digital Camera")
# category = Category.objects.get(id=1)
# category = Category.objects.all()

# Product.objects.create(name="Hasselblad H6D", category=category[0], description="Built like a tank, with a sensor as big as one.", price = 9999.99)
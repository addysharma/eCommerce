from django.shortcuts import render, HttpResponse
from .models import Category, Product, ImageUploadForm, ProductImage

# Create your views here.
def index(request):
	# category = Category.objects.create(name="Digital Camera")
	# category = Category.objects.get(id=1)
	# Product.objects.create(name="Hasselblad H6D", category=category, quantity=2, description="Built like a tank, with a sensor as big as one.", price = 9999.99)
	allproducts = Product.objects.all()

	categories = Category.objects.all()
	context ={ 
		'allproducts':allproducts,
		'allcategories': categories
		}
	return render(request, 'products/index.html', context)

def show(request, id):
	product = Product.objects.get(id=id)
	context = {'product': product}
	return render(request, 'products/show.html', context)	

def createProduct(request):
	print request.POST
	formInfo = request.POST
	category = Category.objects.get(id=formInfo['categoryid'])
	Product.objects.create(name=formInfo['product'], category=category,quantity=formInfo['quantity'], description=formInfo['description'], price = formInfo['price'])
	return HttpResponse('created new product success')

def createCategory(request):
	category = Category.objects.create(name=request.POST['category'])
	print category.name
	return HttpResponse('Created a new category')


def upload_pic(request):
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			#change this otherwise all images will go to item 1
			product = Product.objects.get(id=1)
			# m = ProductImage.objects.get(product=product)
			m = ProductImage.objects.create(product=product)
			m.product_pic = form.cleaned_data['image']
			m.save()
			return HttpResponse('image upload success')
	return HttpResponseForbidden('allowed only via POST')

# Create a category
# Category.objects.create(name="Digital Camera")
# category = Category.objects.get(id=1)
# category = Category.objects.all()

# Product.objects.create(name="Hasselblad H6D", category=category[0], description="Built like a tank, with a sensor as big as one.", price = 9999.99)
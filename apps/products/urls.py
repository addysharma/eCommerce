from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^show/(?P<id>\w+)$', views.show),	
	url(r'^createproduct$', views.createProduct, name="create_product"),	
	url(r'^createcategory$', views.createCategory, name="create_category"),	
	url(r'^upload_image$', views.upload_pic, name="upload_pic"),
]


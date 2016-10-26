from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^show/(?P<id>\w+)$', views.show),	
	url(r'^createproduct$', views.createProduct),	
	url(r'^upload_image$', views.upload_pic, name="upload_pic"),
]


from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.frontpage, name = "frontpage"),
    url(r'^log$', views.index, name= "login-index"),
    url(r'^logout$', views.logout, name = "logout"),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^manage$',views.manage, name = 'manage'),
    url(r'^productRoute$', views.productRoute, name = 'productRoute'),
    url(r'^orderTest$', views.order_show, name = 'ordershow')

]

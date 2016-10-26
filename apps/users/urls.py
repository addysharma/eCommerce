from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin$', views.admin),
    url(r'^$', views.index, name= "login-index"),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^manage$',views.manage, name= 'manage'),
]

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
    url(r'^add_to_cart/(?P<id>\d+)$', views.add_to_cart, name = 'add_to_cart'),
    url(r'^orderTest$', views.order_show, name = 'ordershow'),
    url(r'^cart_process$', views.cart_process, name = 'cart_process'),
    url(r'^userRoute$', views.userRoute, name = 'userRoute'),
    url(r'^userDelete/(?P<id>\d+)$', views.userDelete, name = 'userDelete'),
    url(r'^productDelete/(?P<id>\d+)$', views.productDelete, name = 'productDelete'),
    url(r'^categoryDelete/(?P<id>\d+)$', views.categoryDelete, name = 'categoryDelete'),
    url(r'^categoryRoute$', views.categoryRoute, name = 'categoryRoute'),
    url(r'^makeAdmin/(?P<id>\d+)$', views.makeAdmin, name = "makeAdmin"),
    url(r'^removeAdmin/(?P<id>\d+)$', views.removeAdmin, name = "removeAdmin"),
    url(r'^shoppingCartDisplay$', views.shoppingCartDisplay, name = "shoppingCartDisplay"),
    url(r'^shoppingCartDelete/(?P<id>\d+)$', views.shoppingCartDelete, name = "shoppingCartDelete"),
    url(r'^resetShoppingCart$', views.resetShoppingCart, name = "resetShoppingCart"),
    url(r'^commitOrder$', views.commitOrder, name = "commitOrder"),
	url(r'^generate_order$', views.generate_order, name= 'generate_order')
]

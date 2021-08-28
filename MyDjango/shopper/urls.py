from django.urls import path
from shopper import views

urlpatterns = [
    path('.html', views.shopperView, name='shopper'),
    path('/login.html', views.loginView, name='login'),
    path('/logout.html', views.logoutView, name='logout'),
    path('/shopcart.html', views.shopcartView, name='shopcart'),
]

from django.urls import path
from commodity import views

urlpatterns = [
    path('.html', views.commodityView, name='commodity'),
    path('/detail.<int:id>.html', views.detailView, name='detail'),
]

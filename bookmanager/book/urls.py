from django.urls import path
from book import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index)
]

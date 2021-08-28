"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 添加项目应用的urls
    # path('', include(('index.urls', 'index'), namespace='index')),
    path('index', include(('index.urls', 'index'), namespace='index')),
    path('commodity', include(('commodity.urls', 'index'), namespace='commodity')),
    path('shopper', include(('shopper.urls', 'index'), namespace='shopper')),
    # 配置媒体资源路由
    # re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media').
]

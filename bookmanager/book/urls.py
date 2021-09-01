from django.urls import path
from book import views
from django.urls.converters import register_converter


# 自定义转换器
# 1.定义转换器
class MobileConverter:
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据交给视图函数
    def to_python(self, value):
        return value

    # def to_url(self, value):
    # 将匹配结果用于反向解析传值时使用
    #     return str(value)


# 2.注册转换器,使用register_converter注册
# register_converter(converter, type_name)
# converter 转换器类
# type_name 转换器名称
register_converter(MobileConverter, 'phone')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    # 获取url的路径参数
    # http://127.0.0.1:8000/index/456/987/
    # 获取到city_id 456  shop_id 987
    # 通过转换器实现对数据类型的匹配
    # 可以使用自定义的转换器实现自己的匹配需求,比如匹配手机号码
    # 使用自定义的转换器识别手机号码
    path('<int:city_id>/<phone:shop_id>/', views.shop),

    # 获取post请求的参数
    path('regist/', views.regist),

    # 获取json数据
    path('jsondata/', views.json_data),

    # 返回JSON数据
    path('jsonresponsedata/', views.return_json),

    # 设置cookies获取cookies
    path('set_cookies/', views.set_cookies),
    path('get_cookies/', views.get_cookies),
]

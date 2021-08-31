import json

from django.shortcuts import render
from book.models import BookInfo, PeopleInfo
from django.http import HttpResponse


# Create your views here.
def index(request):
    """
    首页
    @param request:
    @return:
    """
    context = {
        "name": '点击有惊喜'
    }
    return render(request, 'book/index.html', context=context)


def shop(request, city_id, shop_id):
    """
    店铺
    @param request: 请求
    @param city_id:  城市ID
    @param shop_id:  店铺ID
    @return:
    """
    # 使用GET属性获取查询字符串参数
    data = request.GET
    print(data)

    return HttpResponse("{}城市{}号店铺".format(city_id, shop_id))


def regist(request):
    """
    获取post的form表单数据
    @param request:
    @return:
    """
    # 获取post请求中的form表单的数据,需要使用request请求的POST属性获取
    data = request.POST
    print(data)
    return HttpResponse("post ok")


def json_data(request):
    """
    获取json数据
    @param request:
    @return:
    """
    # 使用request对象的body属性获取发送过来的json数据
    data = request.body
    # print(data)
    data_str = data.decode()
    # print(data_str)
    data_dict = json.loads(data_str)
    print(data_dict)

    return HttpResponse("json ok")

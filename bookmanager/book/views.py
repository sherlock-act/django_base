import json

from django.shortcuts import render
from django.views import View

from book.models import BookInfo, PeopleInfo
from django.http import HttpResponse, JsonResponse


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


def return_json(request):
    """
    返回json数据
    @param request:
    @return:
    """
    data = {
        'name': 'Gundom Seed',
        'year': 2002
    }

    return JsonResponse(data)


def set_cookies(request):
    """
    设置cookies
    @param request:
    @return:
    """
    print(request.META)
    user_name = request.GET['name']
    password = request.GET['pwd']

    response = HttpResponse('set_cookies ok')
    # 在response对象里面设置cookies,max_age指定cookie有效时间
    response.set_cookie('name', user_name, max_age=60 * 60)
    response.set_cookie('pwd', password)

    # 返回响应的时候携带设置cookies信息
    return response


def get_cookies(request):
    """
    返回当前请求携带的cookies
    @param request:
    @return:
    """
    user_name = request.COOKIES['name']
    password = request.COOKIES['pwd']

    return HttpResponse('user_name:{},password:{}'.format(user_name, password))


def set_session(request):
    """
    设置session信息
    @param request:
    @return:
    """
    user_name = request.GET.get("name")
    password = request.GET.get("pwd")

    # 设置session
    request.session["name"] = user_name
    request.session["pwd"] = password

    return HttpResponse("set_session ok")


def get_session(request):
    """
    浏览器与服务器交互,比较session
    @param request:
    @return:
    """
    user_name = request.session.get('name')
    password = request.session.get("pwd")

    return HttpResponse("请求的用户为:{}, 请求用户的密码为:{}".format(user_name, password))


class get_post_request(View):
    """定义类视图,同时处理get和post请求"""

    def get(self, request):
        return HttpResponse("get get")

    def post(self, request):
        return HttpResponse("post post")

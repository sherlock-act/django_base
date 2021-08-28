from django.shortcuts import render
from commodity.models import CommodityInfos, Types


# Create your views here.
def indexView(request):
    """
    首页
    :param request:
    :return: HttpResponse对象
    """
    title = '首页'
    classContent = ''
    commodityInfos = CommodityInfos.objects.all().order_by('-sold')[:8]

    types = Types.objects.all()

    # 儿童服饰
    cl = [x.seconds for x in types if x.firsts == '儿童服饰']
    clothes = CommodityInfos.objects.filter(types__in=cl).order_by('-sold')[:5]

    # 奶粉辅食
    fl = [i.seconds for i in types if i.firsts=='奶粉辅食']
    food = CommodityInfos.objects.filter(types__in=fl).order_by('-sold')[:5]

    # 宝宝用品
    gl = [i.seconds for i in types if i.firsts=='儿童用品']
    goods = CommodityInfos.objects.filter(types__in=gl).order_by('-sold')[:5]

    return render(request, 'index.html', locals())
    # pass

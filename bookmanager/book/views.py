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
    context={
        "name": '点击有惊喜'
    }
    return render(request, 'book/index.html', context=context)


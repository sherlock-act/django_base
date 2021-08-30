from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from polls.models import Question


def index(request):
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {"last_question_list": last_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question {}".format(question_id))


def results(request, question_id):
    return HttpResponse("You're looking at the results of question {}".format(question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))



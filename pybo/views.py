from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
def index(requset):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(requset,'pybo/question_list.html',context)
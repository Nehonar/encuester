from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    html = 'Welcome'
    return HttpResponse(html)

def detail(request, question_id):
    return HttpResponse('This is the question%s.'%question_id)

def results(request, question_id):
    response = 'These are the results of questions%s.'
    return HttpResponse(response% question_id)

def vote(request, question_id):
    return HttpResponse('You vote on question%s.'%question_id)
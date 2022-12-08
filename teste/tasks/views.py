from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.
def hello(request):
    return HttpResponse('Hello world')


def taskList(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})


def seuNome(request, nome):
    return render(request, 'tasks/list.html', {'name':nome})

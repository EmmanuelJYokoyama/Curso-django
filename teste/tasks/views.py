from django.shortcuts import render, get_object_or_404
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


def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})
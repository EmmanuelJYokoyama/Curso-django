from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<Hello world')


def taskList(request):
    return render(request, 'tasks/list.html')


def seuNome(request, nome):
    return render(request, 'tasks/list.html', {'name':nome})

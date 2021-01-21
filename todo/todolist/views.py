from django.shortcuts import render, HttpResponse
from .models import ToDo


def homepage(request):
    return render(request, 'index.html')
    
def test(request):
    todo_list=ToDo.objects.all()
    return render(request, 'test.html',{"todo_list":todo_list})

def test1(request):
    return render(request, 'test1.html')

def test2(request):
    return render(request, 'test2.html')
     
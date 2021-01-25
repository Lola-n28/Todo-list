from django.shortcuts import render, HttpResponse
from .models import ToDo

# Create your views here.
def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list=ToDo.objects.all()
    return render(request, "test.html",{"todo_list":todo_list})

# def test(request):
#     return render(request, "go.html")

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")

def add(request):
    return render(request, "added.html")

def change(request):
    return render(request, "changed.html")

def delete(request):
    return render(request, "deleted.html")
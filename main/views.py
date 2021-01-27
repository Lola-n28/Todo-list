from django.shortcuts import render, HttpResponse,redirect
from .models import ToDo, Books

# Create your views here.
def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list=ToDo.objects.all()
    return render(request, "test.html",{"todo_list":todo_list})

def books(request):
    books=Books.objects.all()
    return render(request, "books.html",{"books":books})

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

def add_todo(request):
    form=request.POST
    text=form["todo_text"]
    todo=ToDo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form=request.POST
    book=Books(
        title=form["title"],
        subtitle=form["subtitle"],
        description=form["description"],
        price=form["price"],
        genre=form["genre"],
        author=form["author"],
        year=form["year"][:10]
        )
    book.save()
    return redirect(books)
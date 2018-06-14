from django.shortcuts import render,redirect
from .forms import AddBookForm
from .models import Book

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/list_books.html', {'books':books})

def add_book(request):
    if request.method=="POST":
        form=AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("/")
        
    else:
        form = AddBookForm()
        
    return render(request, 'books/addbook.html',{'form':form})
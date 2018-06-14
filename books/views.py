from django.shortcuts import render,redirect
from .forms import AddBookForm
from .models import Book

# Create your views here.

def book_list(request):
     if request.user.is_authenticated:
        books = Book.objects.filter(owner=request.user)
     else:
        books = []
     return render(request, 'books/list_books.html', {'books': books})

def add_book(request):
    if request.method=="POST":
        form=AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            book=form.save(commit=False)
            book.owner = request.user
            book.save()
        return redirect("/")
        
    else:
        form = AddBookForm()
        
    return render(request, 'books/addbook.html',{'form':form})
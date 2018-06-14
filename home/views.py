from django.shortcuts import render, HttpResponse
from books.models import Book

# Create your views here.
    
def get_home(request):
    books = Book.objects.all()
    return render(request,"home/index.html",{"books":books})
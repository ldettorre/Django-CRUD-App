from django import forms
from django.core.exceptions import ValidationError
from .models import Book



class AddBookForm(forms.ModelForm): #Model form takes care of normal form fields. we just add a field name and it creates it.
    class Meta:
        model=Book
        fields=['name','author','isbn','notes','image']
    
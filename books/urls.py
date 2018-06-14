from django.conf.urls import url
from .views import add_book



urlpatterns = [
    url(r'^add_book', add_book, name="add_book"),
]   
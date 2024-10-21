from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import Book


def my_view(request):
    return HttpResponse('Hello, Dear Django!')




class BookListView(ListView):
    model = Book                # Model to be used
    template_name = 'book_list.html'  # Template to render the view
    context_object_name = 'books'     # Name of the context variable in the template


# Class-Based View (CBV)
class MyView(View):
    def get(self, request):
        return HttpResponse("Welcome to Django!")
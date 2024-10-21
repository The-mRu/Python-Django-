from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView   

from book.models import Book
from book.forms import ContactForm

def home(request):
    return HttpResponse("Welcome to the Book page! (home function)")


def my_view(request):
    return HttpResponse('Hello, Dear Django from my my_view function!')


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class MyView(View):
    def get(self, request):
        return HttpResponse("Welcome to Django!")


class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url=reverse_lazy('contact_success')

    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)

from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView   

from book.models import Book
from book.forms import ContactForm, BookForm

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

# Task 3: Create view for handling BookForm submission to add new books
class BookCreateView(FormView):
    template_name = 'book_list.html'  # Task 3: Template to render the book form
    form_class = BookForm  # Task 3: Use the BookForm created in forms.py
    success_url = reverse_lazy('book_list')  # Task 3: Redirect to book list after successful form submission

    def form_valid(self, form):
        form.save()  # Task 3: Save the form data (book details) to the database
        return super().form_valid(form)
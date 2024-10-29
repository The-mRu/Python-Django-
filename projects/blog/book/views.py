from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView   

from book.models import Book,Author
from book.forms import ContactForm, BookForm

#from rest framework
from rest_framework.response import Response
from rest_framework.views import APIView
from book.serializers import BookSerializer, AuthorSerializer
from rest_framework import status


def home(request):
    return HttpResponse("Welcome to the Book page! (home function)")


def my_view(request):
    return HttpResponse('Hello, Dear Django from my my_view function!')


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            context = {'x':1}
            return render(request,'login.html',context)  # Redirect to login if not authenticated
        return super().dispatch(request, *args, **kwargs)



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
    
    
#Rest framework API's
class BookListCreate(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        

class AuthorListCreate(APIView):
    def get(self, request):
        authors = Author.objects.all()  # Retrieve all authors
        serializer = AuthorSerializer(authors, many=True)  # Serialize multiple authors
        return Response(serializer.data)  # Return serialized data

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)  # Deserialize JSON to Author object
        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save the new Author instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return success response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return error response if invalid
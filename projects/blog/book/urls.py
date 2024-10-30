# book/urls.py
from django.urls import path
from django.shortcuts import render
from django.contrib import admin
from . import views
from book.views import my_view,BookListView, MyView,ContactFormView, BookCreateView, BookListCreate, AuthorListCreate, BookGetUpdateDelete




urlpatterns = [
    path('', views.home, name='home'),
    path('initial/', my_view),  
    path('book_list/', BookListView.as_view(),name='list'),
    path('initial_class/', MyView.as_view() ),
    path('contact/add/',ContactFormView.as_view()),
    path('contact/success/', lambda request: render(request, 'success/contact_success.html'), name = 'contact_success'),
    path('content/add/', BookCreateView.as_view(), name='book_list'),  # New URL for adding a book
    #REST API
    path('rest_booklist/', BookListCreate.as_view(), name='rest_book_list'),
    path('authors/', AuthorListCreate.as_view(), name='rest_author_list'),  # Route for author API
    path('rest/book/<int:pk>',BookGetUpdateDelete.as_view(), name='rest_book'),

]


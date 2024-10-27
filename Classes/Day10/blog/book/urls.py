# book/urls.py
from django.urls import path
from django.shortcuts import render
from django.contrib import admin
from . import views
from book.views import my_view,BookListView, MyView,ContactFormView, BookCreateView




urlpatterns = [
    path('', views.home, name='home'),
    path('initial/', my_view),  
    path('book_list/', BookListView.as_view()),
    path('initial_class/', MyView.as_view() ),
    path('contact/add/',ContactFormView.as_view()),
    path('contact/success/', lambda request: render(request, 'success/contact_success.html'), name = 'contact_success'),
    path('content/add/', BookCreateView.as_view(), name='book_list'),  # New URL for adding a book    
]

# book/urls.py

from django.urls import path
from book.views import my_view,BookListView, MyView

urlpatterns = [
    path('initial/', my_view),  
    path('book_list/', BookListView.as_view()),
    path('initial_class/', MyView.as_view() ),
]

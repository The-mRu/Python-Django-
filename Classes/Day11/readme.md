# Day-11: Django REST Framework


## Task 1 : Setting Up DRF 
### Install DRF

1. Install Django REST Framework by running:
   ```bash
   pip install djangorestframework
   ```

Add rest_framework to the INSTALLED_APPS list in settings.py:

   ```bash
#blog/settings.py

INSTALLED_APPS = [

    'rest_framework',
]
   ```

## TASK2: Creating API Endpoints

### Create the Serializer

In the book app, create serializers.py and add the following code:

```bash
# book/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```


### Set up Views

In book/views.py, add the following view code:

```bash
# book/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer 
 
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
```
### URL Configuration

In book/urls.py, add the URL path for the API endpoint:

```bash
# book/urls.py
from django.urls import path
from .views import BookListCreate

urlpatterns = [
    path('rest_booklist/', BookListCreate.as_view(), name='rest_book_list'),
]
```
## TASK 3: Testing and Extending the API
- Use Postman to test the API:

  - **GET /api/rest_booklist/:** Fetches all book records.
  - **POST /api/rest_booklist/:** Adds a new book record.
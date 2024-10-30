from django.contrib import admin
from .models import Author, Publisher, Book


# Register models
admin.site.register(Author)

admin.site.register(Publisher)

admin.site.register(Book)


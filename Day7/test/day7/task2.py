from book.models import Author, Book
author = Author.objects.get(name='Rayhan')
books_by_author = Book.objects.filter(author=author)

# Print the books by Rayhan
for book in books_by_author:
    print(book.title)

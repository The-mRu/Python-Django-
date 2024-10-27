# Get the author instance by name (replace "Author Name" with the actual name)
author = Author.objects.get(name="Author Name")

# Get all books by the specific author
books_by_author = Book.objects.filter(author=author)

print(books_by_author)



from django.utils import timezone
from datetime import timedelta

# Calculate the date for 5 years ago
five_years_ago = timezone.now().date() - timedelta(days=5*365)

# Get books published within the last 5 years
recent_books = Book.objects.filter(publication_date__gte=five_years_ago)
print(recent_books)


# Sort all books by price in descending order
sorted_books = Book.objects.all().order_by('-price')
print(sorted_books)


from django.db.models import Avg

# Calculate the average price of all books in the database
avg_price = Book.objects.aggregate(Avg('price'))
print(avg_price)
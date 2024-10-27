


1. **Create Instances of Your Models**:
   You can create new instances of the `Author` and `Book` models, either through the Django shell or your application code.

2. **Using Django Shell**:
   You can test your models directly using the Django shell. To access the shell, run:
   ```bash
   python manage.py shell
   ```
   Then you can create authors and books like this:

   ```python
   from your_app_name.models import Author, Book

   # Create a new author
   author = Author.objects.create(name="Mamun", birthdate="1990-01-01")

   # Create a new book without specifying the price (it defaults to 0.00)
   new_book = Book.objects.create(
       title="New Book Title",
       publication_date="2024-01-01",
       author=author
   )

   # Verify the details
   print(new_book)  # Should print: New Book Title
   print(new_book.price)  # Should print: 0.00
   ```

3. **Check Your Database**:
   You can also use the Django admin interface to check your models. Make sure you have registered your models in `admin.py`:

   ```python
   from django.contrib import admin
   from .models import Author, Book

   admin.site.register(Author)
   admin.site.register(Book)
   ```

   After that, run your server:
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/admin` in your web browser and log in with your superuser account to view and manage your `Author` and `Book` records.

4. **Perform Queries**:
   You can perform various queries now that you have your models set up. Here are a few examples:

   - **Retrieve all books**:
     ```python
     books = Book.objects.all()
     print(list(books))
     ```

   - **Retrieve books by a specific author**:
     ```python
     books_by_author = Book.objects.filter(author__name="Mamun")
     print(list(books_by_author))
     ```

   - **Filter books published in the last 5 years**:
     ```python
     from django.utils import timezone
     from datetime import timedelta

     five_years_ago = timezone.now().date() - timedelta(days=5*365)
     recent_books = Book.objects.filter(publication_date__gte=five_years_ago)
     print(list(recent_books))
     ```

   - **Calculate the average price of all books**:
     ```python
     from django.db.models import Avg

     average_price = Book.objects.aggregate(Avg('price'))['price__avg']
     print("Average Price of Books:", average_price)
     ```

### Summary
You've set up your models, migrated the database, and are now ready to create, query, and manage your data in Django. If you have any specific tasks or questions you'd like to explore further, feel free to ask!
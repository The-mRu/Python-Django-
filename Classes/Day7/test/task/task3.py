# Publisher model, representing a publisher
class Publisher(models.Model):
    # Name of the publisher, a string with a max length of 100 characters
    name = models.CharField(max_length=100)

    # String representation of the Publisher object
    def __str__(self):
        return self.name

# Updating the Book model to include a ForeignKey to Publisher
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    # ForeignKey relation to the Publisher model (many-to-one relation)
    # on_delete=models.CASCADE: if a publisher is deleted, all related books are deleted
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


######Queries#####
# Get the publisher instance by name (replace "Publisher Name" with the actual name)
publisher = Publisher.objects.get(name="Publisher Name")

# Get all books from the specific publisher
books_by_publisher = Book.objects.filter(publisher=publisher)
print(books_by_publisher)


# Get the publisher instance by name
publisher = Publisher.objects.get(name="Publisher Name")

# Count how many books the publisher has published
book_count = Book.objects.filter(publisher=publisher).count()
print(book_count)
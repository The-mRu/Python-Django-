from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)  # Name field
    birthdate = models.DateField()  # Birthdate field

    def __str__(self):
        return self.name


# Publisher model
class Publisher(models.Model):
    name = models.CharField(max_length=200, default="No Publisher")  # Default name for publisher

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)  # Title field
    publication_date = models.DateField()  # Publication date field
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey to Author
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Price field
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)  # Allow null temporarily

    def __str__(self):
        return self.title


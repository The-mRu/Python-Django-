from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)  # Name field
    birthdate = models.DateField(null=True, blank=True)  # Birthdate field (optional)

    def __str__(self):
        return self.name


# Publisher model
class Publisher(models.Model):
    name = models.CharField(max_length=200, default="No Publisher")  # Default name for publisher

    def __str__(self):
        return self.name


# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title field
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateField()  # Publication date field
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey to Author
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Price field with default
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)  # ForeignKey to Publisher, optional
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.title


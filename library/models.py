from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100, help_text="Shelf/Rack location in library")
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
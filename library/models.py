from django.db import models
from django.contrib.auth.models import User

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


class Member(models.Model):
    MEMBERSHIP_TYPES = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('staff', 'Staff'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    membership_type = models.CharField(max_length=10, choices=MEMBERSHIP_TYPES, default='student')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active_member = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.member_id} - {self.user.get_full_name() or self.user.username}"
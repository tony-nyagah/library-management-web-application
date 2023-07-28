from datetime import date
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    """Model representing an author."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(verbose_name="Died", null=True, blank=True)

    class Meta:
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Genre(models.Model):
    name = models.CharField(
        max_length=200, help_text="Enter a book genre (e.g. Science Fiction)"
    )

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter the language the book is written in (e.g. Farsi, English, Swahili)",
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""

    title = models.CharField(max_length=100)
    summary = models.CharField(
        max_length=500, help_text="Enter a brief description of the book"
    )
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
    isbn = models.CharField(
        verbose_name="ISBN",
        max_length=13,
        unique=True,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
    )
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def display_genre(self):
        """Create a string for the genre. This is required to display genre in the Admin"""
        return ", ".join(genre.name for genre in self.genre.all()[:3])


class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        help_text="Unique ID for this particular book across the whole library",
    )
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Book availability",
    )

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)

    @property
    def is_overdue(self):
        """Determines if the book is overdue based on due date and current date."""
        return bool(self.due_back and date.today() > self.due_back)

    def __str__(self):
        return f"{self.book.title} ({self.id})"

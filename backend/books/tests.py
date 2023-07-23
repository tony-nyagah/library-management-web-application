from django.test import TestCase
from django.urls import reverse
from books.models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A good title",
            synopsis="An excellent synopsis",
            author="Tom Christie",
            available_copies="12",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.synopsis, "An excellent synopsis")
        self.assertEqual(self.book.author, "Tom Christie")
        self.assertEqual(self.book.available_copies, "12")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "excellent synopsis")
        self.assertTemplateUsed(response, "book_list.html")

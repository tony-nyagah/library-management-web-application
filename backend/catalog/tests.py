from catalog.models import Author, Book, Genre, Language
from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.test_author = Author.objects.create(first_name="Big", last_name="Bungus")
        self.test_genre_1 = Genre.objects.create(name="Fantasy")
        self.test_genre_2 = Genre.objects.create(name="Science Fiction")
        self.test_language = Language.objects.create(name="English")
        self.test_book = Book.objects.create(
            title="The Big Book",
            summary="This is the summary",
            isbn="123456789",
            author=self.test_author,
            language=self.test_language,
        )
        self.test_book.genre.add(self.test_genre_1, self.test_genre_2)

    def test_model_content(self):
        self.assertEqual(self.test_book.title, "The Big Book")
        self.assertEqual(self.test_book.author, self.test_author)
        self.assertEqual(self.test_book.language, self.test_language)
        self.assertEqual(self.test_book.isbn, "123456789")
        self.assertEqual(self.test_book.summary, "This is the summary")
        self.assertEqual(len(self.test_book.genre.all()), 2)

    def test_api_bookview(self):
        response = self.client.get(reverse("book-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.test_book)

    def test_api_bookdetail(self):
        response = self.client.get(
            reverse("book-detail", kwargs={"pk": self.test_book.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, "The Big Book")

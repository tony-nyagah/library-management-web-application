from django.test import TestCase

from catalog.models import Author, Book, Genre, Language


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_author = Author.objects.create(first_name="Big", last_name="Bungus")
        cls.test_genre = Genre.objects.create(name="Fantasy")
        cls.test_language = Language.objects.create(name="English")
        cls.test_book = Book.objects.create(
            title="The Big Book",
            summary="This is the summary",
            isbn="123456789",
            author=cls.test_author,
            language=cls.test_language,
        )

    def test_model_content(self):
        self.assertEqual(self.test_book.title, "The Big Book")
        self.assertEqual(self.test_book.author, self.test_author)
        self.assertEqual(self.test_book.language, self.test_language)
        # self.assertEqual(self.test_book.genre, self.test_genre)
        self.assertEqual(self.test_book.isbn, "123456789")
        self.assertEqual(self.test_book.summary, "This is the summary")

from django.test import TestCase

from catalog.models import Author, Book, Genre, Language


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

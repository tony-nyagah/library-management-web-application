from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from catalog.models import Author, Book


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(first_name="Test", last_name="Case")
        cls.book = Book.objects.create(
            title="Django for APIs",
            summary="Learn to use Django to power API creation.",
            author=cls.author,
            available_copies="2",
        )

    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
